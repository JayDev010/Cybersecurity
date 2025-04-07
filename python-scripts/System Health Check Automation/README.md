# System Health Check Automation

This Python-based **System Health Check Automation** script is designed to monitor various aspects of your system's health, including **CPU usage**, **memory usage**, **disk usage**, **network connectivity**, and **system uptime**. It provides a simple and effective way to keep track of your system's health, with the added ability to send email reports and schedule regular checks through cron jobs or systemd timers.

## Features

- **Disk Usage Monitoring**: Check the free space and disk usage across your system to ensure you don't run out of storage.
- **Memory Usage Assessment**: Monitor system memory utilization, helping you detect any potential memory overuse.
- **CPU Usage Evaluation**: Track CPU load and processes to detect any potential performance bottlenecks.
- **Network Connectivity Check**: Verify that your system has active network access and connectivity.
- **System Uptime**: View the system's uptime, which helps you monitor when the system was last restarted.
- **Email Reports**: Automatically send system health reports to your email.
- **Automation**: Schedule automatic health checks using cron jobs or systemd timers for Linux-based systems, or Windows Task Scheduler for Windows users.

---


Thanks, Joan! Using your code and the template structure you provided, here’s a customized `README.md` tailored specifically to your **System Health Check** Python script:

---

```markdown
# 🖥️ System Health Check

## 🔍 Overview

This Python-based **System Health Check** tool provides an interactive menu for monitoring essential aspects of system performance. It checks system uptime, disk space, memory usage, CPU load, and network connectivity, and it can email a detailed health report for further analysis or recordkeeping.

It’s designed for sysadmins, cybersecurity analysts, and IT professionals who want a quick, script-based snapshot of system health — ideal for use on Linux servers or desktops.

### ✨ Features

- **Uptime Check**: See how long the system has been running.
- **Disk Usage Monitoring**: View current disk space statistics.
- **Memory Usage**: Get a breakdown of RAM usage.
- **CPU Load**: Evaluate current CPU usage and load average.
- **Network Connectivity**: Check internet connectivity by attempting to reach Google.
- **Email Reports**: Sends the system health log to any valid email address.
- **Logging**: Outputs all activity to a log file located at `/tmp/system_health.log`.
- **Error Handling**: Handles invalid input and email formats gracefully.
- **Color-Coded Output**: Easy-to-read terminal logs using ANSI color codes.

> 💡 Note: This script does not yet support cron jobs or running services check — features mentioned in the template have been adapted accordingly.

---

## 📁 Files

### `system_health.py`
- Core Python script for executing system health checks.
- Offers an interactive menu to trigger different checks.
- Automatically logs each action and its output.
- Supports sending log results via email (basic SMTP setup required).
- Includes email validation and connection error handling.

---

## ⚙️ How It Works

### 🛠️ Menu Options
Once the script runs, you'll be presented with a menu to choose from:

1. **Check System Uptime**
2. **Monitor Disk Usage**
3. **Check Memory Usage**
4. **Evaluate CPU Usage**
5. **Monitor Network Connectivity**
6. **Send Health Report to Email**
7. **Exit**

Each option runs a command under the hood (`uptime`, `df`, `free`, `top`, etc.) and prints the result to both the screen and the log file.

### 📬 Email Report
- The report is sent from a configured Gmail account.
- You’ll be prompted to enter a recipient email.
- Email validation is enforced before sending.
- Make sure to update credentials inside the script before use.

---

## 🧪 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/system-health-check.git
   cd system-health-check
   ```

2. **Update Email Credentials:**
   Open `system_health.py` and update:
   ```python
   sender_email = "your_email@gmail.com"
   sender_password = "your_email_password"
   ```

3. **Run the script:**
   ```bash
   python3 system_health.py
   ```

---

## 📷 Example Workflow

1. Run the script and pick an option from the menu.
2. Check your system uptime, disk, memory, or CPU stats.
3. Test internet connectivity.
4. Send the report via email using option 6.
5. Exit cleanly from the menu.

> 📩 Don't forget to check your inbox for the system report (make sure SMTP is correctly configured).

---

## ⚠️ Notes

- Email functionality depends on external SMTP server access and correct credentials.
- Logging is enabled by default to `/tmp/system_health.log`.
- Script uses Linux-native commands and may not work on Windows without adaptation.
- No third-party dependencies — runs on standard Python 3 with `psutil` included by default in most Linux distributions.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

```

---

Let me know if you’d like:
- A Bash script added to match the template.
- Cron job functionality implemented.
- Any specific visual enhancements or logging features added.

Ready when you are!
