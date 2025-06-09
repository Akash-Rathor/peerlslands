import os

def read_codebase(path):
    code_files = {}

    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            code_files[path] = f.read()
        return code_files


    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(('.java', '.py', '.js')):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        code_files[full_path] = f.read()
                except Exception as e:
                    print(f"Failed to read {full_path}: {e}")

    return code_files
