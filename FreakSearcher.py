"""
FreakSearcher.py - Made by: Celvis - Discord: Celvis
-- Version: 0.0.7
-- https://github.com/Celvis-wq/FreakSearcher
"""

# Import
import os
import requests
import nmap
import subprocess
import traceback

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
    checkRequiredTools()

    domain = input("Welcome to FreakSearcher! | Version: 0.0.7 | Made By: Celvis | Discord: Celvis\n\nPlease enter the domain you wish to scan: ")

    directory = os.path.join(os.getcwd(), "data")
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass

    amassOutput = subprocess.run(["docker", "run", "amass", "enum", "-d", domain], capture_output=True, text=True)
    subdomains = [sd.strip() for sd in amassOutput.stdout.strip().split("\n") if sd.strip()]

    nmScanner = nmap.PortScanner()

    with open(os.path.join(directory, "Port80.txt"), "w") as port80File, open(os.path.join(directory, "Port443.txt"), "w") as port443File:
        for subdomain in subdomains:
            print("Scanning subdomain:", subdomain)

            nmScanner.scan(subdomain, '80,443')

            if subdomain not in nmScanner.all_hosts():
                print(f"Subdomain {subdomain} not found in scan results.")
                continue

            if nmScanner[subdomain].has_tcp(80) and nmScanner[subdomain]['tcp'][80]['state'] == 'open':
                httpStatus = getHttpStatus(subdomain)
                port80File.write(f"{subdomain}: {httpStatus}\n")

            if nmScanner[subdomain].has_tcp(443) and nmScanner[subdomain]['tcp'][443]['state'] == 'open':
                httpStatus = getHttpStatus(subdomain)
                port443File.write(f"{subdomain}: {httpStatus}\n")

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()

