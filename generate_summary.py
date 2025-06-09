import os
import json
import sys
from code_reader import read_codebase
from analyzer import chunk_code, analyze_code_chunk

def generate_summary(code_path, output_file="sakila_analysis.json"):
    print(f"Reading code from: {code_path}")

    if os.path.isfile(code_path):
        with open(code_path, 'r') as f:
            code_data = {code_path: f.read()}
    else:
        code_data = read_codebase(code_path)

    if not code_data:
        print("No code files found to analyze.")
        return

    result = {}

    for path, code in code_data.items():
        print(f"\nAnalyzing file: {path}")
        try:
            chunks = chunk_code(code)
            print(f"Split into {len(chunks)} chunks")
            analyses = []
            for i, chunk in enumerate(chunks):
                print(f"Processing chunk {i+1}/{len(chunks)}")
                response = analyze_code_chunk(chunk)

                structured_response = {
                    "chunk_index": i + 1,
                    "summary": response.get("summary", ""),
                    "functions": response.get("functions", []),
                    "classes": response.get("classes", []),
                    "dependencies": response.get("dependencies", []),
                    "complexity": response.get("complexity", {}),
                    "comments": response.get("comments", "")
                }

                analyses.append(structured_response)

            result[path] = analyses
        except Exception as e:
            print(f"Error analyzing {path}: {e}")
            continue

    with open(output_file, 'w') as f:
        json.dump(result, f, indent=4)

    print(f"\nAnalysis completed! Output saved to: {output_file}")

if __name__ == "__main__":
    path_arg = sys.argv[1] if len(sys.argv) > 1 else "./src"
    generate_summary(path_arg)
