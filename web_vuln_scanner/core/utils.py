from urllib.parse import urlparse
from colorama import Fore

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
