# FreakSearcher.py
# Version: 0.0.7

## Purpose:

- This programs purpose is to scan a domain for subdomains, listing ports ranging from 80 - 443. This tool is for pentesting purposes.
<br />

## FAQ:
- Python3 - Install Packages: requests, python-nmap. (pip install requests python-nmap)
- Any Linux operating system (Ubuntu, Kali, Parrot, etc)
- Have the following installed: amass, docker, nmap

### How to use:
- python3 FreakSearcher.py
- Enter the selected Domain
- Wait for the magic to happen~

# Languages used:
- Python
<img align="left" alt="Python" width="26px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" style="padding-right:10px;" />

<br />
<br />

---

### Changelog:
1. Updated getHttpStatus function. It now uses the requests library for HTTP status checks with added exception handling.
2. Added checkRequiredTools function to verify the existence of required external tools (docker, nmap) before running the script.
3. Now has Nmap Integration. Replaces subprocess calls with the python-nmap library for scanning ports.
4. Updated the exception handling block to include traceback.print_exc(), which will print the complete traceback when an error occurs. This should help in diagnosing the cause of any exceptions more effectively. Overall, better error handling.
5. Updated welcome message.
6. Fixed minor bugs.
7. Added import traceback.
8. Added filtering empty subdomains. Modified the subdomains list comprehension to filter out empty strings, ensuring only valid subdomains are processed.
9. Added a print statement to show which subdomain is currently being scanned. This just helps in debugging and tracking the script's progress.
10. Added check subdomain in scan results. Before attempting to access scan data, the script now checks if the subdomain is present in nmScanner.all_hosts(). If not, it prints a message and continues to the next subdomain.

Please report any further issues to me immediately! Discord: Celvis

More improvements soon!
