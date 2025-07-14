# PENETRATION-TESTING-TOOLKITS

COMPANY: CODTECH IT SOLUTIONS

NAME: YUSUF IRFAN M

INTERN ID: CT04DH428

DOMAIN: CYBERSECURITY & ETHICAL HACKING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

Project Objective

--> Build a Python-based Penetration Testing Toolkit.

--> Create a web interface (runs in Google Chrome) for easy use.

--> Implement a Port Scanner as the first module.

--> Detect open ports on a given IP address.

--> Output banners (if available) from open ports.

--> Designed for ethical hacking and network auditing.

Tools & Technologies Used:

1. Python 3.10+:

Chosen as the primary language due to its simplicity, rich library ecosystem, and widespread use in cybersecurity.



2. VS Code (Visual Studio Code):

IDE used for developing the toolkit. Its debugger, terminal integration, and extensions made development and testing efficient.



3. Standard Python Libraries:

socket, subprocess, os, sys, argparse, and time were used to build low-level networking tools, automate commands, and handle arguments.



4. Third-party Libraries:

requests and BeautifulSoup: For web-based scanning and parsing.

nmap (optional): For deeper port scanning if installed with python-nmap.

colorama: For colored CLI output for better user readability.

threading: To implement multithreading for speed and parallel execution in scans.



5. Command Line Interface (CLI):

Each module was designed to be executed from the terminal with user input, target IPs, and configurations.


Modules Implemented in the Toolkit:

1. Port Scanner:

Performs scanning of a target IP to identify open ports and services.

Uses socket.connect_ex() to test port connectivity.

Multi-threaded implementation for faster scanning.



2. Brute Force Login Tester:

Designed to test weak credentials on services like SSH, FTP, or web logins.

Reads a list of usernames and passwords from files and attempts logins.

Added delay and logging to mimic real-world scenarios and avoid lockouts.



3. Subdomain Finder:

Takes a base domain and brute-forces subdomains using a dictionary file.

Makes HTTP requests to check if subdomains are live.



4. Whois & DNS Lookup Tool:

Queries domain registration data and DNS records.

Uses socket and APIs (if allowed) to gather information about IPs and domains.



5. IP Geolocation Lookup:

Uses public APIs to find geolocation, ISP, and other metadata for a given IP address.



6. Directory/File Enumerator:

Brute-forces common directories or file names on websites.

Checks for HTTP status codes to determine accessibility (e.g., 200 OK, 403 Forbidden).



7. Email and Phone Number Extractor:

Crawls a web page or text content to extract sensitive data like email addresses and phone numbers using regex.



8. Basic Vulnerability Scanner:

Checks for common vulnerabilities like:

SQL Injection (' OR '1'='1)

Cross-site scripting (XSS) (<script>alert(1)</script>)

Directory Traversal (../../etc/passwd)


Sends payloads through forms or URLs and observes the responses.


Development Process:

1. Requirement Analysis:

Understood what ethical hackers and penetration testers need in real-world tools.

Broke down the task into sub-tools (modules).



2. Modular Architecture:

Designed each tool as a standalone Python file or function.

Ensured code reusability and separation of concerns.



3. Testing on Local Network:

Tested port scanning and brute force modules on localhost and test servers.

Simulated vulnerabilities on mock websites for safe testing.



4. User Interface:

Built a simple CLI menu to select the desired module.

Each module prompts for inputs like IPs, domains, file paths, etc.



5. Error Handling:

Handled exceptions such as network timeouts, permission errors, and file read/write issues gracefully.



6. Documentation & Logging:

Added comments and docstrings to make the code understandable.

Implemented logging in key modules to record attack attempts and results.



Use Cases:

Testing the security posture of internal or client-side systems.

Identifying weak passwords, open ports, and poor configurations.

Simulating real-world attack scenarios in a controlled environment.



Key Learnings:

Understood how real-world cyber-attacks are scripted and detected.

Learned about network protocols, web vulnerabilities, and system architecture.

Improved skills in multithreading, API usage, CLI design, and ethical hacking principles.

Practiced responsible coding and avoided illegal use cases by focusing only on authorized penetration testing.

 
OUTPUT:

"https://github.com/user-attachments/assets/6fbe004b-fa27-4d3f-a160-d5f27c7289b1" />
