# 🚗 Sistema de Gestión de Flota de Vehículos en Python

Este proyecto es una demostración clara y concisa de cómo modelar un sistema orientado a objetos para la gestión de una flota de vehículos utilizando Python. Ha sido desarrollado con un enfoque pedagógico y limpio, ideal para mostrar habilidades de programación, lógica y diseño de software.

## 📦 Descripción

El sistema permite:

- 📥 Agregar vehículos a una flota.
- 🚘 Alquilar vehículos disponibles.
- 🔄 Devolver vehículos previamente alquilados.
- 📋 Mostrar el estado actual de la flota.

Todo el comportamiento se gestiona a través de tres clases principales distribuidas en módulos separados:

- `Vehiculo`: Representa un vehículo individual con su estado de disponibilidad.
- `Flota`: Gestiona una colección de vehículos y operaciones de alquiler y devolución.
- `main.py`: Script principal para probar el funcionamiento del sistema.

## 🧠 ¿Por qué es interesante este proyecto?

- **Diseño modular y escalable:** Las clases están claramente separadas, lo que facilita su ampliación.
- **Buenas prácticas de OOP:** Se demuestra encapsulamiento, separación de responsabilidades y reutilización de código.
- **Fácilmente extensible:** Se puede integrar con bases de datos, interfaces gráficas o APIs para evolucionar hacia una aplicación más compleja.
- **Aplicación realista:** Simula un caso de uso habitual en empresas de transporte, logística o alquiler de coches.

## 🛠️ Estructura del repositorio
```
├── flota.py # Clase Flota: gestiona vehículos, alquiler y devolución
├── vehiculo.py # Clase Vehiculo: define atributos y acciones de cada coche
└── main.py # Script de prueba y ejemplo de uso del sistema
```


## ✅ Requisitos

- Python 3.x

No se utilizan dependencias externas, lo que facilita la ejecución inmediata.

## 🚀 Ejecución

```bash
python main.py
