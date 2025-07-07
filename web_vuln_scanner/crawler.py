import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys
from colorama import Fore, Style, init
import time

# Initialize Colorama
init(autoreset=True)

visited_links = set()
MAX_LINKS = 100       # Limit total links to crawl
MAX_DEPTH = 10        # Limit crawl depth


def print_banner():
    banner = r"""
__     __        _       _   _                       _ 
\ \   / /__ _ _ (_)_ __ | |_| |__   ___  _ __   __ _| |
 \ \ / / _ \ '__| | '_ \| __| '_ \ / _ \| '_ \ / _` | |
  \ V /  __/ |  | | | | | |_| | | | (_) | | | | (_| | |
   \_/ \___|_|  |_|_| |_|\__|_| |_|\___/|_| |_|\__,_|_|
                                                     
             Web Vulnerability Scanner
"""
    print(Fore.CYAN + banner)


def is_valid_url(url):
    """Check if the URL is valid (has scheme and netloc)."""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def is_same_domain(base_url, target_url):
    """Ensure the target URL is within the same domain as base."""
    return urlparse(base_url).netloc == urlparse(target_url).netloc


def crawl(url, base_url, depth=0):
    """Crawl the given URL to extract links and forms."""
    if url in visited_links:
        return
    if depth > MAX_DEPTH:
        print(Fore.YELLOW + f"[!] Max crawl depth ({MAX_DEPTH}) reached at: {url}", Style.RESET_ALL)
        return
    if len(visited_links) >= MAX_LINKS:
        print(Fore.YELLOW + f"[!] Max link limit ({MAX_LINKS}) reached. Stopping crawl.", Style.RESET_ALL)
        return
    if not is_same_domain(base_url, url):
        return

    print(Fore.CYAN + f"\n[+] Crawling (Depth {depth}): {url}", Style.RESET_ALL)
    visited_links.add(url)

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and print links
        for link_tag in soup.find_all('a'):
            link_text = link_tag.get_text(strip=True)
            link_href = link_tag.get("href")
            if link_href:
                full_link = urljoin(base_url, link_href)
                if is_valid_url(full_link):
                    print(Fore.GREEN + f"    [Link Found] {link_text or '[No Text]'} -> {full_link}", Style.RESET_ALL)
                    crawl(full_link, base_url, depth + 1)

        # Extract and print forms
        forms = soup.find_all('form')
        for form in forms:
            form_action = form.get('action') or "[No Action]"
            form_method = form.get('method', 'GET').upper()
            print(Fore.YELLOW + f"    [Form Found] Action: {form_action}, Method: {form_method}", Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"[-] Error accessing {url}: {e}", Style.RESET_ALL)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python crawler.py <target_url>", Style.RESET_ALL)
        sys.exit(1)

    try:
        print_banner()
        target_url = sys.argv[1]
        print(Fore.CYAN + f"[+] Starting scan on: {target_url}", Style.RESET_ALL)

        start_time = time.time()  # Start timer
        crawl(target_url, target_url)
        end_time = time.time()    # End timer

        elapsed_time = end_time - start_time
        print(Fore.MAGENTA + f"\n[✓] Scan completed in {elapsed_time:.2f} seconds.", Style.RESET_ALL)
        print(Fore.MAGENTA + f"[✓] Total links crawled: {len(visited_links)}", Style.RESET_ALL)

    except KeyboardInterrupt:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(Fore.RED + f"\n[!] Scan interrupted by user after {elapsed_time:.2f} seconds.", Style.RESET_ALL)
        print(Fore.RED + f"[!] Total links crawled before interrupt: {len(visited_links)}", Style.RESET_ALL)
        sys.exit(0)
