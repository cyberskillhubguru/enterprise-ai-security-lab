# ⚔️ Attack-Box Orchestration Suite

This workspace contains automated testing frameworks, offensive script workflows, and adversarial payload configurations executed from the local security testing laptop.

## 🚀 Usage Instructions

### 1. Automated Prompt Fuzzer
Executes sequential fuzzing matrix requests against the frontier target gateway to evaluate input sanitization efficiency.
```bash
python prompt-injection/fuzzer.py
```

### 2. MCP Exploitation Vector
Demonstrates an advanced breakout where an attacker uses an LLM context window to inject downstream SQL code via standard protocol arguments.
```bash
python mcp-tool-abuse/exploit_sql_pivot.py
```
