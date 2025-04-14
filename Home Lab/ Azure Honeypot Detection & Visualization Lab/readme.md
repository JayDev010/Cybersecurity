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

1. In Azure Portal, search for "Virtual Machines" and create a new **Windows 10 VM**.

2. Choose an appropriate size (Cyber Range users may have limited sizes).

3. Take note of the VM's username and password.

4. Navigate to the **Network Security Group** for your VM and allow **all inbound traffic**.

5. Log in to the VM and disable the Windows Firewall:
