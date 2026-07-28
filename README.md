# enterprise-ai-security-lab
An 8 - node physical and virtual enterprise homelab for AI Pentesting, Model Context Protocol (MCP) security, and LLM adversarial engineering.

## Disclaimer - This is for Educational Purpose Only, do not do any of these commands on an un-authorized Network,
## unless you have writing consent from the organization ##

# 🏢 Enterprise AI Security & MCP Penetration Testing Lab

An advanced, multi-tiered enterprise security testing environment dedicated to demonstrating hands-on engineering skills in **AI Pentesting**, **Model Context Protocol (MCP) Security**, and **Defensive LLM Architecture**.

---

## 🚫 Critical Disclaimer & Safety Policy

> [!WARNING]  
> **FOR EDUCATIONAL AND HOMELAB TESTING PURPOSES ONLY.**  
> This project is built entirely for research, training, and professional technical demonstration. All exploit proof-of-concepts, scripts, and targeting parameters are designed strictly to run within an isolated, non-production local loopback environment using synthetic/mock corporate data. Under no circumstances should any scripts or techniques found in this repository be executed against real-world production applications or third-party infrastructure without explicit authorization.

---

## 🎯 What is this Project About?

This repository documents the structural engineering, continuous testing, and defense of a distributed corporate network surface. As enterprise systems rapidly integrate Artificial Intelligence and Model Context Protocol (MCP) servers to grant LLMs access to internal data, traditional security vectors mutate. 

This lab bridges the gap between traditional Application Security (AppSec) and modern AI Security by mapping out real-world corporate attack paths:
1. **AI Gateway Exploitation:** Testing frontier gateway applications against direct and indirect prompt injection.
2. **MCP Protocol Vulnerabilities:** Investigating how unvalidated user parameters passed through LLMs can trigger argument injection and tool abuse on downstream systems.
3. **Lateral Network Pivoting:** Demonstrating how an attacker can leverage a compromised AI execution runtime to pivot into segmented corporate databases and file shares.

---

## 🚀 Why Am I Building This?

I am engineering this multi-month project to definitively showcase the practical, architecture-level competencies required for modern **AI Security Engineer**, **MCP Security specialist**, and **AI Penetration Tester** roles. 

Rather than relying on theoretical concepts or running isolated scripts, this portfolio explicitly proves:
*   **Infrastructure Mastery:** The ability to simulate a true corporate network layout using physical hardware separation and virtual containerization.
*   **Offensive Ingenuity:** Writing structured python fuzzers, parameter injection exploits, and adversarial testing harnesses specifically targeting AI-to-tool connections.
*   **Defensive Engineering:** Implementing real-world containment boundaries, input sanitation controls, API proxies, and structured logging frameworks to stop attacks before they execute.

---

## 🏗️ Lab Architecture

The environment bridges a local host environment with a bare-metal hardware cluster to replicate strict network micro-segmentation.

### Hardware Node Distribution
*   **The Attack Box:** Gigabyte Laptop (NVIDIA RTX 3060 GPU) — Generates local adversarial payloads, models automated script routines, and simulates the external threat actor.
*   **The Defender Gateway:** Raspberry Pi 5 (Node 1) — Serves as the security operational center, parsing traffic through LLM Firewalls (e.g., Llama Guard) and managing secure centralized syslogs.
*   **The Target Application:** Raspberry Pi 5 (Node 2) — Hosts the front-facing customer application and running Model Context Protocol servers.
*   **The Segmented Enterprise LAN:** 5x Raspberry Pi 3B units isolated completely from external public traffic, simulating internal infrastructure tiers:
    *   `Node 1 (Vector Storage):` Hosting semantic embeddings (Qdrant/Milvus) for RAG querying.
    *   `Node 2 (Relational Core):` Running PostgreSQL to store simulated corporate credentials and assets.
    *   `Node 3 (Network File System):` Holding passive shared office records (NFS/Samba).
    *   `Node 4 (Ingestion Engine):` Simulating an active automation pipe processing user feedback logs.
    *   `Node 5 (Shadow IT Node):` An unhardened, unpatched system to test and demonstrate lateral movement security risks.

### Simplified Network Flow
```text
      [ Attack Box (RTX 3060) ] 
                 │ 
                 ▼ (External WAN / Perimeter Traffic)
      [ Defender Pi 5 (LLM Firewall) ]
                 │
                 ▼ (Filtered Traffic)
      [ Target Pi 5 (AI & MCP Gateway) ]
                 │
  ┌──────────────┴──────────────┬────────────────────────┐
  ▼                             ▼                        ▼
[Pi 3B: Vector DB]     [Pi 3B: Relational DB]    [Pi 3B: Storage/Shadow IT]
  └──────────────────── (Isolated Enterprise LAN) ───────┘
```

---

## 📂 Repository Blueprint

```text
├── .github/workflows/      # Automated security checks (CI/CD) and code linting
├── documentation/          # Lab architecture diagrams and attack write-ups
├── attack-box/             # Python exploit scripts & automated testing frameworks
│   ├── prompt-injection/   # Local input fuzzers and payload matrices
│   └── mcp-tool-abuse/     # Downstream argument injection validation scripts
├── target-infrastructure/  # The core vulnerable deployments (Docker-in-Docker replication)
│   ├── docker-compose.yml  # Local virtual emulation of the 8-node lab
│   ├── mcp-server/         # Vulnerable & patched MCP server source code
│   └── vulnerable-app/     # Frontend chat interface logic
└── defender-box/           # Defensive rule configurations, proxies, and firewall setups
```

---

## 🛠️ Phase 1 Setup: Running the Local Emulation

To test this layout locally on your own test bench machine using Docker prior to hardware migration:

1. Clone this repository locally.
2. Spin up the isolated virtual network infrastructure containers:
   ```bash
   cd target-infrastructure
   docker compose up -d
   ```
3. Execute the automated fuzzing scripts found inside the `/attack-box/` framework to evaluate the baseline application constraints.
