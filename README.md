# Java Codebase Analyzer using Open-Source LLM (Qwen + Ollama)

A lightweight, modular tool that scans Java source code, intelligently chunks large files, and generates **structured, machine-readable summaries** using an open-source LLM (`qwen2.5-coder:7b`) running locally via **Ollama**.

---

## Objective

Enable teams to **quickly understand large Java codebases** - especially in unfamiliar legacy projects - by automating the summarization process with AI, **without sending any data to cloud-based LLMs**.

This tool is ideal for:
- Onboarding new developers
- Conducting internal code reviews

---

## Approach & Architecture

### 1. Read & Identify Files
The script starts by recursively scanning the given path for Java files. It supports both:
- Full directory analysis
- Single file analysis (if a `file path` is passed)

### 2. Code Chunking
Large Java files are split into **logical chunks** (based on line count or delimiters), ensuring:
- Tokens stay within LLM context limits
- Each chunk remains semantically meaningful

### 3. LLM-Powered Summarization
Each chunk is sent to the **Qwen model**, running locally via `Ollama`. The prompt ensures structured output in JSON format, including:
- Summary
- Key classes/functions
- Dependencies
- Cyclomatic complexity
- Developer insights

### 4. Output Consolidation
All LLM responses are cleaned, parsed, and structured into a single JSON file (`sakila_analysis.json`) for easy consumption or integration into other tools.

---

## Major Files in This Project

| File | Responsibility |
|------|----------------|
| `generate_summary.py` | CLI entry point. Parses CLI args and initiates the pipeline. |
| `code_reader.py` | Scans the directory or single file, returning Java code as dictionary. |
| `analyzer.py` | Chunks code and invokes LLM for structured analysis. |


---

## How to run
**Installation** : ```python3 -r requirements.txt```
**Run** : # to run model on full codebase ```python3 generate_summary.py```
**Run** : # to run model on single file ```python3 generate_summary.py <file path>```
---

## Open Source LLM Usage

This tool is **fully offline** and respects your code privacy. It uses:

- **LLM:** [Qwen](https://ollama.com/library/qwen2.5) (by Alibaba)
- **Runtime:** [Ollama](https://ollama.com/)  -  a local LLM manager
- **Command:** The LLM is invoked using command in terminal:
  ```
  ollama run qwen2.5-coder:7b
  ```
