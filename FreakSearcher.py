"""
FreakSearcher.py - Made by: Celvis#5477
-- Version: 0.0.1
-- https://github.com/Celvis-wq/FreakSearcher

TODO:
-- Finish this program overall
"""

# Import
import subprocess

# Asks for domain name
print("Welcome to FreakSearcher!\nVersion: 0.0.1\nMade By: Celvis#5477\n")
domain = input("\nPlease enter the domain you wish to scan: ")

# Find subdomains with amass
amassOutput = subprocess.run(["docker", "run", "amass", "enum", "-d", domain], capture_output=True)
subdomains = amassOutput.stdout.decode().strip().split("\n")

# Nmap each subdomain for ports 80 and 443
for subdomain in subdomains:
  nmapOutput = subprocess.run(["nmap", "-p", "80,443", subdomain], capture_output=True)
  
  # Check if ports 80 and 443 are open
  if "80/tcp open" in nmapOutput.stdout.decode() and "443/tcp open" in nmapOutput.stdout.decode():
    # Curl the subdomain and print the HTTP status code
    curl_output = subprocess.run(["curl", "-I", subdomain], capture_output=True)
    print(f"{subdomain}: {curl_output.stdout.decode().split()[1]}")
    
# To be completed
