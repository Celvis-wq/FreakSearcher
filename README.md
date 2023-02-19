# FreakSearcher.py
# Version: 0.0.4

## Purpose:

- This programs purpose is to scan a domain for subdomains, listing ports ranging from 80 - 443. This tool is for pentesting purposes.
<br />

## FAQ:
- Python3
- Any Linux operating system (Ubuntu, Kali, Parrot, etc)
- Have amass installed to use
- This program is not complete at the moment. I will continue to improve and add more to this program. Please report any issues to me @discord: Celvis#5477

### How to use:
- python3 FreakSearcher.py
- Enter the selected Domain
- Wait for the magic to happen~

# Languages used:
- Python
[<img align="left" alt="Python" width="26px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" style="padding-right:10px;" />]

<br />
<br />

---

### Changelog:
1. Utilizing f-strings for string interpolation instead of concatenation.
2. Added error handling for subprocess calls in case they fail.
3. Use the os.path.join method to join paths instead of hard-coding them.
4. Using a context manager for the subprocess.run calls to avoid having to call stdout.decode().
5. Uses the try-except block to catch any exceptions that might occur while executing the code.
6. Removed the break statement at the end of the for loop because it was useless.
7. Using a list comprehension to simplify the code that writes the subdomain and http status code data to files.

More improvements soon!
