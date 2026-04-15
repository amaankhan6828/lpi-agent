# LPI Agent
This is a simple AI agent built using the LPI concepts and a local LLM (Ollama).

## What it does
1) Uses a sample LPI (SMILE methodology) output
2) Sends it to a local LLM (qwen2.5:1.5b via Ollama)
3) Generates a summarized response

## How it works
1. A sample LPI response is defined inside the script
2. The agent sends this data to Ollama using a local API
3. The model processes and returns a clean summary

## Tech Stack
- Python
- Requests library
- Ollama (local LLM)

## How to run
```bash
pip install -r requirements.txt
python agent.py
