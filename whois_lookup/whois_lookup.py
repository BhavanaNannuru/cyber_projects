import whois
import socket
from datetime import datetime

def get_whois_data(domain):
    """
    Fetch WHOIS data and normalize fields.
    Handles bad TLDs, timeouts, and unregistered domains gracefully.
    Returns: whois object or None
    """
    try:
        socket.setdefaulttimeout(5)  # Prevent hanging

        data = whois.whois(domain)

        # Some servers return a dict-like response with no actual data
        if not data or not getattr(data, 'domain_name', None):
            print(f"[WARN] No WHOIS record found for {domain} — possibly unregistered.", end="\n\n")
            return None

        # Normalize creation and expiration fields
        if isinstance(data.creation_date, list):
            data.creation_date = min(data.creation_date)
        if isinstance(data.expiration_date, list):
            data.expiration_date = max(data.expiration_date)

        # Normalize email field
        if isinstance(data.emails, list):
            data.emails = list(set(filter(None, data.emails)))

        return data

    except whois.parser.PywhoisError as we:
        print(f"[WARN] WHOIS says domain not found: {domain}", end="\n\n")
    except socket.timeout:
        print(f"[ERROR] Timeout while querying WHOIS for {domain}", end="\n\n")
    except socket.error as se:
        print(f"[ERROR] Socket error for {domain}: {se}", end="\n\n")
    except Exception as e:
        print(f"[ERROR] Failed to fetch WHOIS for {domain}:\n→ {e}", end="\n\n")
    
    return None
