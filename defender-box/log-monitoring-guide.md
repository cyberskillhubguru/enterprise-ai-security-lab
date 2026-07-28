\# 📊 Enterprise AI \& MCP Log Monitoring Guide



This document defines the security auditing standards, detection logic, and logging strategies used by the `Defender-Box` to identify and alert on active adversarial attacks against the enterprise AI infrastructure.



\---



\## 🔍 1. High-Value Log Sources



To catch modern AI and Model Context Protocol threats, traditional network logging must be paired with application-level semantic auditing. The lab monitors three primary data streams:



1\.  \*\*AI Gateway Access Logs (`vulnerable-app` runtime):\*\* Tracks raw incoming strings, user session tokens, and response latencies.

2\.  \*\*MCP Protocol Audit Trail (`mcp-server` transaction logs):\*\* Records the exact functions called by the LLM and the raw arguments passed into backend system tools.

3\.  \*\*Database Query Logs (`pi3b-sql-db` engine logs):\*\* Audits compiled database interactions to capture syntax execution anomalies and unauthorized table access attempts.



\---



\## 🚨 2. Signature Detection Rules (SIEM / Analytics Logic)



The following monitoring signatures are implemented within the log analysis pipeline to trigger high-priority alerts for security analysts.



\### Rule 01: MCP SQL Argument Injection Detection

\*   \*\*Monitored Log:\*\* `target-mcp-server` standard output lines.

\*   \*\*Threat Vector:\*\* Exploit attempts targeting unvalidated tool variables.

\*   \*\*Detection Query / Keyword Pattern:\*\*

&#x20;   ```text

&#x20;   \[MCP LOG] Executing Downstream Tool Query: \* UNION SELECT \*

&#x20;   \[MCP LOG] Executing Downstream Tool Query: \* OR 1=1 \*

&#x20;   ```

\*   \*\*Alert Severity:\*\* CRITICAL

\*   \*\*Response Action:\*\* Automatically terminate the active user session token and isolate the frontend proxy container.



\### Rule 02: Indirect Injection Context Overrides

\*   \*\*Monitored Log:\*\* `target-ai-frontend` chat transaction records.

\*   \*\*Threat Vector:\*\* Document tampering via weaponized RAG files.

\*   \*\*Detection Query / Keyword Pattern:\*\*

&#x20;   ```text

&#x20;   "SYSTEM UPDATE:" OR "IGNORE PAST INSTRUCTIONS" OR "OVERRIDE DIRECTIVE"

&#x20;   ```

\*   \*\*Alert Severity:\*\* HIGH

\*   \*\*Response Action:\*\* Flag the originating session for manual manual review and audit recent vector repository index uploads.



\### Rule 03: Post-Exploit System Breakout (RCE Discovery)

\*   \*\*Monitored Log:\*\* `target-mcp-server` operational error tracks.

\*   \*\*Threat Vector:\*\* Shell invocation or python sandboxing escape attempts.

\*   \*\*Detection Query / Keyword Pattern:\*\*

&#x20;   ```text

&#x20;   "import os" OR "subprocess.Popen" OR "sh" OR "bash"

&#x20;   ```

\*   \*\*Alert Severity:\*\* CRITICAL

\*   \*\*Response Action:\*\* Instantly trigger container containment protocols and isolate the target node interface on the internal network.



\---



\## 🛠️ 3. Verification \& Mock Log Generation



When the physical Raspberry Pi 5 cluster is active, analysts can verify logging health by executing the automated test strings located in the `/attack-box/` framework and cross-referencing the centralized log repository to ensure indicators are generating correct detection event tags.



