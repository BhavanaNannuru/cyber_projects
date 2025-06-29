import sys
import csv
import argparse
from time import sleep
from colorama import init, Fore, Style

from whois_lookup import get_whois_data
from threat_scoring import calculate_threat_score, classify_risk


init(autoreset=True)


def color_risk(risk):
    if "HIGH" in risk.upper() or "MALICIOUS" in risk.upper():
        return Fore.RED + "🔴 " + risk + Style.RESET_ALL
    elif "MEDIUM" in risk.upper() or "SUSPICIOUS" in risk.upper():
        return Fore.YELLOW + "🟠 " + risk + Style.RESET_ALL
    elif "LOW" in risk.upper() or "SAFE" in risk.upper():
        return Fore.GREEN + "🟢 " + risk + Style.RESET_ALL
    return risk


def color_score(score):
    if score >= 8:
        return Fore.RED + str(score)
    elif score >= 5:
        return Fore.YELLOW + str(score)
    else:
        return Fore.GREEN + str(score)


def analyze_domain(domain):
    whois_data = get_whois_data(domain)
    if not whois_data:
        return None

    score, flags, subrisk = calculate_threat_score(whois_data, domain)
    risk = classify_risk(score)

    return {
        "Domain": domain,
        "Registrar": whois_data.registrar or "Unknown",
        "Created": str(whois_data.creation_date),
        "Expires": str(whois_data.expiration_date),
        "Score": score,
        "Risk": risk,
        "Subrisk": subrisk or "",
        "Flags": "; ".join(flags),
        "Country": whois_data.country,
        "Name": whois_data.name
    }


def analyze_single_domain(domain):
    result = analyze_domain(domain)
    if not result:
        return

    print("\n=========== WHOIS THREAT REPORT ===========")
    print(f"🔹 Domain       : {result['Domain']}")
    print(f"🔹 Registrar    : {result['Registrar']}")
    print(f"🔹 Created      : {result['Created']}")
    print(f"🔹 Expires      : {result['Expires']}")
    print(f"🔹 Country      : {result['Country']}")
    print(f"🔹 Name         : {result['Name']}")
    print("\n🚨 Threat Intelligence:")
    print(f"   ➤ Score      : {color_score(result['Score'])}/10")
    print(f"   ➤ Risk Level : {color_risk(result['Risk'])}")
    if result['Subrisk']:
        print(f"   ➤ Signature  : {result['Subrisk']}")
    print("   ➤ Flags:")
    for r in result['Flags'].split("; "):
        print(f"     - {r}")
    print("===========================================\n")


def analyze_bulk(file_path="domains.txt", output_file="scan_results.csv"):
    try:
        with open(file_path, "r") as f:
            domains = [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return

    print(f"\n📁 Loaded {len(domains)} domains from {file_path}\n")
    results = []

    for domain in domains:
        print(f"🔍 Analyzing: {domain}")
        result = analyze_domain(domain)
        if result:
            print(f"    ➤ Risk: {color_risk(result['Risk'])} | Score: {color_score(result['Score'])}/10", end ="\n\n")
            results.append(result)
        sleep(0.3)

    if results:
        save_csv(results, output_file)



def save_csv(results, output_file):
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)
    print(f"\n✅ Results saved to {output_file}")



def parse_args():
    parser = argparse.ArgumentParser(description="🔍 WHOIS Threat Analyzer")

    parser.add_argument("--d", help="Analyze a single domain")
    parser.add_argument("--f", help="Input file for bulk scan (default: domains.txt)")
    parser.add_argument("--o", help="Output CSV file path (default: scan_results.csv)")

    return parser.parse_args()



if __name__ == "__main__":
    args = parse_args()

    if args.d:
        analyze_single_domain(args.d)
    else:
        file_path = args.f if args.f else "domains.txt"
        output_file = args.o if args.o else "scan_results.csv"
        analyze_bulk(file_path, output_file)
