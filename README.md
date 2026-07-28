# enterprise-ai-security-lab
An 8 - node physical and virtual enterprise homelab for AI Pentesting, Model Context Protocol (MCP) security, and LLM adversarial engineering.

enterprise-ai-security-lab/
├── .github/workflows/      # Automated security checks (CI/CD)
├── documentation/          # Lab architecture diagrams and attack write-ups
│   └── network-topology.md
├── attack-box/             # Python exploit scripts & Garak configuration
│   ├── prompt-injection/
│   └── mcp-tool-abuse/
├── target-infrastructure/  # Docker setup simulating the target environment
│   ├── docker-compose.yml  # Spins up target LLM, MCP server, and Pi 3B backends
│   ├── mcp-server/         # Vulnerable/hardened MCP server code
│   └── vulnerable-app/     # Frontend chat interface
└── defender-box/           # Llama-Guard / LLM firewall configurations
