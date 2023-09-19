"""
FreakSearcher.py - Made by: Celvis - Discord: Celvis
-- Version: 0.0.6
-- https://github.com/Celvis-wq/FreakSearcher
"""

# Import
import os
import subprocess

# Fetch the headers of an HTTP response from a given subdomain
def getHttpStatus(subdomain):
    curlOutput = subprocess.run(["curl", "-I", subdomain], captureOutput=True, text=True)
    httpHeaders = curlOutput.stdout.split('\n')
    statusLine = [line for line in httpHeaders if line.startswith("HTTP/")]
    if statusLine:
        return statusLine[0].split()[1]
    return "Unknown"

try:
    # Asks for domain name
    domain = input("Welcome to FreakSearcher!\nVersion: 0.0.5\nMade By: Celvis\nDiscord: Celvis\nPlease enter the domain you wish to scan: ")

    # Create the directory if it does not exist
    directory = os.path.join(os.getcwd(), "data")
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass

    # Find subdomains with amass
    amassOutput = subprocess.run(["docker", "run", "amass", "enum", "-d", domain], capture_output=True, text=True)
    subdomains = amassOutput.stdout.strip().split("\n")

    # Open files to write subdomain and HTTP status code data to
    with open(os.path.join(directory, "Port80.txt"), "w") as port80file, open(os.path.join(directory, "Port443.txt"), "w") as port443file:
        for subdomain in subdomains:
            # Nmap the subdomain for ports 80 and 443
            nmapOutput = subprocess.run(["nmap", "-p", "80,443", subdomain], capture_output=True, text=True)

            nmapOutputStr = nmapOutput.stdout

            # Check if port 80 is open and write the HTTP status code to the port 80 file
            if "80/tcp open" in nmapOutputStr:
                httpStatus = getHttpStatus(subdomain)
                port80file.write(f"{subdomain}: {httpStatus}\n")

            # Check if port 443 is open and write the HTTP status code to the port 443 file
            if "443/tcp open" in nmapOutputStr:
                httpStatus = getHttpStatus(subdomain)
                port443file.write(f"{subdomain}: {httpStatus}\n")

except Exception as e:
    print(f"An error occurred: {e}")
    # TEST
    #print(f"An error occurred: {e}")
    #print(f"An error occurred: {e}")
    #print(f"An error occurred: {e}")
