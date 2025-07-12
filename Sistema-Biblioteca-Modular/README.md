# 📚 Sistema Modular de Gestión de Biblioteca en Python

Este proyecto es una implementación modular y orientada a objetos de un sistema de gestión de bibliotecas. Diseñado con claridad y buenas prácticas, muestra cómo estructurar código reutilizable en Python utilizando clases, herencia, encapsulamiento y separación por módulos.

## 📦 Descripción

El sistema permite gestionar libros en una biblioteca general y una sección especializada para literatura infantil. Se pueden realizar operaciones como:

- ➕ Agregar nuevos libros.
- 📖 Prestar libros disponibles.
- 🔁 Devolver libros prestados.
- 👀 Visualizar el catálogo completo, los libros disponibles o solo los prestados.

El sistema está diseñado para ser fácilmente extensible y cuenta con una subclase específica (`BibliotecaInfantil`) que hereda de la biblioteca general para añadir lógica adicional centrada en los libros infantiles.

---

## 🧠 ¿Qué demuestra este proyecto?

- ✅ Principios de **Programación Orientada a Objetos (POO)**.
- 🧬 Uso de **herencia** y **sobreescritura de métodos**.
- 📂 **Modularización del código** (cada clase en su propio archivo).
- 🔐 Uso de **propiedades** (`@property`) para proteger y controlar el acceso a atributos.
- 🚀 Un `main.py` que sirve como entorno de prueba con múltiples operaciones simuladas.

---

## 🗂️ Estructura del Proyecto
```
── src/
│ ├── biblioteca.py # Clase Biblioteca general
│ ├── biblioteca_infantil.py # Subclase específica para libros infantiles
│ ├── libro.py # Clase Libro: título, autor, disponibilidad
│ └── main.py # Script principal con casos de uso
```

🏁 Instrucciones de uso
markdown
Copiar
Editar
## 🏁 Instrucciones de uso

### 1. Clonar el repositorio:

```bash
git clone https://github.com/D1ngirHack/Proyectos-Python.git
cd Proyectos-Python/Sistema-Biblioteca-Modular/src
```

## 👨‍💻 Objetivo del proyecto

Este proyecto fue desarrollado como ejercicio práctico para afianzar habilidades fundamentales en desarrollo con Python, especialmente orientado a sistemas reales y escalables. Con él se busca dominar conceptos como:

- 🧱 Diseño modular y limpio del software
- 📦 Organización lógica del código en carpetas y archivos
- 🧬 Uso de clases, herencia y encapsulamiento en POO
- ⚙️ Encapsulación mediante propiedades y métodos
- 📄 Separación de responsabilidades y reutilización del código
- 🧪 Práctica de ejemplos con flujos realistas en consola

Además, el proyecto sirve como base para futuros desarrollos que incluyan almacenamiento en bases de datos, interfaces gráficas o entornos web.


