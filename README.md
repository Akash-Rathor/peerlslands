# Java Codebase Analyzer using LLMs

This project analyzes a Java codebase and generates structured, machine-readable summaries for each file. It leverages a Large Language Model (LLM) to provide insights into the components, relationships, and complexity of the codebase.

---

## Objective

To automate the process of understanding large codebases by generating structured summaries from source code using an LLM. This is especially useful for onboarding, documentation, and software audits.

---

## How It Works

1. **Code Reading**: Recursively traverses the provided path to read `.java` files.
2. **Chunking**: Splits large files into manageable chunks to avoid context overflow in LLMs.
3. **LLM Analysis**: Sends each chunk to an LLM with a consistent prompt for summary generation.
4. **JSON Structuring**: Cleans and parses the LLM response into structured JSON.
5. **Output**: Consolidates and writes the results to a single `sakila_analysis.json` file.

---

## Methodologies Employed

- **Recursive Directory Traversal**: Automatically reads all `.java` files within nested directories.
- **Code Chunking Strategy**: Large files are split into logical chunks to remain within LLM token limits.
- **Prompt Engineering**: A concise, deterministic prompt is used to guide the LLM’s output structure.
- **Regex-Based JSON Extraction**: Ensures clean parsing by removing markdown artifacts (like triple backticks).
- **Fallback Strategy**: Gracefully handles failed LLM responses with structured placeholder data.

---

## Output Structure (per chunk)

Each chunk returns:

```json
{
  "summary": "High-level overview of what the code does.",
  "functions": ["methodA", "methodB"],
  "classes": ["ClassName"],
  "dependencies": ["javax.persistence", "java.util.List"],
  "complexity": {
    "cyclomatic": 3,
    "nesting_depth": 2
  },
  "comments": [
    "Observations or suggestions from the LLM about the code."
  ]
}
