import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import Fore, Style, init

from .utils import is_valid_url, is_same_domain
from .vulnerability import process_forms

# Initialize Colorama
init(autoreset=True)

MAX_LINKS = 100       # Limit total links to crawl
MAX_DEPTH = 10        # Limit crawl depth

def crawl(session, url, base_url, visited_links, forms_found, vulnerabilities, depth=0):
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
        response = session.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and crawl links
        for link_tag in soup.find_all('a'):
            link_href = link_tag.get("href")
            if link_href:
                full_link = urljoin(base_url, link_href)
                if is_valid_url(full_link):
                    print(Fore.GREEN + f"    [Link Found] -> {full_link}", Style.RESET_ALL)
                    crawl(session, full_link, base_url, visited_links, forms_found, vulnerabilities, depth + 1)

        # Extract forms and test for vulnerabilities
        for form in soup.find_all('form'):
            form_action = form.get('action') or "[No Action]"
            form_method = form.get('method', 'GET').upper()
            print(Fore.YELLOW + f"    [Form Found] Action: {form_action}, Method: {form_method}", Style.RESET_ALL)

            inputs = form.find_all('input')
            input_details = [
                {'name': input_tag.get('name') or "[No Name]", 'type': input_tag.get('type', 'text')}
                for input_tag in inputs
            ]

            form_details = {
                'action': form_action,
                'method': form_method,
                'inputs': input_details,
                'url': url
            }
            forms_found.append(form_details)

            # Test form for vulnerabilities
            process_forms(session, form_details, url, vulnerabilities, urljoin)

    except Exception as e:
        print(Fore.RED + f"[-] Error accessing {url}: {e}", Style.RESET_ALL)
