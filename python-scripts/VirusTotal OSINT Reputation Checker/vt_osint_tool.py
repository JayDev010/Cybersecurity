import requests 
import sys

API_KEY = ''  # Replace with your actual VirusTotal API key
BASE_URL = 'https://www.virustotal.com/api/v3/'

headers = {
    "x-apikey": API_KEY
}

def get_ip_reputation(ip):
    url = BASE_URL + f"ip_addresses/{ip}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        whois = data["data"]["attributes"].get("whois", "N/A")
        print(f"\n[+] IP: {ip}")
        print(f"    Malicious:   {stats['malicious']}")
        print(f"    Suspicious:  {stats['suspicious']}")
        print(f"    Harmless:    {stats['harmless']}")
        print(f"    Undetected:  {stats['undetected']}")
        print(f"    WHOIS Info:  {whois[:300]}{'...' if len(whois) > 300 else ''}")
    else:
        print(f"\n[!] Error {response.status_code}: Unable to retrieve data for IP {ip}")
        print("    Reason:", response.text)

def get_hash_reputation(file_hash):
    url = BASE_URL + f"files/{file_hash}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        file_type = data["data"]["attributes"].get("type_description", "N/A")
        print(f"\n[+] File Hash: {file_hash}")
        print(f"    Type:        {file_type}")
        print(f"    Malicious:   {stats['malicious']}")
        print(f"    Suspicious:  {stats['suspicious']}")
        print(f"    Harmless:    {stats['harmless']}")
        print(f"    Undetected:  {stats['undetected']}")
    else:
        print(f"\n[!] Error {response.status_code}: Unable to retrieve data for hash {file_hash}")
        print("    Reason:", response.text)

def main():
    print("=== VirusTotal OSINT Threat Intelligence Tool ===")
    print("1. Check IP Reputation")
    print("2. Check File Hash Reputation")
    choice = input("Select an option (1 or 2): ")

    if choice == '1':
        ip = input("Enter the IP address: ")
        get_ip_reputation(ip)
    elif choice == '2':
        file_hash = input("Enter the file hash (MD5/SHA1/SHA256): ")
        get_hash_reputation(file_hash)
    else:
        print("Invalid selection. Please choose 1 or 2.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Exiting on user interrupt.")
        sys.exit(0)
    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")
