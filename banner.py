import socket

ip = input("Enter IP address: ")
port = int(input("Enter Port number: "))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((ip, port))
    
    s.send(b"Hello\r\n")
    banner = s.recv(1024)
    
    print("Banner received:")
    print(banner.decode(errors="ignore"))
    
    s.close()

except Exception as e:
    print("Error:", e)
