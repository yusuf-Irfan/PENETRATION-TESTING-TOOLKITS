import socket

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip, port))
        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner"
        s.close()
        return f"Port {port} is OPEN → {banner}"
    except:
        return None

def start_scan(ip, port_range):
    results = []
    for port in port_range:
        result = scan_port(ip, port)
        if result:
            results.append(result)
    return results
