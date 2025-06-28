import socket
import threading
from queue import Queue
from datetime import datetime
import sys

NUM_THREADS = 100  # Number of concurrent threads
PORT_RANGE = (1, 1025)  # Ports to scan

# Thread-safe queue to hold port numbers
port_queue = Queue()


target = input("Enter target IP address or domain: ").strip()

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print(f"[ERROR] Cannot resolve hostname: {target}")
    sys.exit()

print("-" * 60)
print(f"Starting scan on {target_ip}")
print(f"Scan started at: {datetime.now()}")
print("-" * 60)


def scan_port():
    while not port_queue.empty():
        port = port_queue.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.2)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            s.close()
        except Exception:
            pass
        finally:
            port_queue.task_done()



for port in range(PORT_RANGE[0], PORT_RANGE[1]):
    port_queue.put(port)


threads = []

for _ in range(NUM_THREADS):
    t = threading.Thread(target=scan_port)
    t.start()
    threads.append(t)


for t in threads:
    t.join()


print("-" * 60)
print(f"Scan completed at: {datetime.now()}")
print("-" * 60)
