# PENETRATION-TESTING-TOOLKITS

COMPANY: CODTECH IT SOLUTIONS

NAME: YUSUF IRFAN M

INTERN ID: CT04DH428

DOMAIN: CYBERSECURITY & ETHICAL HACKING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

1. Project Objective

--> Build a Python-based Penetration Testing Toolkit.

--> Create a web interface (runs in Google Chrome) for easy use.

--> Implement a Port Scanner as the first module.

--> Detect open ports on a given IP address.

--> Output banners (if available) from open ports.

--> Designed for ethical hacking and network auditing.

2. Tools & Technologies Used

Python 3.13 → Core programming language for backend logic.

Flask → Lightweight Python web framework to run the app in Chrome.

Socket Module → For TCP port scanning and making raw network connections.

HTML (Jinja Template) → To create the frontend user interface (input form + output display).

Google Chrome → As the browser to run the frontend interface.

Visual Studio Code (VS Code) → Main IDE used to write, run, and manage the project.

Terminal (Command Prompt) → Used to install packages and run the Flask server.

scanme.nmap.org → Safe IP used for penetration testing (offered by Nmap for practice).

Operating System → Windows 10/11 (user tested environment).

3. Modules / Files Included

app.py → Main Flask application that handles routing and user requests.

port_scanner.py → Python file that contains the actual scanning logic using sockets.

index.html → HTML file placed inside templates/ folder for user interface.

modules/ → Directory that stores all scanning logic (modular structure).

templates/ → Folder for storing front-end HTML files required by Flask.

4. How the Tool Works

--> User visits http://127.0.0.1:5000 in Chrome (served by Flask).

--> A form is displayed asking for:

    1. Target IP

    2.Start port

    3.End port


When the user submits the form:

--> Flask receives the input

--> The backend Python script loops through the port range

For each port:

--> Tries to establish a connection

--> If successful → the port is OPEN

--> Tries to retrieve a banner (like Apache, SSH, etc.)

--> The final output is displayed on the webpage in list format.

5. Real-World Use Cases

--> Used by ethical hackers to map out which services are running on a server.

--> Helps in network auditing and cybersecurity assessments.

--> Can identify misconfigured services or unprotected open ports.

--> Useful in penetration testing internships or CTF competitions.

 6. Security Considerations

--> This scanner is safe for use on local or legal IPs.

--> Use only on systems you own or have permission to test.

--> Targeting unauthorized systems can result in legal issues.

 7. Future Scope / Next Modules

--> Multi-threaded scanning for speed

--> Brute force login module (FTP, SSH)

--> Banner grabbing with version fingerprinting

--> Subdomain scanner

--> WHOIS Lookup tool

--> HTML / PDF Report Generator

--> Authentication login page

-->Dark mode web UI

 OUTPUT

"https://github.com/user-attachments/assets/6fbe004b-fa27-4d3f-a160-d5f27c7289b1" />
