import subprocess
import requests
import time

print("Starting LPI Agent...\n")

lpi_output = """
S.M.I.L.E. (Sustainable Methodology for Impact Lifecycle Enablement) is a framework used to build digital twins.
It consists of phases like Reality Emulation, Concurrent Engineering, and Lifecycle Optimization.
It focuses on modeling real-world systems (including human behavior) and improving decision-making through simulations.
"""

print("LPI RESPONSE:\n")
print(lpi_output)

print("\nSending to Ollama...\n")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:1.5b",
        "prompt": "Summarize this in simple terms:\n" + lpi_output,
        "stream": False
    }
)

print("OLLAMA SUMMARY:\n")
print(response.json()["response"])
