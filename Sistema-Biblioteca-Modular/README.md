# Sistema de Gestión de Biblioteca Modular en Python 📚

## Descripción del Proyecto

Este proyecto es una implementación modular de un sistema básico de gestión de bibliotecas utilizando el lenguaje de programación Python. Ha sido diseñado con un enfoque en la Programación Orientada a Objetos (POO) y el uso de herencia para gestionar diferentes tipos de colecciones de libros.

El sistema permite realizar operaciones fundamentales como:
- Añadir nuevos libros a la biblioteca.
- Prestar y devolver libros, actualizando su disponibilidad.
- Visualizar todos los libros existentes, así como los disponibles y los prestados.

Una característica clave de este sistema es la inclusión de una **sección especializada para libros infantiles**, que hereda la funcionalidad de la biblioteca general y añade lógica específica para la clasificación y gestión de este tipo de literatura.

Este proyecto es ideal para comprender:
- La creación y gestión de clases y objetos.
- El concepto de herencia y cómo sobreescribir métodos.
- La organización del código en módulos (archivos separados).
- El uso de propiedades (`@property`) para encapsular la lógica de acceso a datos.

-   **`libro.py`**: Define la clase `Libro`, que representa un único libro con atributos como ID, título, autor y estado de disponibilidad.
-   **`biblioteca.py`**: Contiene la clase `Biblioteca`, que gestiona la colección general de libros y las operaciones básicas (añadir, prestar, devolver, mostrar).
-   **`biblioteca_infaltil.py`**: Contiene la clase `BibliotecaInfantil`, que hereda de `Biblioteca`. Extiende la funcionalidad para clasificar y gestionar específicamente libros infantiles.
-   **`main.py`**: El script principal que demuestra el uso de las clases `Libro` y `BibliotecaInfantil` a través de varios ejemplos de operaciones.

🛠️ Estructura del proyecto
```
├── src
    ├── biblioteca.py 
    ├── biblioteca_infantil.py 
    ├── libro.py
    └── main.py # Script de prueba y ejemplo de uso del sistema
```
