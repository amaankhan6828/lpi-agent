# Level 3 — What I Did

I built a basic and simple AI agent using Python that integrates LPI concepts with a local LLM (Ollama).
Instead of directly calling the LPI sandbox, I simulated an LPI (SMILE methodology) output inside the script. This keeps the agent lightweight and focused on the core idea of combining structured knowledge with a language model.

The agent takes this LPI-style output and sends it to a locally running LLM (qwen2.5:1.5b via Ollama), which generates a simplified summary.

This demonstrates how AI agents can combine structured system outputs with LLM reasoning to produce useful insights.

## What I Learned

1. How to connect Python applications with a local LLM using APIs  
2. How to design a simple agent pipeline (input → processing → output)  
3. How structured data (like LPI outputs) can be enhanced using LLMs  
