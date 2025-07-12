# 🐚 Reverse Shell en Python – Conexión TCP entre Atacante y Víctima

Este proyecto demuestra la implementación de una **reverse shell básica en Python**, diseñada para establecer una conexión desde una máquina víctima hacia un servidor atacante. A través de esta conexión, el atacante puede ejecutar comandos en la máquina remota y recibir la salida de los mismos.

---

## 🧠 ¿Qué es una reverse shell?

Una **reverse shell** permite que una máquina (víctima) se conecte a otra (atacante) y le entregue una consola remota. A diferencia de una shell normal (bind shell), en este caso es el cliente quien **inicia la conexión saliente**, lo que ayuda a evadir firewalls o NATs.

Este tipo de técnica es ampliamente usada en:
- Pruebas de penetración
- Simulación de ataques
- Entornos de laboratorio CTF
- Ingeniería inversa y desarrollo de malware ético

---

## 🧱 Estructura del proyecto
```
reverse_shell/
├── cliente.py # Script que se ejecuta en la máquina víctima
├── servidor.py # Script que ejecuta el atacante
└── README.md
```
---

## 🖥️ ¿Cómo funciona?

### 📂 `cliente.py` – Máquina víctima

Este script:
- Se conecta al servidor (atacante) en una IP y puerto específicos.
- Escucha comandos entrantes.
- Ejecuta los comandos recibidos usando `subprocess`.
- Envía la salida de vuelta al atacante.

> 🔒 Debe ser ejecutado por la máquina comprometida o simulada en un entorno controlado.

---

### 🧑‍💻 `servidor.py` – Máquina atacante

Este script:
- Espera una conexión entrante en el puerto 4444.
- Cuando se conecta el cliente, permite enviar comandos en tiempo real.
- Muestra la salida recibida del cliente.
- Finaliza la sesión si se envía el comando `exit`.

> 🧠 Ideal para pruebas locales o en red interna.

---

## 🧪 Ejecución (modo laboratorio)

### 1. Inicia el servidor (atacante):

```bash
$ python servidor.py
[*] Esperando conexión en 127.0.0.1:4444...
[+] Conexión establecida desde ('127.0.0.1', 52238)

Comando >> whoami
victima-user

Comando >> dir
Desktop
Documents
Downloads
client.py

Comando >> exit
[!] Cerrando conexión...
```
### 2. En otra máquina (o terminal), ejecuta el cliente (víctima):
```
$ python cliente.py
[*] Conectado al servidor atacante en 127.0.0.1:4444
[*] Esperando comandos...
```

## 📌 Tecnologías usadas

🐍 Python 3.x

📡 Socket TCP

⚙️ Subprocess para ejecución de comandos

---

# ⚠️ Advertencia ética
🛡 Este proyecto tiene fines exclusivamente educativos y de formación en ciberseguridad ofensiva.

Toda prueba debe realizarse en entornos controlados y con autorización explícita.

El uso indebido de estas técnicas puede ser considerado ilegal y sancionable.
