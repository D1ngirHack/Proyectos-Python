# 🔍 Escáner de Puertos TCP en Python

Este proyecto es un **escáner de puertos personalizado** desarrollado en Python utilizando la librería estándar `socket`. Permite identificar qué puertos se encuentran **abiertos o cerrados** en una dirección IP específica, de forma rápida y sencilla.

---

## 🧠 ¿Qué hace este escáner?

Este script realiza un barrido de puertos definidos manualmente (comunes en servicios como FTP, SSH, HTTP, MySQL, etc.) para detectar cuáles están abiertos en un sistema remoto o local. 

Se utiliza el método `connect_ex()` de sockets TCP para verificar la disponibilidad del puerto:

- Si devuelve `0` → El puerto está **abierto**.
- Si devuelve otro valor → El puerto está **cerrado o inaccesible**.

---

## ⚙️ Tecnologías utilizadas

- 🐍 **Python 3.x**
- 🧰 **socket** (librería estándar para comunicación en red)

---

## 📂 Contenido del Script

```python
ip_objetivo = input("Introduce la IP objetivo: ")
puertos = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 3306, 3389, 5432, 5900, 8080]
```
---

## 🚀 Uso del Script
```
$ python main.py
Introduce la IP objetivo: 127.0.0.1

[+] Escaneando... 127.0.0.1
[-] Puerto 21 cerrado
[-] Puerto 22 cerrado
[-] Puerto 80 cerrado
[+] Puerto 445 abierto
...

```

##🛠️ Funcionamiento del script
- Solicita al usuario la IP objetivo.

- Establece un timeout global para evitar esperas largas.

- Recorre los puertos definidos uno por uno.

- Intenta establecer conexión TCP.

- Informa en consola si el puerto está abierto o cerrado.

- Cierra el socket tras cada intento.

## 🛡 Aplicaciones prácticas
- Reconocimiento previo a una intrusión (fase de recon).

- Pruebas internas en entornos de red corporativa.

- Automatización de auditorías de puertos abiertos.

- Entrenamiento de habilidades ofensivas en CTFs o laboratorios.

# 🚨 Advertencia ética
>Estos scripts están diseñados con fines educativos.
>Toda prueba ofensiva debe hacerse en entornos controlados y con permiso explícito.
>El uso indebido de estas herramientas puede ser ilegal.