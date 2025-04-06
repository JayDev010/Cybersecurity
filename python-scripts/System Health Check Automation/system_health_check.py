import os
import re
import smtplib
import socket
import subprocess
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import psutil
from time import sleep


# Constants for formatting
BOLD = "\033[1m"
NOFORMAT = "\033[0m"
GREENTEXT = "\033[38;5;46m"
YELLOWTEXT = "\033[38;5;11m"
REDTEXT = "\033[38;5;203m"
CYANTEXT = "\033[38;5;14m"

# Log file
LOG_FILE = "/tmp/system_health.log"

# Debug flag
DEBUG = 0

if DEBUG:
    import logging
    logging.basicConfig(level=logging.DEBUG)

# Logging function
def log_message(message: str, level="INFO"):
    levels = {"INFO": GREENTEXT, "ERROR": REDTEXT, "DEBUG": CYANTEXT}
    formatted_message = f"{levels.get(level, GREENTEXT)}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{NOFORMAT} - {message}"
    print(formatted_message)
    with open(LOG_FILE, "a") as log_file:
        log_file.write(formatted_message + "\n")

# Exception handler
def exception_handler(message: str):
    log_message(f"{REDTEXT}ERROR{NOFORMAT}: {message}", level="ERROR")
    input(f"\n{REDTEXT}An error occurred! Press Enter to exit.{NOFORMAT}")
    exit(1)

# System Health Check Menu
def print_main_menu():
    print(f"{BOLD}{YELLOWTEXT}==== SYSTEM HEALTH CHECK MENU ===={NOFORMAT}")
    print("1. Check System Uptime")
    print("2. Monitor Disk Usage")
    print("3. Check Memory Usage")
    print("4. Evaluate CPU Usage")
    print("5. Monitor Network Connectivity")
    print("6. Send Health Report to Email")
    print("7. Exit")
    print(f"{BOLD}{YELLOWTEXT}==============================={NOFORMAT}")

# Check system uptime
def check_uptime():
    log_message(f"{CYANTEXT}Checking system uptime...{NOFORMAT}")
    try:
        uptime_result = subprocess.run(["uptime", "-p"], capture_output=True, text=True)
        print(f"Uptime: {uptime_result.stdout.strip()}")
        log_message(f"System Uptime: {uptime_result.stdout.strip()}", level="INFO")
    except Exception as e:
        exception_handler(f"Failed to check uptime: {e}")

# Monitor disk usage
def check_disk_usage():
    log_message(f"{CYANTEXT}Checking disk usage...{NOFORMAT}")
    try:
        disk_result = subprocess.run(["df", "-h"], capture_output=True, text=True)
        print(disk_result.stdout)
        log_message(f"Disk Usage:\n{disk_result.stdout}", level="INFO")
    except Exception as e:
        exception_handler(f"Failed to check disk usage: {e}")

# Assess memory usage
def check_memory_usage():
    log_message(f"{CYANTEXT}Assessing memory usage...{NOFORMAT}")
    try:
        memory_result = subprocess.run(["free", "-h"], capture_output=True, text=True)
        print(memory_result.stdout)
        log_message(f"Memory Usage:\n{memory_result.stdout}", level="INFO")
    except Exception as e:
        exception_handler(f"Failed to assess memory usage: {e}")

# Evaluate CPU usage
def check_cpu_usage():
    log_message(f"{CYANTEXT}Evaluating CPU usage...{NOFORMAT}")
    try:
        cpu_result = subprocess.run(["top", "-bn1"], capture_output=True, text=True)
        cpu_info = [line for line in cpu_result.stdout.splitlines() if "Cpu(s)" in line]
        load_result = subprocess.run(["uptime"], capture_output=True, text=True).stdout.split("load average: ")[-1].strip()
        
        if cpu_info:
            print(cpu_info[0])
            print(f"Load average: {load_result}")
            log_message(f"CPU Info: {cpu_info[0]}\nLoad Average: {load_result}", level="INFO")
    except Exception as e:
        exception_handler(f"Failed to evaluate CPU usage: {e}")

# Monitor network connectivity
def check_network():
    log_message(f"{CYANTEXT}Checking network connectivity...{NOFORMAT}")
    try:
        socket.create_connection(("www.google.com", 80), timeout=5)
        print(f"{GREENTEXT}Network is up!{NOFORMAT}")
        log_message(f"Network connectivity: Up", level="INFO")
    except socket.error:
        print(f"{REDTEXT}Network is down!{NOFORMAT}")
        log_message(f"Network connectivity: Down", level="ERROR")

# Send health report via email
def send_report(email: str):
    log_message(f"{CYANTEXT}Sending system health report to {NOFORMAT}{email}...")
    if re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
        try:
            with open(LOG_FILE, "r") as file:
                report_content = file.read()

            sender_email = "your_email@gmail.com"
            sender_password = "your_email_password"
            smtp_server = "smtp.gmail.com"
            smtp_port = 587

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email
            msg['Subject'] = "System Health Report"
            msg.attach(MIMEText(report_content, 'plain'))

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, msg.as_string())
            server.quit()
            log_message(f"Report sent successfully to {email}", level="INFO")
            print(f"{GREENTEXT}Health report sent to {email}.{NOFORMAT}")
        except Exception as e:
            exception_handler(f"Failed to send report: {e}")
    else:
        log_message(f"Invalid email address: {email}", level="ERROR")
        print(f"{REDTEXT}Invalid email address!{NOFORMAT}")

# Main driver function
def main():
    while True:
        print_main_menu()
        choice = input(f"{BOLD}{YELLOWTEXT}Choose an option [1-7]: {NOFORMAT}")
        
        if choice == '1':
            check_uptime()
        elif choice == '2':
            check_disk_usage()
        elif choice == '3':
            check_memory_usage()
        elif choice == '4':
            check_cpu_usage()
        elif choice == '5':
            check_network()
        elif choice == '6':
            email = input(f"{YELLOWTEXT}Enter your email address: {NOFORMAT}")
            send_report(email)
        elif choice == '7':
            log_message("Exiting program.")
            print(f"{CYANTEXT}Goodbye!{NOFORMAT}")
            exit(0)
        else:
            print(f"{REDTEXT}Invalid choice! Please try again.{NOFORMAT}")

        # Pause before showing the menu again
        input(f"{CYANTEXT}Press Enter to continue...{NOFORMAT}")

if __name__ == "__main__":
    main()
