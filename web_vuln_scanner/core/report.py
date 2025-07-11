from datetime import datetime
from colorama import Fore

def save_report(elapsed_time, target_url, visited_links, forms_found, vulnerabilities):
    """Save a stylish scan report to scan_report.txt"""
    report_file = "scan_report.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(report_file, "w") as f:
        # Header
        f.write("="*60 + "\n\n")
        f.write("          VulnHound Web Vulnerability Scanner Report\n")
        f.write("="*60 + "\n\n")

        # Metadata
        f.write(f"Scan Time           : {timestamp}\n")
        f.write(f"Target URL          : {target_url}\n")
        f.write(f"Total Runtime       : {elapsed_time:.2f} seconds\n")
        f.write(f"Total Pages Crawled : {len(visited_links)}\n")
        f.write(f"Total Forms Found   : {len(forms_found)}\n")
        f.write("-"*60 + "\n\n")

        # Forms Details
        if forms_found:
            f.write("Forms Discovered:\n")
            f.write("-"*60 + "\n")
            for idx, form in enumerate(forms_found, 1):
                f.write(f"[Form {idx}] URL: {form['url']}\n")
                f.write(f"    Action : {form['action']}\n")
                f.write(f"    Method : {form['method']}\n")
                f.write("    Inputs :\n")
                for input_field in form['inputs']:
                    f.write(f"        - name={input_field['name']}, type={input_field['type']}\n")
                f.write("-"*60 + "\n\n")
        else:
            f.write("No forms discovered during scan.\n")
            f.write("-"*60 + "\n\n")

        # Vulnerabilities Details
        if vulnerabilities:
            f.write("Vulnerabilities Discovered:\n")
            f.write("-"*60 + "\n")
            for idx, vuln in enumerate(vulnerabilities, 1):
                f.write(f"[Vulnerability {idx}]\n")
                f.write(f"    Type : {vuln['type']}\n")
                f.write(f"    URL  : {vuln['url']}\n")
                f.write(f"    Form : Action={vuln['form']['action']}, Method={vuln['form']['method']}\n")
                f.write("-"*60 + "\n\n")
        else:
            f.write("No vulnerabilities discovered during scan.\n")
            f.write("-"*60 + "\n\n")

        # Footer
        f.write("\nEnd of Report\n")
        f.write("="*60 + "\n")

    print(Fore.BLUE + f"\n[✓] Stylish scan report saved to {report_file}")
