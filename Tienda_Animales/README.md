Sistema de Gestión para una Tienda de Animales 🐾
Descripción del Proyecto
Este proyecto en Python implementa un sistema básico de gestión para una tienda de animales, diseñado para simular las operaciones fundamentales de un negocio de este tipo. Desarrollado con los principios de la Programación Orientada a Objetos (POO), el sistema modela de manera efectiva las entidades Animal y TiendaAnimales, permitiendo un control intuitivo sobre el inventario y el estado de cada animal.

Características Clave:

Registro y Visualización de Animales: Gestiona animales con atributos detallados como nombre, especie, nivel de salud y estado de alimentación.

Interacción con Animales: Permite realizar acciones fundamentales sobre los animales, como alimentarlos para mantener su bienestar y hacerlos jugar, lo que afecta su energía y salud.

Gestión de Inventario: Facilita la adición de nuevos animales al inventario de la tienda y la venta de animales existentes, actualizando automáticamente el stock.

Seguimiento del Negocio: Ofrece un seguimiento básico de la cantidad de animales en tienda y el total de animales vendidos, proporcionando métricas operativas.

Aspectos Destacados para Reclutadores
Este proyecto es una demostración práctica de mis habilidades en:

Diseño y Modelado de Clases: Capacidad para traducir requisitos del mundo real en un diseño de clases coherente y extensible, como se evidencia en las clases Animal y TiendaAnimales.

Programación Orientada a Objetos (POO): Sólida comprensión y aplicación de los pilares de la POO, incluyendo la encapsulación de datos y comportamientos dentro de objetos, y la colaboración efectiva entre diferentes objetos y clases.

Estructura y Modularización del Código: Organización lógica del código en módulos (animal.py, tienda_animales.py, main.py) para mejorar la legibilidad, mantenibilidad y escalabilidad del proyecto.

Lógica de Negocio y Gestión de Estado: Implementación de lógica para gestionar el estado de los animales (alimentado, jugando, salud) y las operaciones de la tienda (agregar/vender animales), reflejando una capacidad para modelar procesos de negocio.

Experiencia Práctica: Un ejemplo concreto de cómo la POO puede ser utilizada para resolver problemas y gestionar información en un contexto de negocios realista, aplicando conceptos teóricos a un escenario práctico.

Estructura del Proyecto
El proyecto se compone de los siguientes archivos Python:

.
├── animal.py
├── tienda_animales.py
└── main.py
animal.py: Define la clase Animal, que encapsula las propiedades (nombre, especie, salud, estado de alimentación, estado de juego) y el comportamiento (alimentar, jugar) de un animal individual.

tienda_animales.py: Define la clase TiendaAnimales, que gestiona la colección de objetos Animal y ofrece funcionalidades a nivel de tienda, como agregar, vender, mostrar, alimentar a todos o hacer jugar a todos los animales.

main.py: El script principal que coordina la creación de la tienda, la adición de animales, y la ejecución de las operaciones de gestión para demostrar la funcionalidad del sistema.

Cómo Ejecutar el Proyecto
Para ejecutar este sistema en tu entorno local, sigue los siguientes pasos:

Clona el repositorio (si está alojado en Git) o descarga los archivos.

Asegúrate de tener Python 3 instalado en tu sistema.

Navega al directorio del proyecto en tu terminal.

Ejecuta el script principal:

Bash

python main.py
