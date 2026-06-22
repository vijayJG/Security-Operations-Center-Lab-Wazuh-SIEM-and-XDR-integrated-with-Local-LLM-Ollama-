# Security-Operations-Center-Lab-Wazuh-SIEM-and-XDR-integrated-with-Local-LLM-Ollama-
Wazuh SIEM/XDR Home Lab: Ubuntu Manager &amp; Windows Agent . Implements File Integrity Monitoring (FIM) for real-time detection . Integrated Ollama (Llama 3.1:8b) as a local AI assistant for security log analysis and incident response. Demonstrates endpoint monitoring and AI-driven SOC analysis



SOCAI is a local AI-powered SOC (Security Operations Center) assistant that integrates:

Wazuh SIEM (log collection + alerting)
Windows endpoint agent monitoring
Ollama local LLM (Llama 3.1 8B)
Python automation engine
Cross-machine API communication (Ubuntu ↔ Windows)

The system converts raw security alerts into human-readable SOC analyst insights, including:

Severity classification
Attack interpretation
MITRE ATT&CK mapping
Recommended remediation steps


🏗️ Architecture
                     ┌────────────────────────┐
                     │   Windows Host        │
                     │------------------------│
                     │ Ollama LLM Server     │
                     │ llama3.1:8b           │
                     │ Port: 11434           │
                     └─────────┬──────────────┘
                               │ HTTP API
                               │ (LAN Access)
                               ▼
┌────────────────────────────────────────────────────┐
│              Ubuntu 22.04 VM (VirtualBox)         │
│----------------------------------------------------│
│ Wazuh Manager                                      │
│ Wazuh Dashboard                                    │
│ Wazuh API                                          │
│ Python SOC-AI Engine                               │
└────────────────────────────────────────────────────┘
                               ▲
                               │
                     Windows Agent (Endpoint)

                     
⚙️ Tools & Technologies Used


🛡️ Security Stack
Wazuh SIEM (4.x)
Windows Event Logging
File Integrity Monitoring (FIM)
Syscollector & Rootcheck


🤖 AI Stack
Ollama
Llama 3.1 8B (Q4_K_M quantized model)
REST API inference


💻 Infrastructure
Oracle VirtualBox
Ubuntu Server 22.04
Windows 10 Host Machine
NAT + Host-only networking


🐍 Development
Python 3
Requests library
Bash scripting
PowerShell (Windows configuration)


🚀 Features
✔ Real-time Security Monitoring
File integrity detection
Windows event log analysis
Agent-based telemetry
✔ AI SOC Analyst
Converts raw alerts into explanations
Maps attacks to MITRE ATT&CK
Provides remediation steps
✔ Distributed AI Architecture
Windows runs LLM inference
Ubuntu runs SIEM + orchestration
API-based communication



⚙️ Windows Setup Script (PowerShell)
# Allow Ollama access from network
New-NetFirewallRule -DisplayName "SOCAI Ollama Access" `
-Direction Inbound `
-Protocol TCP `
-LocalPort 11434 `
-Action Allow
🐧 Ubuntu Setup Script (Wazuh Agent)
# Install dependencies
sudo apt update

# Install Python dependencies
sudo apt install python3-pip -y
pip install requests

# Check Wazuh agent status
sudo systemctl status wazuh-agent
🧪 API Testing Commands
Windows → Check Ollama
curl http://127.0.0.1:11434/api/tags
Ubuntu → Check LAN access
curl http://192.168.0.10:11434/api/tags
⚠️ Challenges Faced & Solutions
❌ Issue 1: Ollama only accessible via localhost

Problem: API not reachable from Ubuntu VM
Cause: Default binding to 127.0.0.1
Solution: Forced binding using:

OLLAMA_HOST=0.0.0.0:11434
❌ Issue 2: Firewall blocking VM access

Problem: Connection refused from Ubuntu
Solution:

Created inbound firewall rule for port 11434
❌ Issue 3: Ollama auto-restarting in localhost mode

Problem: Process kept reverting to 127.0.0.1
Solution:

Killed background launcher
Disabled auto-start behavior
Manual server control enforced
❌ Issue 4: VirtualBox networking confusion

Problem: Misunderstanding IP ranges
Solution:

Identified correct IP mapping:
Windows: 192.168.0.10
Ubuntu: 192.168.0.11
❌ Issue 5: Python dependency restriction (PEP 668)

Problem: pip install blocked
Solution:

Used system packages or virtual environment


This project demonstrates:

 #SIEM architecture design
 #Endpoint security monitoring
 #LLM integration for cybersecurity
 #REST API engineering
 #Cross-platform networking
 #Incident analysis automation
 #SOC workflow simulation

 Final Statement

This project demonstrates a fully functional AI-assisted Security Operations Center prototype, combining real-world SIEM tools with local LLM inference to simulate intelligent cybersecurity analysis.
