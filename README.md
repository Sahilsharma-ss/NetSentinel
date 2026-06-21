# NetSentinel

## Real-Time Network Threat Detection and Analysis Platform

NetSentinel is a cybersecurity-focused network monitoring and intrusion detection platform designed to capture live network traffic, analyze packet behavior, detect suspicious activities, and generate actionable security alerts in real time.

The project aims to simulate core functionalities found in modern Intrusion Detection Systems (IDS) and Security Operations Center (SOC) platforms by combining packet inspection, attack detection, threat scoring, and security analytics into a unified solution.

---

## Features

### Real-Time Packet Monitoring

* Capture live network traffic using Scapy
* Monitor source and destination IPs
* Track ports, protocols, packet sizes, and timestamps

### Threat Detection Engine

Detects multiple attack patterns including:

* Port Scanning
* SSH Brute Force Attempts
* Distributed Denial of Service (DDoS) Activity
* DNS Tunneling
* Beaconing / Command-and-Control Communication
* Suspicious Traffic Patterns

### Alert Management

* Real-time alert generation
* Severity classification
* Alert logging and storage
* Incident tracking

### Threat Intelligence Integration

* AbuseIPDB integration
* AlienVault OTX integration
* Malicious IP reputation checking

### Security Analytics

* Traffic statistics
* Attack timelines
* Threat scoring
* Security event visualization

### Machine Learning Based Detection

* Isolation Forest anomaly detection
* Behavioral analysis
* Detection of previously unseen threats

---

## Project Architecture

## Project Architecture

```text
NetSentinel
│
├── backend
│   │
│   ├── main.py
│   │
│   ├── config
│   │   └── setting.py
│   │
│   ├── capture
│   │   ├── __init__.py
│   │   └── sniffer.py
│   │
│   ├── detector
│   │   ├── __init__.py
│   │   ├── port_scan.py
│   │   ├── brute_force.py
│   │   ├── ddos.py
│   │   ├── dns_tunnel.py
│   │   └── beaconing.py
│   │
│   ├── database
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── packet_store.py
│   │   └── alert_store.py
│   │
│   ├── services
│   │   ├── __init__.py
│   │   ├── alert_manager.py
│   │   ├── threat_score.py
│   │   └── threat_intel.py
│   │
│   ├── models
│   │   ├── __init__.py
│   │   ├── packet.py
│   │   └── alert.py
│   │
│   ├── utils
│   │   ├── logger.py
│   │   ├── helpers.py
│   │   └── time_window.py
│   │
│   └── api
│       ├── __init__.py
│       └── routes.py
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── pcaps
│   ├── attack_samples
│   └── test_traffic
│
├── logs
│   ├── alerts.log
│   └── system.log
│
├── docs
│   ├── architecture.md
│   └── setup.md
│
├── requirements.txt
├── README.md
├── Dockerfile
└── docker-compose.yml
```

## Technology Stack

### Backend

* Python
* FastAPI
* Scapy
* PyShark

### Database

* SQLite
* PostgreSQL

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy

### Frontend

* React
* Chart.js

### Deployment

* Docker
* Linux (Kali/Ubuntu)

---

## Use Cases

* Network Security Monitoring
* Intrusion Detection
* Threat Hunting
* Security Research
* Cybersecurity Education
* Security Operations Center (SOC) Simulation

---

## Example Detection Workflow

1. Attacker performs network reconnaissance.
2. NetSentinel detects abnormal SYN activity.
3. Port Scan Detector triggers an alert.
4. Alert Manager calculates risk score.
5. Event is stored in the database.
6. Dashboard displays the incident.
7. Security analyst investigates the threat.

---

## Future Enhancements

* Automated IP Blocking
* Threat Correlation Engine
* Advanced Behavioral Analytics
* Malware Traffic Detection
* SIEM Integration
* Multi-Host Monitoring
* Real-Time Threat Intelligence Feeds
* AI-Powered Security Recommendations

---

## Disclaimer

NetSentinel is intended for educational, research, and defensive security purposes only. Users are responsible for ensuring compliance with applicable laws, regulations, and organizational policies when monitoring network traffic.
