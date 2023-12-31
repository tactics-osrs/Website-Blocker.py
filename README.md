# Website Blocker

This Python script allows you to block access to specific websites during certain times of the day. 

## How It Works

1. The script prompts the user to enter the websites they want to block, separated by commas.
2. The user is then asked to specify the time (in 24-hour format) to start and end the website ban.
3. If the current time falls within the start and end times, the script blocks the specified websites by adding entries to the hosts file.
4. If the current time is outside the start and end times, the script unblocks the websites by removing their entries from the hosts file.

## Usage

To use the script, simply run it in a Python environment. You will be prompted to enter the websites to block and the start and end times for the ban.

Run Website Unblocker.py to Unblock all websites effected by website blocker.
To do so open CMD, type python website_unblocker.py, and press enter.

```python
python website_unblocker.py
python website_blocker.py

Requirements
Python 3.x
Administrative privileges for modifying the hosts file
Disclaimer
This script modifies your system’s hosts file.
Always make sure to have a backup of the original file before running the script.
Be careful when editing the hosts file as it could affect your system’s network settings.

Also, remember that using such scripts could be against the terms of service of some websites. Always use such scripts responsibly.
