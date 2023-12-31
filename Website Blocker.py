import os
from datetime import datetime

def validate_input(hour, minute):
    if not 0 <= hour <= 23 or not 0 <= minute <= 59:
        print("Invalid time input. Please enter hour in 24-hour format (0-23) and minute (0-59).")
        return False
    return True

# Ask the user for the websites to block
sites_to_block = input("Enter the websites to block, separated by a comma: ").split(',')

# Ask the user for the time to start the ban
start_hour = int(input("Enter the hour (in 24-hour format) to start the ban: "))
start_minute = int(input("Enter the minute to start the ban: "))

if not validate_input(start_hour, start_minute):
    exit()

# Ask the user for the time to lift the ban
end_hour = int(input("Enter the hour (in 24-hour format) to lift the ban: "))
end_minute = int(input("Enter the minute to lift the ban: "))

if not validate_input(end_hour, end_minute):
    exit()

# Set the start and end time for blocking websites
start_time = datetime.now().replace(hour=start_hour, minute=start_minute)
end_time = datetime.now().replace(hour=end_hour, minute=end_minute)

# Path to the hosts file
if os.name == 'nt':  # If the OS is Windows
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
else:  # For Unix or Linux
    hosts_path = "/etc/hosts"

# IP address to redirect to
redirect = "127.0.0.1"

def block_websites():
    try:
        if start_time <= datetime.now() < end_time:
            print("Block sites")
            with open(hosts_path, 'r+') as hostfile:
                hosts_content = hostfile.read()
                for site in sites_to_block:
                    if site not in hosts_content:
                        hostfile.write(redirect + ' ' + site + '\\n')
        else:
            print('Unblock sites')
            with open(hosts_path, 'r+') as hostfile:
                lines = hostfile.readlines()
                hostfile.seek(0)
                for line in lines:
                    if not any(site in line for site in sites_to_block):
                        hostfile.write(line)
                hostfile.truncate()
    except PermissionError:
        print("Permission denied. Please run this script as an administrator.")
    except IOError as e:
        print(f"An error occurred: {e}")

# Call the function
block_websites()
