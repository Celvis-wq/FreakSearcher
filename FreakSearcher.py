"""
FreakSearcher.py - Made by: Celvis#5477
-- Version: 0.0.3
-- https://github.com/Celvis-wq/FreakSearcher
"""

# Import
import os
import subprocess

# Asks for domain name
domain = input("Welcome to FreakSearcher!\nVersion: 0.0.1\nMade By: Celvis#5477\nPlease enter the domain you wish to scan: ")

# Create the directory if it does not exist
if not os.path.exists("/data"):
  os.makedirs("/data")

# Find subdomains with amass
amassOutput = subprocess.run(["docker", "run", "amass", "enum", "-d", domain], capture_output=True)
subdomains = amassOutput.stdout.decode().strip().split("\n")

# Open files to write subdomain and http status code data to
with open("/data/domain_PORT80.txt", "w") as port80file, open("/data/domain_PORT443.txt", "w") as port443file:
  for subdomain in subdomains:
    # Nmap the subdomain for ports 80 and 443
    nmapOutput = subprocess.run(["nmap", "-p", "80,443", subdomain], capture_output=True)
  
    # Check if port 80 is open and write the HTTP status code to the port 80 file
    if "80/tcp open" in nmapOutput.stdout.decode():
      curl_output = subprocess.run(["curl", "-I", subdomain], capture_output=True)
      port80file.write(f"{subdomain}: {curl_output.stdout.decode().split()[1]}\n")
    
    # Check if port 443 is open and write the HTTP status code to the port 443 file
    if "443/tcp open" in nmapOutput.stdout.decode():
      curl_output = subprocess.run(["curl", "-I", subdomain], capture_output=True)
      port443file.write(f"{subdomain}: {curl_output.stdout.decode().split()[1]}\n")
 
    # End
    break
