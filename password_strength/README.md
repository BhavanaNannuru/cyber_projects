# Password Strength Analyzer

This project is a Python-based tool designed to evaluate and improve password strength by combining several techniques:

- **Password Strength Analysis**: Checks password length, complexity, and common patterns.
- **zxcvbn Integration**: Leverages Dropbox's `zxcvbn` library to calculate password strength, feedback, and estimated crack times.
- **Pwned Passwords API**: Validates passwords against breached databases.

---

## **Features**

- Validates password complexity (length, case sensitivity, digits, and special characters).
- Provides actionable feedback to improve weak passwords.
- Checks password breach occurrences using the Pwned Passwords API.
- Calculates password strength using `zxcvbn`, with detailed warnings and suggestions.

---

## **Requirements**

- **Python**: Version 3.7 or higher.
- **Required Python Libraries**:
  - `zxcvbn`
  - `pwnedpasswords`

### Install dependencies using pip:
```bash
pip install zxcvbn pwnedpasswords
```
## **Code Overview**

### **Key Functions**

- **`strength(pwd)`**:  
  Evaluates password length, character diversity, and checks for common patterns.

- **`analyzes_password(password)`**:  
  Uses `zxcvbn` to compute strength and provide feedback.

- **`analyze_password(password)`**:  
  Checks password against the Pwned Passwords API to identify breaches.

- **`re_usage(pwd)`**:  
  Ensures compliance with complexity requirements using regular expressions.

---

## **Future Improvements**

- Implement a GUI for better user interaction.
- Add multilingual support for feedback messages.
- Include additional password patterns and dictionaries for better analysis.

---

## **Acknowledgments**

- **[zxcvbn](https://github.com/dropbox/zxcvbn)**:  
  A password strength estimator developed by Dropbox. It helps compute password strength and provides detailed feedback and crack time estimates.

- **[Pwned Passwords API](https://haveibeenpwned.com/Passwords)**:  
  A database of compromised passwords, helping to identify passwords that have been exposed in data breaches.


