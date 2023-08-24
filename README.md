# FreakSearcher.py
# Version: 0.0.5

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
1. I added a new function called getHttpStatus() to extract the HTTP status code from the headers obtained using curl. This function handles parsing the status code and returning "Unknown" if the status line is not found.
2. text=True in subprocess calls, this ensures that the output of subprocess commands is returned as text (strings) directly, which eliminates the need to manually decode the bytes to strings.
3. Improved HTTP status code retrieval. The HTTP status code is now extracted using the getHttpStatus() function. Improves both code readability and reduces repetition.
4. In nmapOutputStr I assigned the nmapOutput.stdout to a variable for easier referencing, improving code readability.

More improvements soon!
