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

## Estructura del Proyecto

El proyecto se compone de los siguientes módulos principales:

SistemaBibliotecaModular/
├── biblioteca.py
├── biblioteca_infaltil.py
├── libro.py
└── main.py


-   **`libro.py`**: Define la clase `Libro`, que representa un único libro con atributos como ID, título, autor y estado de disponibilidad.
-   **`biblioteca.py`**: Contiene la clase `Biblioteca`, que gestiona la colección general de libros y las operaciones básicas (añadir, prestar, devolver, mostrar).
-   **`biblioteca_infaltil.py`**: Contiene la clase `BibliotecaInfantil`, que hereda de `Biblioteca`. Extiende la funcionalidad para clasificar y gestionar específicamente libros infantiles.
-   **`main.py`**: El script principal que demuestra el uso de las clases `Libro` y `BibliotecaInfantil` a través de varios ejemplos de operaciones.

## Cómo Ejecutar el Proyecto

Para ejecutar este sistema en tu máquina local, sigue estos pasos:

1.  **Clona el repositorio** (si aún no lo has hecho) o navega a la carpeta del proyecto:
    ```bash
    git clone [https://github.com/tu_usuario/MisProyectosPython.git](https://github.com/tu_usuario/MisProyectosPython.git)
    cd MisProyectosPython/SistemaBibliotecaModular
    ```
    (Asegúrate de reemplazar `tu_usuario` con tu nombre de usuario de GitHub).

2.  **Asegúrate de tener Python instalado** (versión 3.x recomendada).

3.  **Ejecuta el script principal**:
    ```bash
    python main.py
    ```

    Verás una serie de impresiones en la consola que demuestran la adición de libros, préstamos, devoluciones y la visualización de diferentes colecciones de libros (general, disponibles, prestados, infantiles).

## Ejemplos de Uso (dentro de `main.py`)

El archivo `main.py` incluye ejemplos de cómo interactuar con las clases:

```python
# Importar clases necesarias
from libro import Libro
from biblioteca_infaltil import BibliotecaInfantil

# Crear una instancia de la biblioteca infantil
biblioteca = BibliotecaInfantil()

# Crear libros
libro1 = Libro(1, "El principito", "Antoine de Saint-Exupéry")
libro2 = Libro(2, "Cien años de soledad", "Gabriel García Márquez")
libro4 = Libro(4, "Aprendiendo a colorear desde cero", "Pepito Manolete")

# Agregar libros (algunos como infantiles)
biblioteca.agregar_libro(libro1, es_para_ninos=True)
biblioteca.agregar_libro(libro2, es_para_ninos=False)
biblioteca.agregar_libro(libro4, es_para_ninos=True)

# Mostrar todos los libros
biblioteca.mostrar_libros

# Prestar un libro
biblioteca.prestar_libro(1)

# Devolver un libro
biblioteca.devolver_libro(1)

# Mostrar libros disponibles
biblioteca.libros_disponibles
