# Ethical Network Packet Analyzer

An **ethical, educational, and extensible network packet analyzer** built in Python to understand how data flows across networks at the protocol level.  
This project focuses on **authorized traffic inspection, protocol parsing, and analytical insights**, not exploitation.

---

## 📌 Purpose

This project is designed to:

- Learn how network packets are structured and transmitted
- Parse and analyze common protocols (Ethernet, IP, TCP, UDP, ICMP)
- Perform **defensive traffic analysis** and basic anomaly detection
- Build a clean, modular foundation similar to real-world tools like Wireshark or Zeek

It is intended for **students, cybersecurity learners, and network engineers**.

---

## ⚠️ Legal & Ethical Notice

> **This tool is strictly for educational purposes and authorized network analysis only.**

- Do **NOT** use this tool on networks you do not own or have explicit permission to analyze
- Unauthorized packet sniffing may violate privacy laws and regulations
- The author is **not responsible** for misuse of this software

See `docs/ethics.md` for detailed ethical guidelines.

---

## ✨ Features

- Raw packet capture (platform dependent)
- Modular protocol parsing:
  - Ethernet
  - IPv4
  - TCP
  - UDP
  - ICMP
- Traffic statistics and summaries
- Basic anomaly and pattern detection
- Structured logging
- Offline analysis support (PCAP parsing planned)

---

## 🗂 Project Structure

network-packet-analyzer/
├── src/
│ ├── main.py
│ ├── capture/
│ ├── parsing/
│ ├── analysis/
│ ├── logging/
│ └── utils/
├── docs/
│ ├── ethics.md
│ ├── architecture.md
│ └── protocols.md
├── tests/
├── examples/
├── requirements.txt
├── LICENSE
└── README.md


---

## 🛠 Tech Stack

- **Language:** Python 3.x
- **Core Concepts:**
  - Computer Networks
  - Packet Structures
  - Traffic Analysis
  - Defensive Cybersecurity

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/network-packet-analyzer.git
cd network-packet-analyzer
``` 

```Install dependencies
pip install -r requirements.txt
```

```3️⃣ Run the analyzer
python src/main.py
```

⚠️ Some packet capture features may require administrator/root privileges.

📊 Example Output
[+] Packet Captured
    Source IP: 192.168.1.5
    Destination IP: 142.250.182.14
    Protocol: TCP
    Destination Port: 443

