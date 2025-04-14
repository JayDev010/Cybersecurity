# Azure Honeypot Detection & Visualization Lab

This project walks through setting up a honeypot on Azure, capturing brute-force login attempts, enriching logs with geolocation data, and visualizing attacks using Microsoft Sentinel. It's designed for hands-on practice in security operations, SIEM, and Kusto Query Language (KQL).

## Part 1: Azure Subscription Setup

1. Create a [Free Azure Subscription](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account) or use a paid subscription. If opting for a paid tier, remember to shut down/delete resources when done to avoid charges.

2. Alternatively, use the [Cyber Range](https://skool.com/cyber-range) for a flat fee and get access to:
   - Azure resources
   - Tenable & Defender for Endpoint
   - Guided labs & courses
   - Optional cybersecurity internship

3. Once set up, log in to the [Azure Portal](https://portal.azure.com).

---

## Part 2: Deploying the Honeypot (Windows VM)

1. **Create a Resource Group**  
   - In Azure Portal, search for **"Resource Groups"**.
   - Click **Create** and give it a name (e.g., `Honeypot-RG`).
   - Choose your subscription and preferred region.

2. **Create a Virtual Network (VNet)**  
   - Navigate to **Virtual Networks** and click **Create**.
   - Name your VNet (e.g., `Honeypot-VNet`) and assign it to your new Resource Group.
   - Set address space and create at least one subnet (e.g., `10.0.0.0/24`).

3. **Create a Windows 10 Virtual Machine**  
   - Go to **Virtual Machines** and click **Create**.
   - Choose **Windows 10** as the image.
   - Place the VM in your existing **Resource Group** and **VNet**.
   - Select an appropriate size (smaller sizes may be enforced if you're using the Cyber Range).
   - Set a username and password — keep these safe!

4. **Allow All Inbound Traffic**  
   - After the VM is deployed, go to its **Network Security Group (NSG)**.
   - Add a new inbound rule to **allow all traffic** (for honeypot simulation).

5. **Disable Windows Firewall**  
   - RDP into the VM using the public IP address.
   - Open the firewall settings:

6. Take note of the VM's username and password.
