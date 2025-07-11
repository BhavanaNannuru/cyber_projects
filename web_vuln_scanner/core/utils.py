from urllib.parse import urlparse
from colorama import Fore, Style

def print_banner():
    banner = r"""
__     __        _       _   _                       _ 
\ \   / /__ _ _ (_)_ __ | |_| |__   ___  _ __   __ _| |
 \ \ / / _ \ '__| | '_ \| __| '_ \ / _ \| '_ \ / _` | |
  \ V /  __/ |  | | | | | |_| | | | (_) | | | | (_| | |
   \_/ \___|_|  |_|_| |_|\__|_| |_|\___/|_| |_|\__,_|_|
                                                     
            VulnHound Web Vulnerability Scanner
"""
    print(Fore.CYAN + banner)


def is_valid_url(url):
    """Check if the URL is valid (has scheme and netloc)."""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def is_same_domain(base_url, target_url):
    """Ensure the target URL is within the same domain."""
    return urlparse(base_url).netloc == urlparse(target_url).netloc


def print_scan_summary(elapsed_time, target_url, visited_links, forms_found, vulnerabilities):
    print(Fore.MAGENTA + f"\n[✓] Scan completed in {elapsed_time:.2f} seconds.", Style.RESET_ALL)
    print(Fore.MAGENTA + f"[✓] Target: {target_url}", Style.RESET_ALL)
    print(Fore.MAGENTA + f"[✓] Total links crawled: {len(visited_links)}", Style.RESET_ALL)
    print(Fore.MAGENTA + f"[✓] Total forms found: {len(forms_found)}", Style.RESET_ALL)
    print(Fore.MAGENTA + f"[✓] Total vulnerabilities found: {len(vulnerabilities)}", Style.RESET_ALL)


def handle_interrupt(elapsed_time, target_url, visited_links, forms_found, vulnerabilities):
    print(Fore.RED + f"\n[!] Scan interrupted by user after {elapsed_time:.2f} seconds.", Style.RESET_ALL)
    print(Fore.RED + f"[!] Target: {target_url}", Style.RESET_ALL)
    print(Fore.RED + f"[!] Total links crawled before interrupt: {len(visited_links)}", Style.RESET_ALL)
    print(Fore.RED + f"[!] Total forms found before interrupt: {len(forms_found)}", Style.RESET_ALL)
    print(Fore.RED + f"[!] Total vulnerabilities found before interrupt: {len(vulnerabilities)}", Style.RESET_ALL)