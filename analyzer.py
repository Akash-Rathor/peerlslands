from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
import re


llm = OllamaLLM(model="qwen2.5-coder:7b")

def chunk_code(text, max_chars=1500):
    splitter = RecursiveCharacterTextSplitter(chunk_size=max_chars, chunk_overlap=200)
    return splitter.split_text(text)

def extract_json_from_response(response_text):
    """
    Extract JSON object from the LLM response, ignoring surrounding markdown or extra text.
    """
    json_match = re.search(r"```json(.*?)```", response_text, re.DOTALL)
    if not json_match:
        json_match = re.search(r"```(.*?)```", response_text, re.DOTALL)
    if json_match:
        json_str = json_match.group(1).strip()
    else:
        json_str = response_text.strip()

    start = json_str.find('{')
    end = json_str.rfind('}')
    if start != -1 and end != -1:
        json_str = json_str[start:end+1]
    else:
        json_str = json_str

    return json_str

def analyze_code_chunk(code_chunk):
    prompt = f"""
        You are a senior software engineer and architect. Analyze the following Java code and return a structured JSON with the following keys:
        - summary: A high-level overview of what this code chunk does.
        - functions: List of function/method names in this chunk.
        - classes: List of class names defined in this chunk.
        - dependencies: List of external classes or modules this chunk relies on.
        - complexity: An object with keys 'cyclomatic' and 'nesting_depth' (estimates are fine).
        - comments: Any useful observations about the code quality, design, or structure.

        Here is the code chunk:
        \"\"\"
        {code_chunk}
        \"\"\"
        Only return valid JSON, no explanation.
        """

    response = llm.invoke(prompt)

    try:
        json_str = extract_json_from_response(response)
        return json.loads(json_str)
    except Exception as e:
        print("Failed to parse LLM response:", response)
        return {
            "summary": "",
            "functions": [],
            "classes": [],
            "dependencies": [],
            "complexity": {"cyclomatic": 0, "nesting_depth": 0},
            "comments": "LLM failed to parse the chunk."
        }