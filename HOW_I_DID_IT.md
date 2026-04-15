## Level 3 — What I Did

I built a simple AI agent using Python that connects to the LPI sandbox and a local LLM.
Initially, I started the LPI server and called one of the tools (smile_overview) using a subprocess.
Then, I passed the output to a locally running model using Ollama (qwen2.5:1.5b).
The model generated a summary of the response, showing how LPI tools and LLMs can be combined to build agents.

What I learned:
1) How MCP communication works using stdin/stdout
2) How to connect LPI tools with a local LLM
3) How to build a basic AI agent pipeline
