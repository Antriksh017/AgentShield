# 🛡️ AgentShield

> Multi-agent AI framework for automated cyber threat intelligence using local LLMs — no API key required.

Built by **Antriksh Gupta** | [LinkedIn](https://linkedin.com/in/antriksh-gupta-39a69b222) | [TryHackMe](https://tryhackme.com/p/AntrikshGupta) | [GitHub](https://github.com/Antriksh017)

---

## 📌 What is AgentShield?

AgentShield is a cybersecurity automation framework powered by multiple AI agents that collaborate to perform real-world security tasks — fetching live threat intelligence, analyzing vulnerabilities, and generating professional HTML reports automatically.

Originally inspired by [NVISOsecurity/cyber-security-llm-agents](https://github.com/NVISOsecurity/cyber-security-llm-agents), AgentShield is a heavily modified and improved fork that:

- Runs **completely offline** using [Ollama](https://ollama.com) (Qwen3) — no OpenAI API key needed
- Fetches **live CISA KEV data** in real time
- Automatically generates **dark-themed HTML reports** after every scenario
- Uses **Microsoft AutoGen** for multi-agent orchestration

---

## 🧠 How It Works

```
You run:  python run_agents.py <SCENARIO>
                    ↓
    Task Coordinator Agent receives the scenario
                    ↓
         Delegates to specialized agents:
    - text_analyst_agent  → analyzes and summarizes data
    - cmd_exec_agent      → executes system commands
    - internet_agent      → fetches web data
    - caldera_agent       → runs attack simulations
                    ↓
    Agents collaborate and pass results to each other
                    ↓
    HTML report auto-saved to /reports folder
```

---

## ⚡ Key Features

- 🤖 **Multi-Agent Architecture** — agents talk to each other using AutoGen
- 🌐 **Live Threat Intelligence** — fetches real CISA Known Exploited Vulnerabilities
- 📄 **Auto HTML Reports** — professional dark-themed reports saved automatically
- 🔒 **Fully Local** — powered by Ollama Qwen3, no cloud API needed
- 🧩 **Modular Scenarios** — easily add new scenarios in one file

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| Python 3.12 | Core language |
| Microsoft AutoGen 0.2.34 | Multi-agent framework |
| Ollama + Qwen3 | Local LLM (no API key) |
| CISA KEV Feed | Live vulnerability data source |
| HTML/CSS | Report generation |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- [Ollama](https://ollama.com) installed and running
- Qwen3 model pulled: `ollama pull qwen3`

### Setup

```bash
# Clone the repo
git clone https://github.com/Antriksh017/AgentShield.git
cd AgentShield

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Copy env template
cp .env_template .env
```

### Run a Scenario

```bash
python run_agents.py SUMMARIZE_RECENT_CISA_VULNS
```

---

## 📋 Available Scenarios

| Scenario | Description |
|---|---|
| `HELLO_AGENTS` | Basic test to verify setup |
| `SUMMARIZE_RECENT_CISA_VULNS` | Fetch and summarize latest CISA vulnerabilities |
| `DETECT_EDR` | Detect EDR products on a target system |
| `IDENTIFY_EDR_BYPASS_TECHNIQUES` | Find EDR telemetry gaps |
| `TTP_REPORT_TO_TECHNIQUES` | Extract MITRE techniques from threat reports |

---

## 📁 Project Structure

```
AgentShield/
├── actions/          # Scenario definitions
├── agents/           # Agent configurations
├── tools/            # Tool implementations
├── utils/            # Shared utilities + report generator
├── reports/          # Auto-generated HTML reports
├── notebooks/        # Jupyter notebooks for demos
└── run_agents.py     # Main entry point
```

---

## ⚠️ Disclaimer

This tool is intended for **educational and authorized security research purposes only**. Always run in an isolated/virtual environment. The author is not responsible for any misuse.

---

## 📜 License

GPL-3.0

---

<p align="center">Made with 🛡️ by Antriksh Gupta</p>