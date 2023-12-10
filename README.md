**CloudFlare Subdomain Scanner**
This tool enumerates subdomains and detects if the target domain is behind CloudFlare.


**Features**
Multithreaded subdomain scanning via wordlist
Detection if site uses CloudFlare
Output list of found subdomains
Saves results to optional text file

**Usage**

python cloudflare_subdomain_scanner.py [domain] [options]

**Required:**

domain - The target domain to scan for subdomains

**Options:**

-h, --help - Show help message and exit

-w, --wordlist - Wordlist of subdomains to check (default: subdomains.txt)

-o, --output - Save results to the provided file

-t, --threads - Number of threads to use (default: 10)

**Install Requirements** 

pip install -r requirements.txt

**Example**
Scan example.com with 50 threads using subdomain-list.txt wordlist and output to results.txt:

python cloakquest3r.py example.com -w subdomain-list.txt -t 50 -o results.txt

The tool will output any subdomains found and save them to results.txt.
