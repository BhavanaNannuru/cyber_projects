# 🕵️ WHOIS Threat Analyzer

A Python-based cybersecurity tool to analyze domain WHOIS data, assess risk, and flag potentially malicious domains based on multiple signals. The tool also includes DNS resolution to fetch the IP address of each domain.

> ⚡️ Designed for cybersecurity learners, CTI analysts, and ethical hackers who want a practical, extensible WHOIS inspection pipeline.

---

## 📌 Features

- ✅ **Single or Bulk Domain Scanning**
- 🧠 **Threat Scoring System** based on:
  - Domain age
  - Short-term registrations
  - Registrar reputation
  - WHOIS privacy/proxy usage
  - High-abuse TLDs
  - Suspicious naming patterns
- 🔍 **Risk Classification**: SAFE, LOW RISK, SUSPICIOUS, MALICIOUS
- 📝 **CSV Export** for CTI use or reporting
- 🎨 **Terminal Colorization** for clarity
- 📦 Modular design following software engineering best practices
- 🖥️ Each domain is resolved to its corresponding IP using DNS lookup.
---

## 🚀 How to Use

### ✅ Requirements

```bash
pip install python-whois
```

### Run the analyzer 
```
python main.py --file domains.txt --output scan_results.csv
```

- `--file`: Input file with domain names *(defaults to `domains.txt`)*
- `--output`: Output CSV file *(defaults to `scan_results.csv`)*

---

## 🛠️ Threat Scoring System

Each domain is scored on a 10-point scale using the following heuristics:

| Heuristic                                      | Points |
|-----------------------------------------------|--------|
| Domain created < 30 days ago                  | +4     |
| Domain expires < 30 days                      | +2     |
| Short registration period (<90 days)          | +2     |
| WHOIS privacy/proxy usage                     | +2     |
| Role-based or generic emails                  | +1     |
| Suspicious or unknown registrar               | +1–2   |
| High-abuse or unknown TLD                     | +1–3   |
| Suspicious name pattern (e.g., abc1234567.xyz)| +1–2   |

---

## 🧠 Risk Mapping

| Score | Risk Level   |
|-------|--------------|
| 0–1   | ✅ SAFE       |
| 2–4   | 🟡 LOW RISK   |
| 5–7   | 🟠 SUSPICIOUS |
| 8–10  | 🔴 MALICIOUS  |

---

## 🧪 Controlled Test Domains

A curated list of ethical, legal test domains to validate scoring logic:

| Domain                              | Description                         |
|-------------------------------------|-------------------------------------|
| github.com, google.com              | Safe, well-known domains            |
| abc1234567.xyz, freedomain.cf       | Suspicious TLDs and naming patterns |
| fake-service-support.live          | Likely phishing setup               |
| info-verification.online           | Likely phishing setup               |
| scanme.org                         | Nmap’s safe test domain             |
| shortreg.top                       | Suspicious lifetime + TLD           |

> ⚠️ Domains like `secure-paypal-login.net` may appear unregistered — used to test robustness.

---

## 🔍 Design Insights & Engineering Decisions

- **Modularization**: Logic split into dedicated files (`scoring.py`, `config.py`, etc.) for clarity.
- **Error Handling**: Gracefully manages WHOIS failures, DNS timeouts, and unregistered domains.
- **Edge Case Coverage**: Sample domains include suspicious patterns, short life spans, and more.
- **Clean Output**: Works well even under rate-limiting or DNS lookup failures.

---

**🎯 Why IP Address Lookup Matters:**
- Adds **network-layer visibility** to domain intelligence.
- Helps detect multiple suspicious domains pointing to the same IP.
- Forms the foundation for:
  - 🌍 GeoIP-based country identification
  - 📶 ASN (Autonomous System) mapping
  - 🔐 IP reputation/blocklist checks

This enhancement boosts the depth of threat intelligence by combining both **domain-level** and **infrastructure-level** context.

---

## 📈 Future Enhancements

- Add support for third-party WHOIS APIs  
- Generate analytics visuals from CSV output  
- Cross-check with reputation APIs (e.g., VirusTotal, AbuseIPDB)

---

## 🧑‍💻 Author Notes

This project is part of a hands-on journey through cybersecurity and Python — evolving from beginner scripts to real-world tooling. Every decision was made to ensure practicality, clarity, and learning value.

> ⚠️ **Disclaimer**: Educational and ethical use only. Always scan domains you own or have permission to analyze.

---
