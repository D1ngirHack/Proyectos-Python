import socket

ip_objetivo = input("Introduce la IP objetivo: ")
puertos = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 3306, 3389, 5432, 5900, 8080]

socket.setdefaulttimeout(2)

print(f"\n[+] Escaneando... {ip_objetivo}")

for puerto in puertos:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((ip_objetivo, puerto))
    
    
    if resultado == 0:
        print(f"[+] Puerto {puerto} abierto")
    else:
        print(f"[-] Puerto {puerto} cerrado")
        
    sock.close()