Password Strength Analyzer

This project is a Python-based tool designed to evaluate and improve password strength by combining several techniques:

Password Strength Analysis: Checks password length, complexity, and common patterns.

zxcvbn Integration: Leverages Dropbox's zxcvbn library to calculate password strength, feedback, and estimated crack times.

Pwned Passwords API: Validates passwords against breached databases.

Features

Validates password complexity (length, case sensitivity, digits, and special characters).

Provides actionable feedback to improve weak passwords.

Checks password breach occurrences using the Pwned Passwords API.

Calculates password strength using zxcvbn, with detailed warnings and suggestions.

Requirements

Python 3.7+

Required Python libraries:

zxcvbn

pwnedpasswords

Install dependencies using pip:

pip install zxcvbn pwnedpasswords

How to Use

Clone this repository:

git clone https://github.com/yourusername/password-strength-analyzer.git

Navigate to the project directory:

cd password-strength-analyzer

Run the script:

python password_analyzer.py

Enter the password when prompted. The script will:

Evaluate password strength.

Provide feedback to improve the password.

Check the password against breached databases.

Example Output

Enter the password:
Password strength: Weak
Suggestions to improve:
- Password should be at least 8 characters long
- Password must contain both Uppercase and Lowercase letters
- Password must contain at least 1 digit
- Password must contain at least 1 special character

Password strength: 0
  - Warning: This is a top-10 common password. Avoid using such passwords.
  - Suggestion: Add another word or two. Uncommon words are better.
Crack time (offline): < 1 second
Crack time (online): < 1 second

This password has been seen 1,234 times in breaches.
Password is too weak.

Code Overview

Key Functions

strength(pwd): Evaluates password length, character diversity, and checks for common patterns.

analyzes_password(password): Uses zxcvbn to compute strength and provide feedback.

analyze_password(password): Checks password against Pwned Passwords API.

re_usage(pwd): Ensures compliance with complexity requirements using regular expressions.

Future Improvements

Implement a GUI for better user interaction.

Add multilingual support for feedback messages.

Include additional password patterns and dictionaries for better analysis.

Contributing

Contributions are welcome! Please follow these steps:

Fork this repository.

Create a new branch:

git checkout -b feature-branch

Commit your changes:

git commit -m "Add new feature"

Push to the branch:

git push origin feature-branch

Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

zxcvbn: Password strength estimator by Dropbox.

Pwned Passwords API: Database of compromised passwords.

Feel free to report issues or suggest features by opening an issue in this repository.

