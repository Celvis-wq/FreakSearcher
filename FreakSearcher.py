"""
FreakSearcher.py - Made by: Celvis - Discord: Celvis
-- Version: 0.0.7
-- https://github.com/Celvis-wq/FreakSearcher

-- bug fixes soon
"""

# Import
import os
import requests
import subprocess

# Function to fetch the headers of an HTTP response from a given subdomain
def getHttpStatus(subdomain):
    try:
        response = requests.head("http://" + subdomain, timeout=5)
        return str(response.status_code)
    except requests.RequestException:
        return "Unknown"

# Function to check for the existence of required tools
def checkRequiredTools():
    requiredTools = ["docker", "nmap"]
    missingTools = []
    for tool in requiredTools:
        if subprocess.call(["which", tool], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
            missingTools.append(tool)
    if missingTools:
        print("Missing required tools:", ", ".join(missingTools))
        print("Please install them before running the script.")
        exit(1)

try:
    # Check for required tools
    checkRequiredTools()

    # Asks for domain name
    domain = input("Welcome to FreakSearcher!\nVersion: 0.0.7\nMade By: Celvis\nDiscord: Celvis\nPlease enter the domain you wish to scan: ")

    # Create the directory if it does not exist
    directory = os.path.join(os.getcwd(), "data")
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass

    # Find subdomains with amass
    amassOutput = subprocess.run(["docker", "run", "amass", "enum", "-d", domain], capture_output=True, text=True)
    subdomains = amassOutput.stdout.strip().split("\n")

    # Initialize Nmap Scanner
    nmScanner = nmap.PortScanner()

    # Open files to write subdomain and HTTP status code data to
    with open(os.path.join(directory, "Port80.txt"), "w") as port80File, open(os.path.join(directory, "Port443.txt"), "w") as port443File:
        for subdomain in subdomains:
            # Nmap the subdomain for ports 80 and 443
            nmScanner.scan(subdomain, '80,443')

            # Check if port 80 is open and write the HTTP status code to the port 80 file
            if nmScanner[subdomain].has_tcp(80) and nmScanner[subdomain]['tcp'][80]['state'] == 'open':
                httpStatus = getHttpStatus(subdomain)
                port80File.write(f"{subdomain}: {httpStatus}\n")

            # Check if port 443 is open and write the HTTP status code to the port 443 file
            if nmScanner[subdomain].has_tcp(443) and nmScanner[subdomain]['tcp'][443]['state'] == 'open':
                httpStatus = getHttpStatus(subdomain)
                port443File.write(f"{subdomain}: {httpStatus}\n")

except Exception as e:
    print(f"An error occurred: {e}")
