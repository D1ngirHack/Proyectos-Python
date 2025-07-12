
class Biblioteca():
    def __init__(self):
        self.libros = {}
        
    def agregar_libro(self, libro):
        if libro.id_libro in self.libros:
            print(f"El libro con ID {libro.id_libro} ya existe")
            return False
        else:
            self.libros[libro.id_libro] = libro
            print(f"[+]El libro {libro.titulo} ha sido agregado\n")
            return True
            
    def prestar_libro(self, id_libro):
        if id_libro in self.libros:
            libro = self.libros[id_libro]
            if libro.disponible:
                libro.disponible = False
                print(f"[+]El libro {libro.titulo} ha sido prestado\n")
                return True
            else:
                print(f"[!]El libro {libro.titulo} no está disponible\n")
                return False
        else:
            print(f"[!]El libro con ID {id_libro} no existe\n")
            return False
     
    def devolver_libro(self, id_libro):
        if id_libro in self.libros:
            libro = self.libros[id_libro]
            if not libro.disponible:
                libro.disponible = True
                print(f"[+]El libro {libro.titulo} ha sido devuelto\n")
                return True
            else:
                print(f"[!]El libro {libro.titulo} no ha sido prestado\n")
                return False
        else:
            print(f"[!]El libro con ID {id_libro} no existe\n")
            return False
            
    @property
    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca\n")
            return
        print("\n--- Todos los libros en la biblioteca general ---")
        for libro in self.libros.values():
            print(libro)
    
    @property
    def libros_disponibles(self):
        disponibles = [libro for libro in self.libros.values() if libro.disponible]
        if not disponibles:
            print("[!]No hay libros disponibles en la biblioteca general.")
            return
        print("\n--- Libros disponibles en la biblioteca general ---")
        for libro in disponibles:
            print(libro)
    
    @property
    def libros_prestados(self):
        prestados = [libro for libro in self.libros.values() if not libro.disponible]
        if not prestados:
            print("[!]No hay libros prestados en la biblioteca general.")
            return
        print("\n--- Libros prestados en la biblioteca general ---")
        for libro in prestados:
            print(libro)
