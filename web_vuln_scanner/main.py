import sys
import time
from colorama import Fore, Style
from core.utils import print_banner, print_scan_summary, handle_interrupt
from core.crawler import crawl
from core.report import save_report

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python main.py <target_url>", Style.RESET_ALL)
        sys.exit(1)

    target_url = sys.argv[1]
    session = __import__('requests').Session()

    visited_links = set()
    forms_found = []
    vulnerabilities = []

    try:
        print_banner()
        print(Fore.CYAN + f"[+] Starting scan on: {target_url}", Style.RESET_ALL)

        start_time = time.time()
        crawl(session, target_url, target_url, visited_links, forms_found, vulnerabilities)
        end_time = time.time()

        elapsed_time = end_time - start_time
        print_scan_summary(elapsed_time, target_url, visited_links, forms_found, vulnerabilities)
        save_report(elapsed_time, target_url, visited_links, forms_found, vulnerabilities)

    except KeyboardInterrupt:
        end_time = time.time()
        elapsed_time = end_time - start_time
        handle_interrupt(elapsed_time, visited_links, forms_found, vulnerabilities, target_url, save_report)
        save_report(elapsed_time, target_url, visited_links, forms_found, vulnerabilities)
        sys.exit(0)

if __name__ == "__main__":
    main()
