# VirusTotal OSINT Threat Intelligence Tool

This Python script interacts with the VirusTotal API to gather threat intelligence information for IP addresses and file hashes (MD5, SHA1, SHA256). It provides a reputation check based on the latest analysis from VirusTotal, including the number of detections (malicious, suspicious, harmless, undetected) and additional metadata, such as WHOIS information for IP addresses.

## Features
IP Reputation Check: Retrieves reputation data for a given IP address, including analysis statistics and WHOIS information.  

File Hash Reputation Check: Fetches reputation data for a given file hash (MD5, SHA1, SHA256), including the analysis statistics and file type description.

### Requirements
- Python 3.x

- requests library (for making HTTP requests to the VirusTotal API)

### **Step 1: Get Your API Key**. 

- Sign up for a free or premium account on VirusTotal and navigate to the API Key section in your VirusTotal account settings to retrieve your personal API key.  

- Replace YOUR_API_KEY_HERE in the script with your actual API key.

### **Step 2: Clone or Download the Repository**. 

- Clone or download the script to your local machine.


### **Step 3: Run the Script**  
Execute the script from the terminal or command prompt:

bash. 
Copy. 
Edit. 
python vt_osint_tool.py. 
When prompted, select either 1 to check the IP reputation or 2 to check the file hash reputation.  


For IP Reputation: Enter a valid IP address (e.g., 8.8.8.8).  

For File Hash Reputation: Enter a valid file hash (MD5, SHA1, or SHA256).  

#### Output 

`=== VirusTotal OSINT Threat Intelligence Tool ===. 
1. Check IP Reputation
2. Check File Hash Reputation
Select an option (1 or 2): 1
Enter the IP address: 8.8.8.8

[+] IP: 8.8.8.8
    Malicious:   0
    Suspicious:  0
    Harmless:    0
    Undetected:  60
    WHOIS Info:  N/A`. 

`File Hash Reputation
mathematica
Copy
Edit
=== VirusTotal OSINT Threat Intelligence Tool ===
1. Check IP Reputation
2. Check File Hash Reputation
Select an option (1 or 2): 2
Enter the file hash (MD5/SHA1/SHA256): b5ba2f87a22dcce1734743e4dca0ecf3d34b23c7

[+] File Hash: b5ba2f87a22dcce1734743e4dca0ecf3d34b23c7
    Type:        N/A
    Malicious:   0
    Suspicious:  0
    Harmless:    0
    Undetected:  1`
 
### **Step 4: Error Handling**.   

- The script includes basic error handling. If there's an issue with the API request (e.g., invalid API key, invalid IP address or file hash), the script will display an error message along with the HTTP status code and reason.

**Common errors include:**  
Error 401: Authentication error (usually due to a missing or invalid API key).  

Error 404: Data not found (the IP address or file hash hasn't been analyzed by VirusTotal).  

## License
This project is open-source and distributed under the MIT License. See the LICENSE file for more details.