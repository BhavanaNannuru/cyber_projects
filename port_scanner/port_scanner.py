# Port scanners help security professionals discover, verify, and evaluate the attack surface of systems.
import socket
from datetime import datetime
import sys

target = input("Enter target IP address or domain: ").strip()
try:
    target_ip = socket.gethostbyname(target)
except:
    print("Couldnt resolve host name")
    sys.exit()

print("-" * 50)
print(f"Scanning Target: {target_ip}")
print(f"Scan Started at: {datetime.now()}")
print("-" * 50)


try:
    for port in range(1,1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
        
        s.close()

except KeyboardInterrupt:
    print("\n[!] Scan interrupted!")
    sys.exit()

except socket.error as err:
    print("\n[ERROR] Socket error: {err}")
    sys.exit()

print("-" * 50)
print(f"Scan Completed at: {datetime.now()}")
print("-" * 50)
