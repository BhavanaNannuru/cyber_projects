# 🔎 Python Port Scanner

A beginner-friendly **Python-based Port Scanner** that scans TCP ports of a target system to identify open ports and running services. This project is built to strengthen foundational knowledge in **network security**, **Python socket programming**, and ethical reconnaissance techniques.

---

## 🧠 Why Build a Port Scanner?

A **port scanner** is a foundational tool in cybersecurity. It scans network ports on a target to discover open services that may be exposed, misconfigured, or vulnerable.

> **Think of it as a flashlight in the dark—it shows you which digital doors are open.**

---

## 🎯 Use Cases

| 🔐 Use Case | 💡 Description |
|------------|----------------|
| **🔍 Reconnaissance** | First step in ethical hacking or red teaming to identify available services. |
| **🛡️ Vulnerability Discovery** | Detect services (e.g., FTP, SSH) with known vulnerabilities (CVEs). |
| **🧱 Firewall Testing** | Check which ports are allowed or blocked by firewall configurations. |
| **📋 Network Inventory** | Inventory of services running on machines within a network. |
| **🧯 Incident Response** | Detect unusual or unauthorized open ports during breach investigations. |
| **🔧 IoT Device Auditing** | Find insecure devices (e.g., printers with open Telnet or HTTP). |
| **🏁 CTFs & Labs** | Starting point in any Capture The Flag or lab-based challenge to identify attack surface. |

---

## 🛠️ Features

- Accepts hostname or IP as input
- Scans well-known ports (1–1024)
- Displays open ports
- Graceful error handling and user interrupts
- Timestamp logging for start and end
- Easy to expand and customize

---

## 💡 How It Works

1. User provides a target IP or domain.
2. The scanner resolves the domain to IP (if needed).
3. It iterates over a port range (default: 1–1024).
4. For each port:
   - Attempts a TCP connection using `socket.connect_ex()`
   - Reports if the port is open
5. Logs scan start and end time
6. Handles keyboard interrupts or connection errors gracefully

---

## 📜 Code Summary (Core Concepts)

- `socket`: Python module to create TCP/IP connections
- `connect_ex()`: Returns 0 if connection to a port is successful
- `settimeout()`: Limits wait time for each port (faster scans)
- `gethostbyname()`: Resolves a domain to an IP address
- `try...except`: Ensures error handling for DNS issues, Ctrl+C, etc.

---

## ✅ Ethical & Safe Targets for Practice

Always **scan only with permission**. 

## 🚀 How to Run

```bash
python3 port_scanner.py
