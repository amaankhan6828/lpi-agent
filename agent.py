import subprocess
import json
import requests

server = subprocess.Popen(
    ["node", "../lpi-developer-kit/dist/src/index.js"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
init_msg = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {
            "name": "lpi-agent",
            "version": "1.0"
        }
    }
}
server.stdin.write(json.dumps(init_msg) + "\n")
server.stdin.flush()


tool_call = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "smile_overview",
        "arguments": {}
    }
}
server.stdin.write(json.dumps(tool_call) + "\n")
server.stdin.flush()

response = server.stdout.readline()
print("LPI RESPONSE:\n", response)


ollama_response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:1.5b",
        "prompt": "Summarize this:\n" + response,
        "stream": False
    }
)

print("\nOLLAMA SUMMARY:\n", ollama_response.json()["response"])
