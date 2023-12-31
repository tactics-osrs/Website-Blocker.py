import os

# Path to the hosts file
if os.name == 'nt':  # If the OS is Windows
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
else:  # For Unix or Linux
    hosts_path = "/etc/hosts"

# IP address to redirect to
redirect = "127.0.0.1"

def unblock_all_websites():
    with open(hosts_path, 'r+') as hostfile:
        lines = hostfile.readlines()
        hostfile.seek(0)
        for line in lines:
            if not line.startswith(redirect):
                hostfile.write(line)
        hostfile.truncate()

# Call the function to unblock all websites
unblock_all_websites()
