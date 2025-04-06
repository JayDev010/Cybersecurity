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

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Health Check Options](#health-check-options)
- [Automating with Cron Jobs](#automating-with-cron-jobs)
- [Automating with systemd (Linux)](#automating-with-systemd-linux)
- [Automating with Windows Task Scheduler](#automating-with-windows-task-scheduler)
- [Troubleshooting](#troubleshooting)
- [Email Setup](#email-setup) (Optional)
- [License](#license)

---

## Overview

The **System Health Check Automation** script is a simple yet powerful tool that allows you to monitor your system's health by checking the following metrics:

- **CPU Usage**: Displays the percentage of CPU usage.
- **Memory Usage**: Displays the percentage of used memory.
- **Disk Usage**: Displays the percentage of used disk space on the system root.
- **Network Connectivity**: Checks if the system has internet access.
- **System Uptime**: Shows the time since the system was last booted.

The script allows you to:
- **Run checks manually** or
- **Schedule automated health checks** using **cron jobs**, **systemd timers**, or **Windows Task Scheduler**.

You can also **send health reports** via email for periodic updates on your system's status.

---

## Installation

To install the System Health Check Automation script, follow these steps:

### 1. Clone the Repository

Clone the repository to your local machine using `git`:

```bash
git clone https://github.com/yourusername/system-health-check.git
cd system-health-check
```

### 2. Ensure Python 3 is Installed

The script requires **Python 3** to run. Check if Python 3 is installed by running:

```bash
python3 --version
```

If Python 3 is not installed, follow the installation instructions for [Python 3](https://www.python.org/downloads/).

### 3. Install Dependencies

This script uses the **psutil** Python library to gather system health data. Install the required dependencies using `pip`:

```bash
pip3 install psutil
```

The `psutil` library handles system statistics such as CPU, memory, and disk usage.

---

## Dependencies

The following dependencies are required to run the script:

- **psutil**: A cross-platform library to retrieve system and process-related information (CPU, memory, disks, and more).
- **smtplib**: A built-in Python library used to send email notifications. 

All dependencies are installed using the `pip3` command, as shown in the installation steps above.

---

## Usage

After installation, you can run the script manually or automate it to run at scheduled intervals.

### Running the Script Manually

To run the script manually, use the following command:

```bash
python3 system_health_check.py
```

Once the script is running, it will check and display your system's health metrics, including CPU, memory, disk usage, and uptime. The script will prompt you with a menu of available options to check various system parameters.

### Health Check Options

When the script runs, you'll be prompted with the following options:

- **Check System Uptime**: Displays how long the system has been running since the last boot.
- **Monitor Disk Usage**: Displays the percentage of disk usage for the system root (`/`).
- **Check Memory Usage**: Displays the percentage of memory in use.
- **Evaluate CPU Usage**: Displays the current CPU load.
- **Monitor Network Connectivity**: Checks if the system has internet access.
- **Send Health Report via Email**: Sends an email with the system health report (requires email setup).
- **Exit**: Exits the script.

---

## Automating with Cron Jobs

On **Linux/macOS**, you can schedule the script to run at regular intervals using **cron jobs**.

### Steps to Set Up a Cron Job

1. **Make the script executable**:

    ```bash
    chmod +x system_health_check.py
    ```

2. **Create a cron job**:

    Open the crontab editor by running:

    ```bash
    crontab -e
    ```

    Add the following line to schedule the script to run every 4 hours:

    ```bash
    0 */4 * * * /usr/bin/python3 /path/to/system_health_check.py >> /path/to/cron_output.log 2>&1
    ```

    This cron job will run the script every 4 hours and log the output to `cron_output.log`.

---

## Automating with systemd (Linux)

If you're using **systemd** on Linux, you can use a systemd timer to schedule the script.

### Steps to Set Up systemd Timer

1. **Create a systemd service**:

    Create a file `/etc/systemd/system/system_health_check.service` with the following content:

    ```ini
    [Unit]
    Description=System Health Check Service

    [Service]
    ExecStart=/usr/bin/python3 /path/to/system_health_check.py
    User=your_user
    WorkingDirectory=/path/to/working_directory

    [Install]
    WantedBy=multi-user.target
    ```

2. **Create the systemd timer**:

    Create a timer file `/etc/systemd/system/system_health_check.timer` with the following content:

    ```ini
    [Unit]
    Description=Runs system health check every 4 hours

    [Timer]
    OnBootSec=10min
    OnUnitActiveSec=4h
    Unit=system_health_check.service

    [Install]
    WantedBy=timers.target
    ```

3. **Enable the timer**:

    Enable and start the timer by running the following commands:

    ```bash
    sudo systemctl enable system_health_check.timer
    sudo systemctl start system_health_check.timer
    ```

---

## Automating with Windows Task Scheduler

For **Windows** users, you can use **Windows Task Scheduler** to run the script at regular intervals.

### Steps to Set Up Windows Task Scheduler

1. Open **Task Scheduler** and click **Create Task**.
2. In the **General** tab, provide a name for the task (e.g., "System Health Check").
3. In the **Triggers** tab, create a trigger to run the script every 4 hours.
4. In the **Actions** tab, select "Start a Program" and browse to your Python executable. In the "Add arguments" box, add the full path to your script (`/path/to/system_health_check.py`).
5. Save the task.

---

## Troubleshooting

- **`psutil` installation errors**: If you're having trouble installing `psutil`, ensure you're using the correct version of `pip` for Python 3 (`pip3`).
- **Email not sending**: If the email functionality is not working, ensure your SMTP settings are correct and that your email provider (e.g., Gmail) allows access to less secure apps.
- **Permission errors**: Ensure you have the necessary permissions to run the script and create cron jobs/systemd timers.

---

## Email Setup

For the **Send Health Report via Email** feature, you need an SMTP server set up. For **Gmail**, follow these steps:

1. Enable **Less Secure Apps** in your Gmail account settings.
2. Use the following sample code for sending email reports (replace placeholders with your credentials):

    ```python
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    def send_email_report(subject, body, to_email):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'your_email@gmail.com'
        sender_password = 'your_email_password'
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, to_email, text)
    ```

---

##
