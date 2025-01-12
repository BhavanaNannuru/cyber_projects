import re
import string
import getpass
from zxcvbn import zxcvbn
from pwnedpasswords import check


def analyze_password(password):
    # Check with zxcvbn
    zxcvbn_result = zxcvbn(password)
    print("zxcvbn Score:", zxcvbn_result['score'])

    # Check against breached databases
    pwned_count = check(password)
    # print(pwned_count)
    if pwned_count > 0:
        print(f"This password has been seen {pwned_count} times in breaches.")



#builtin library developed by dropbox
# Score: 0 (weak) to 4 (strong)
#incase user inputs are available, they can be passed too. 
def analyzes_password(password):
    result = zxcvbn(password)
    print("Password strength:", result['score'])  
    if result['feedback']['warning']:
        print(f"  - Warning: {result['feedback']['warning']}")
    for suggestion in result['feedback']['suggestions']:
        print(f"  - Suggestion: {suggestion}")
    print(f"Crack time (offline): {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
    print(f"Crack time (online): {result['crack_times_display']['online_no_throttling_10_per_second']}")


def re_usage(pwd):
    if re.search(r"[A-Z]", pwd) and re.search(r"\d", pwd) and re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        print("Password meets complexity requirements.")
    else:
        print("Password is too weak.")




def strength(pwd):
    str = 0
    feedback = []

    #check for min length
    if len(pwd)>=8:
        str+=1
    else:
        feedback.append("Password should be at least 8 characters long")

    
    #check for uppercase and lowercase letters
    if any(c.islower() for c in pwd) and any(c.isupper() for c in pwd):
        str+=1
    else:
        feedback.append("Password must contain both Uppercase and Lowercase letters")

    
    #check for digits
    if any(c.isdigit() for c in pwd):
        str+=1
    else:
        feedback.append("Password must contain at least 1 digit")


    #check for special characters
    if any(c in string.punctuation for c in pwd):
        str+=1
    else:
        feedback.append("Password must contain at least 1 special character")

    
    #check for common patterns
    c_patterns = ["hello","123","asdf"]
    if any(pattern in pwd.lower() for pattern in c_patterns):
        feedback.append("Password is too common")
    else:
        str+=1
    

    return str, feedback

pwd = getpass.getpass("Enter the password:")
str, feedback = strength(pwd)
if str < 3:
    print("Password strength: Weak")
elif str == 3 or str == 4:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")

if feedback:
    print("Suggestions to improve:")
    for suggestion in feedback:
        print(f"- {suggestion}")

print(analyzes_password(pwd))
print("\n\n\n\n")
re_usage(pwd)
print("\n\n\n\n")
analyze_password(pwd)