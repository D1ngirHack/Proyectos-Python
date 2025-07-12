# Sistema de Gestión para una Tienda de Animales 🐾

## Descripción del Proyecto
<<<<<<< HEAD

Este proyecto en Python simula un sistema básico de gestión para una tienda de animales. Utiliza los principios de la Programación Orientada a Objetos (POO) para modelar entidades como `Animal` y `TiendaAnimales`, permitiendo un control fundamental sobre el inventario y el estado de los animales.

Las funcionalidades principales incluyen:
- Registro y visualización de animales con sus atributos (nombre, especie, salud, estado de alimentación).
- Acciones sobre los animales: alimentarlos, hacerlos jugar.
- Gestión de inventario de la tienda: agregar nuevos animales, vender animales existentes.
- Seguimiento básico de la cantidad de animales en tienda y animales vendidos.

Este sistema es un excelente ejemplo para entender:
- El diseño de clases y objetos.
- La encapsulación de datos y comportamiento.
- La interacción entre diferentes objetos y clases en un programa.
- La organización del código en módulos Python.

## Estructura del Proyecto

El proyecto está organizado en una estructura modular para mejorar la claridad y la mantenibilidad del código:

```
tienda_animales/
│
├── tienda.py
├── animal.py
├── main.py
└── README.md
```

=======
Este proyecto en Python implementa un sistema básico de gestión para una tienda de animales, diseñado para simular las operaciones fundamentales de un negocio de este tipo. Desarrollado con los principios de la Programación Orientada a Objetos (POO), el sistema modela de manera efectiva las entidades Animal y TiendaAnimales, permitiendo un control intuitivo sobre el inventario y el estado de cada animal.

## Características Clave:

Registro y Visualización de Animales: Gestiona animales con atributos detallados como nombre, especie, nivel de salud y estado de alimentación.

Interacción con Animales: Permite realizar acciones fundamentales sobre los animales, como alimentarlos para mantener su bienestar y hacerlos jugar, lo que afecta su energía y salud.

Gestión de Inventario: Facilita la adición de nuevos animales al inventario de la tienda y la venta de animales existentes, actualizando automáticamente el stock.

Seguimiento del Negocio: Ofrece un seguimiento básico de la cantidad de animales en tienda y el total de animales vendidos, proporcionando métricas operativas.

# 🐾 Sistema de Gestión para una Tienda de Animales en Python

Este proyecto simula la operativa interna de una tienda de animales, combinando programación orientada a objetos, modularidad y lógica de negocio. Está desarrollado completamente en Python, con una estructura clara y organizada ideal para mostrar buenas prácticas de diseño, encapsulamiento y simulación de procesos reales.

---

## ⚙️ Funcionalidades principales

- ➕ Registrar nuevos animales en la tienda.
- 📋 Visualizar todos los animales disponibles.
- 🍗 Alimentar animales para mejorar su salud.
- 🧸 Jugar con los animales, afectando su estado físico.
- 💰 Vender animales y mantener un registro del inventario.
- 📊 Ver estadísticas como número total de animales vendidos.

---

## 👨‍💻 Objetivo del proyecto

Este proyecto fue desarrollado con fines didácticos y prácticos para reforzar conceptos clave como:

- 📌 Modelado de clases y objetos a partir de problemas reales.
- 🔒 Encapsulamiento de atributos y comportamientos.
- 🧱 Diseño modular, separación por responsabilidades y código reutilizable.
- 🔄 Simulación de lógica de negocio (interacción y gestión de estados).
- 🚀 Desarrollo de software mantenible y escalable.

---

## 🧠 Aspectos técnicos destacados

- ✅ Uso de POO con clases bien definidas.
- 📂 Organización del código en módulos (`animal.py`, `tienda_animales.py`, `main.py`).
- 🔄 Control de estado interno en los objetos (`salud`, `alimentado`, `jugando`).
- ✨ Lógica simple pero adaptable a escenarios más complejos (como BD o interfaz).

---

## 🏁 Instrucciones de uso

### 1. Clonar el repositorio:

```bash
git clone https://github.com/D1ngirHack/Proyectos-Python.git
cd Proyectos-Python/Sistema-Tienda-Animales/src
```
---
## Estructura del Proyecto

```
├──src
    ├── animal.py
    ├── tienda_animales.py
    └── main.py
```

animal.py: Define la clase Animal, que encapsula las propiedades (nombre, especie, salud, estado de alimentación, estado de juego) y el comportamiento (alimentar, jugar) de un animal individual.

tienda_animales.py: Define la clase TiendaAnimales, que gestiona la colección de objetos Animal y ofrece funcionalidades a nivel de tienda, como agregar, vender, mostrar, alimentar a todos o hacer jugar a todos los animales.

main.py: El script principal que coordina la creación de la tienda, la adición de animales, y la ejecución de las operaciones de gestión para demostrar la funcionalidad del sistema.

>>>>>>> 9a34773400580a1968b6e4c9d43851f351d58d74
