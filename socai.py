import requests
import json

OLLAMA_API = "http://192.168.0.10:11434/api/generate"

def analyze_alert(alert):
    prompt = f"""
You are a SOC analyst AI.

Analyze the following security alert:

Agent: {alert['agent']['name']}
Alert: {alert['rule']['description']}

Return:
1. Severity
2. Attack explanation
3. MITRE ATT&CK mapping
4. Recommended actions
"""

    response = requests.post(
        OLLAMA_API,
        json={
            "model": "llama3.1:8b",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


# Example test alert
if __name__ == "__main__":
    sample_alert = {
        "agent": {"name": "DESKTOP-D30007T"},
        "rule": {
            "description": "Multiple failed login attempts detected"
        }
    }

    result = analyze_alert(sample_alert)
    print("\n--- SOC AI OUTPUT ---\n")
    print(result)
