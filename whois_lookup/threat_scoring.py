from datetime import datetime, timezone
import re
from config import reputable_tlds, high_abuse_tlds, shady_registrars, reputable_registrars


def sanitize_datetime(dt):
    if isinstance(dt, list):
        dt = dt[0]

    if dt is None:
        return None

    if isinstance(dt, str):
        try:
            return datetime.fromisoformat(dt.replace("Z", "+00:00")).astimezone(timezone.utc)
        except ValueError:
            return None

    if isinstance(dt, datetime):
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)  # force to UTC
        return dt.astimezone(timezone.utc)

    return None

from datetime import datetime, timezone
import re
from config import reputable_tlds, high_abuse_tlds, shady_registrars, reputable_registrars


def calculate_threat_score(whois_data, domain):
    score = 0
    flags = []
    subrisk = None
    now = datetime.now(timezone.utc)

    creation = sanitize_datetime(whois_data.creation_date)
    expiry = sanitize_datetime(whois_data.expiration_date)

    # --- Age-based analysis ---
    if creation:
        days_old = (now - creation).days
        if days_old < 30:
            score += 4
            flags.append(f"Very new domain ({days_old} days old)")
        elif days_old < 180:
            score += 2
            flags.append(f"Relatively new domain ({days_old} days old)")
    else:
        score += 1
        flags.append("⚠️  Creation date missing")

    if expiry:
        days_left = (expiry - now).days
        if days_left < 30:
            score += 2
            flags.append(f"Domain expiring soon ({days_left} days left)")
    else:
        score += 1
        flags.append("⚠️  Expiration date missing")

    if creation and expiry:
        lifetime = (expiry - creation).days
        if lifetime <= 90:
            score += 2
            flags.append(f"Short registration period ({lifetime} days) — temp domain?")

    # --- WHOIS privacy protection ---
    name = whois_data.name or ""
    if "privacy" in str(name).lower() or "protected" in str(name).lower():
        score += 2
        flags.append("WHOIS privacy protection enabled")

    # --- Email analysis ---
    email = getattr(whois_data, "emails", None)
    if email:
        if isinstance(email, list):
            email = email[0]
        email_lower = email.lower()
        if any(keyword in email_lower for keyword in ["privacy", "whoisguard", "protect", "proxy"]):
            score += 2
            flags.append("Registrant email uses WHOIS proxy")
        elif email_lower.startswith(("admin@", "info@", "support@", "webmaster@")):
            score += 1
            flags.append("Registrant email is a role-based address")

    # --- Registrar reputation check ---
    registrar = whois_data.registrar or "Unknown"
    if registrar.lower() in shady_registrars:
        score += 2
        flags.append(f"Suspicious registrar: {registrar}")
    elif registrar.lower() not in reputable_registrars:
        score += 1
        flags.append(f"Unrecognized registrar: {registrar}")
    if registrar.lower() in {"freenom", "dot tk", "cf registrar"}:
        score += 2
        flags.append(f"Free registrar used: {registrar}")

    # --- TLD analysis ---
    tld = "." + domain.split(".")[-1].lower()
    if tld in high_abuse_tlds:
        score += 3
        flags.append(f"High-abuse TLD: {tld}")
    elif tld not in reputable_tlds:
        score += 1
        flags.append(f"Unrecognized TLD: {tld}")
    if tld in {".xyz", ".top", ".live"}:
        score += 2
        flags.append(f"Abused TLD used: {tld}")

    # --- Domain pattern analysis ---
    domain_base = domain.split(".")[0]
    if re.search(r"[a-z]{5,}[0-9]{3,}", domain_base):
        score += 2
        flags.append("Suspicious alphanumeric domain pattern")
    elif domain_base.count("-") > 2:
        score += 1
        flags.append("Multiple hyphens in domain name")
    if re.search(r"\d{4,}", domain_base):
        score += 2
        flags.append("Numerically padded domain — suspicious")
    if len(domain_base) > 20:
        score += 1
        flags.append("Long domain name — potential obfuscation")
    if re.search(r"[^\x00-\x7F]", domain):
        score += 2
        flags.append("Non-ASCII characters — possible IDN spoofing")

    # --- Subrisk signature logic ---
    if score >= 9:
        subrisk = "Highly suspicious — possible phishing or malware"
    elif 6 <= score < 9:
        subrisk = "Short-lived or anonymized — C2 or disposable infra"
    elif 2 <= score < 6:
        subrisk = "Legit but low-trust"
    elif score == 0:
        subrisk = "Safe / well-established"

    return score, flags, subrisk



def classify_risk(score):
    if score >= 8:
        return "MALICIOUS"
    elif score >= 5:
        return "SUSPICIOUS"
    elif score >= 2:
        return "LOW RISK"
    else:
        return "SAFE"
