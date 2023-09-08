# FreakSearcher.py
# Version: 0.0.6

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
<img align="left" alt="Python" width="26px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" style="padding-right:10px;" />

<br />
<br />

---

### Changelog:
1. I have implimented a directory creation fix, many of you may have experienced the error message: An error occurred: makedirs() got an unexpected keyword argument 'existOk'. You shouldn't have this issue now. I had a logic error using the os.makedirs function with an incorrect argument 'existOk=True' which doesn't work, I ended up replacing it with a try-except block to create the directory if it doesn't exist.
2.  I made a more robust error handling using a try-except block to catch and display any exceptions that may occur during the execution of the program.

More improvements soon!
