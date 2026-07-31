# 🗺️ Enterprise Network Topology & Traffic Flow Blueprint

This document contains the detailed network architecture, interface configurations, and data flow pathways for the `enterprise-ai-security-lab`. 

---

## 🌐 1. Architectural Design Principles

To simulate an authentic enterprise environment, this lab relies heavily on **Network Micro-Segmentation**. This strategy ensures that high-risk perimeter nodes (like the AI Chat Gateway) are restricted from talking directly to backend servers unless specifically brokered through audited protocols and secure channels.

### Security Zones Defined:
1.  **Zone A: Perimeter WAN (External Network)** — Simulates public-facing internet traffic. The Attack Box operates exclusively in this zone.
2.  **Zone B: Demilitarized Zone (DMZ / Transit Net)** — Contains defensive proxies and application ingress filters. The Defender Gateway sits here to scrub incoming packets.
3.  **Zone C: Isolated Enterprise LAN (Core Backend)** — Completely cut off from the external network. Contains database nodes, file storage repositories, and internal systems. These nodes can only communicate with the Target AI Gateway.

---

## 📊 2. Physical Layout & Hardware Network Diagram (Phase 2 Cluster)

The diagram below reflects the final bare-metal architecture deployment across the 8-node physical layout using managed VLAN interfaces.

```text
       [ Zone A: Public-Facing Attack Space ]
                         │
         ┌───────────────┴───────────────┐
         │ (IP Address)              │ (IP Address)
         ▼                               ▼
  [ Attack Laptop ]              [ Other WAN Hosts ]
  (Gigabyte RTX 3060)
         │
         │ (Inbound Request Traffic via HTTPS / API)
         ▼
 ───────────────────────────────────────────────────────── [ VLAN 10: Perimeter WAN ]
         │
         ▼ (Interface 1: Emulated Public IP)
  [ Defender Node ] 
  (Raspberry Pi 5 #1)
         │
         ▼ (Interface 2: Internal Ingress Proxy)
 ───────────────────────────────────────────────────────── [ VLAN 20: DMZ / Scrubbed Ingress ]
         │
         ▼ (Audited Traffic Delivery Only)
  [ Target AI Gateway ]
  (Raspberry Pi 5 #2)
         │
         └───────────────┬───────────────────────────────┐
                         │ (System API Routing via MCP)  │
                         ▼                               ▼
 ───────────────────────────────────────────────────────── [ VLAN 30: Isolated Enterprise LAN ]
                         │                               │
         ┌───────────────┴───────────────┐               │
         ▼                               ▼               ▼
  [ Database Node #1 ]           [ Database Node #2 ]  [ File/Shadow Nodes ]
  (Pi 3B: Vector DB)             (Pi 3B: Postgres SQL) (Pi 3B #3, #4, #5)
```

---

## 🧮 3. Target IP Mapping Ledger

To maintain organizational clarity during active penetration testing, the network scheme maps to these rigid IP parameters. This scheme is duplicated identically via internal Docker bridges during Phase 1 testing.

| Node Identifier | Hardware Identity | Designated Hostname | IP Assignment | Role / Operational Workspace |
| :--- | :--- | :--- | :--- | :--- |
| **Attack-01** | Gigabyte Laptop | `kali-attacker` | `[NULL - External Host WAN IP]` | Runs automated injection fuzzer & Model frameworks. |
| **Defend-01** | Raspberry Pi 5 | `soc-gateway` | `[NULL - Ingress Boundary IP]` | Reverse proxy firewall running input analysis scripts. |
| **Target-01** | Raspberry Pi 5 | `ai-mcp-gateway` | `[NULL - DMZ Transit IP]` | Hosts frontend Flask logic and standard MCP tools. |
| **Back-01** | Raspberry Pi 3B | `pi3b-vector-db` | `[NULL - Enterprise LAN Dynamic IP]` | Hosts semantic embeddings database (Qdrant). |
| **Back-02** | Raspberry Pi 3B | `pi3b-sql-db` | `[NULL - Enterprise LAN Dynamic IP]` | Shared network directory serving RAG text files. |
| **Back-04** | Raspberry Pi 3B | `pi3b-log-pipe` | `[NULL - Enterprise LAN Dynamic IP]` | Automated backend transaction log ingestion line. |
| **Back-05** | Raspberry Pi 3B | `pi3b-shadow-it` | `[NULL - Enterprise LAN Dynamic IP]` | Unpatched legacy node to simulate pivoting exercises. |

---

## 🔄 4. Threat Model & Data-Flow Scenarios

Documenting how information flows across these network boundaries helps isolate indicators of compromise (IoCs).

### Scenario 1: A Legitimate Application Request
1. **Attack Box** (or normal user) transmits a prompt request over `VLAN 10` to the **Defender Box**.
2. **Defender Box** processes the text payload via an embedded heuristic validation filter. If safe, it forwards the packet to `VLAN 20`.
3. **Target AI Gateway** processes the string, utilizes its local LLM context, and generates an approved API schema.
4. **Target AI Gateway** securely calls out over `VLAN 30` to query data records from the **Pi 3B Relational DB**.
5. The dataset results follow the inverse architecture route safely back to the user.

### Scenario 2: Adversarial Lateral Pivoting Attack
1. **Attack Box** transmits a payload containing a malformed string aimed at triggering Remote Code Execution (RCE) via an unpatched MCP python tool configuration.
2. The payload slips past standard boundary rules because it looks like normal application text.
3. The **Target AI Gateway** executes the unchecked parameter, granting the attacker a low-privilege reverse shell terminal session *inside* the gateway node.
4. The attacker uses this hijacked foothold inside the network to look out across the inner ring (`VLAN 30`), completely bypassing the perimeter firewall.
5. The attacker discovers and exploits `IP Address` (The unpatched **Shadow IT Pi 3B**), compromising deep enterprise network segments.
