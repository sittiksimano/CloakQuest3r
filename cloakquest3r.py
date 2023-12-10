import socket
import sys 
import requests
import threading
from ipaddress import ip_address, AddressValueError  
from colorama import init, Fore
import argparse

# Set up argparse for handling command line options
parser = argparse.ArgumentParser(description="Find subdomains and detect if site uses Cloudflare")
parser.add_argument("domain", help="The domain to scan") 
parser.add_argument("-w", "--wordlist", default="subdomains.txt", help="Wordlist of subdomains to check")
parser.add_argument("-o", "--output", help="Save results to output file")
parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads")
  
init()

def check_subdomain(subdomain):
    url = f"https://{subdomain}.{domain}"
    try: 
        resp = requests.head(url, timeout=5) 
        if resp.status_code == 200:
           print(f"[+] Found: {url} ") 
           with results_lock: 
               results.append(subdomain)
    except:
        pass

if __name__ == "__main__": 

    args = parser.parse_args()
    domain = args.domain
    wordlist = args.wordlist 
    output_file = args.output
    num_threads = args.threads
    
    # Input validation
    if not domain:
        print("Error: No domain specified")
        sys.exit(1) 
    
    try:
        ip = socket.gethostbyname(domain) 
    except socket.gaierror:  
        print("Error: Invalid domain name")
        sys.exit(1)

    print(f"Scanning {domain} for subdomains...")  
    
    results = []
    results_lock = threading.Lock()

    # Start threads
    threads = []
    for subdomain in open(wordlist):
        t = threading.Thread(target=check_subdomain,  args=[subdomain.strip()])
        threads.append(t) 
        t.start()

    # Wait for all threads to complete  
    for t in threads:
        t.join()

    # Print summary and save results if output file is set 
    print(f"{len(results)} subdomains found")
    
    if output_file:
        with open(output_file, "w") as f:
            f.write("\n".join(results))
