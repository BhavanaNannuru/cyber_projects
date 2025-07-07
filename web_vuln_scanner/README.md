# 🕷️ Web Vulnerability Scanner

A Python-based tool to **crawl web applications**, discover links and forms, and prepare for automated security testing. This project focuses on detecting common web vulnerabilities (like XSS and SQL Injection) in future phases.

---

## 🚀 Features (Day 1)
- 🌐 Recursively crawls target websites.
- 🕸️ Extracts and lists all:
  - Hyperlinks (`<a>` tags).
  - Forms with their actions and methods.
- 🛡️ Lays the foundation for OWASP Top 10 vulnerability scanning.

---

## ⚙️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** 
  - [`requests`](https://pypi.org/project/requests/) – For sending HTTP requests.
  - [`BeautifulSoup4`](https://pypi.org/project/beautifulsoup4/) – For HTML parsing.
  - [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html) – For URL joining and validation.

---


## 🤝 Contributions

Contributions are welcome!  
If you have ideas for improvements, new features, or bug fixes:  

- Fork the repository.  
- Create a new branch (`git checkout -b feature/your-feature-name`).  
- Commit your changes (`git commit -m 'Add your feature'`).  
- Push to the branch (`git push origin feature/your-feature-name`).  
- Open a Pull Request.  

For major changes, please open an issue first to discuss what you would like to change.  

---

## 📣 Disclaimer

This tool is intended for **educational purposes** and **authorized security testing only**.  
🚨 **Do not use it on systems or networks without explicit permission** from the owner.  
The author assumes **no responsibility for any misuse or damages** caused by this project.  
