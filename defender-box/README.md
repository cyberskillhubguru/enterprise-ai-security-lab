# 🛡️ Defender-Box: Gateways, AI Firewalls, and Audit Logging

This directory documents the defensive architecture, containment policies, and filtering mechanisms designed to intercept, analyze, and neutralize adversarial attacks targeting the enterprise AI gateway.

In this architecture, the **Defender Box** acts as a strategic security bastion layer situated strictly between the untrusted public internet (Zone A) and the Target AI application environment (Zone B).

---

## 🎨 1. Defensive Layering Strategy

To protect an LLM-orchestrated environment from prompt injections and MCP tool abuse, the defense operates on a framework of **Defense-in-Depth**.

```text
[ Incoming Request ]
         │
         ▼
┌─────────────────────────────────┐
│ Layer 1: Input Regex Sanitizer  │ ──► Drops obvious SQL / Command payloads
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ Layer 2: LLM Guard Firewall     │ ──► Semantic scanning (e.g., Llama Guard)
└─────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│ Layer 3: Least-Privilege MCP    │ ──► Hardened backend parameters
└─────────────────────────────────┘
         │
         ▼
[ Executed Safely on Target ]
```

### 🧱 Core Defensive Pillars:
1. **Input Inspection (The Ingress Proxy):** Scrubbing raw incoming strings for classic application attack vectors (such as quote escapes, union strings, or script tags) before they ever reach the target AI context.
2. **Semantic Boundary Scanning (LLM Firewalls):** Utilizing lightweight classification models (like Llama Guard or custom small language models) to detect malicious formatting intent, such as jailbreaks or direct system prompt overrides.
3. **Downstream Hardening (Parameterized MCP Tools):** Refusing to allow tools to execute raw concatenated parameters. Every database abstraction layer must rely on parameterized queries or strict data type schemas.

---

## 📋 2. Remediating the MCP Tool Abuse Vulnerability

To demonstrate end-to-end security engineering proficiency, this section documents the transformation of an unsafe database query tool into an enterprise-hardened protocol structure.

### ❌ The Vulnerable Pattern (As-Built)
The initial target application deployment utilized a concatenated formatting loop that easily allowed an attacker to break out of data constraints via simple quote injection:
```python
# HIGH RISK: Allows arbitrary command and query injection
unsafe_query = f"SELECT name, price FROM products WHERE name = '{product_name}'"
```

###  The Remediated Pattern (Secure Fix)
The hardened model explicitly separates code execution from untrusted user text inputs by utilizing parameterized query arguments. Even if an attacker passes a complex payload, it is processed purely as a literal data string rather than executable code:
```python
# SECURE: Enforces strict query boundaries via argument parameters
safe_query = "SELECT name, price FROM products WHERE name = ?"
cursor.execute(safe_query, (product_name,))
```

---

## 📊 3. Centralized Audit Logging Schema

Defending an AI application requires thorough insight into what tools the agent is attempting to execute. The Defender Box acts as a centralized syslog server capturing all MCP transaction payloads:

* **Inbound Prompt Hash:** Tracking individual sessions to spot rapid, automated fuzzing behavior.
* **Extracted Tool Arguments:** Logging the exact strings passed from the LLM layer down to the protocol server to audit anomalous query arguments.
* **Error Tracking:** Flagging database syntax exceptions immediately, as these are primary indicators of active injection discovery attempts.
