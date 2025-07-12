from biblioteca import Biblioteca


class BibliotecaInfantil(Biblioteca):
    def __init__(self):
        super().__init__()
        self.libros_ninos = {}
        
    def agregar_libro(self, libro, es_para_ninos = False): # type: ignore -> sobreescribe el método de la clase padre
        
        # 1. Primero, intenta agregar el libro a la colección general de la biblioteca (del padre).
        libro_agregado_general = super().agregar_libro(libro)
        
        # 2. Luego, aplica la lógica específica para clasificar como libro infantil.
        if es_para_ninos:
            if libro_agregado_general or libro.id_libro in self.libros:
                # Si se agregó a la general, o si ya existía en la general,
                # y se marcó como para niños, lo añadimos/confirmamos en libros_ninos.
                if libro.id_libro not in self.libros_ninos:
                    self.libros_ninos[libro.id_libro] = libro
                    print(f"\n[+]Libro '{libro.titulo}' (ID: {libro.id_libro}) ha sido clasificado como infantil.")
                else:
                    print(f"[*]El libro '{libro.titulo}' (ID: {libro.id_libro}) ya estaba clasificado como infantil.")
            else:
                # Esto no debería ocurrir si super().agregar_libro() maneja bien los casos.
                print(f"[!]Error: No se pudo agregar '{libro.titulo}' a la biblioteca general para clasificarlo como infantil.")
        else:
            # Si es_para_ninos es False:
            # Si el libro estaba clasificado como infantil, lo desclasificamos.
            if libro.id_libro in self.libros_ninos:
                del self.libros_ninos[libro.id_libro]
                print(f"[-]El libro '{libro.titulo}' (ID: {libro.id_libro}) ha sido desclasificado como infantil.")
            else:
                # Es un libro no infantil y no estaba clasificado como infantil.
                print(f"[!]El libro '{libro.titulo}' (ID: {libro.id_libro}) no es para niños, solo se agregó a la biblioteca general.\n")
        print()
    
    def prestar_libro(self, id_libro): # type: ignore
        # Verifica si el libro es un libro infantil en esta sección
        if id_libro in self.libros_ninos:
            # Si es un libro infantil, usa el método del padre para cambiar su estado.
            # Esto es seguro porque self.libros_ninos contiene referencias a los mismos objetos Libro
            # que self.libros.
            super().prestar_libro(id_libro) 
        elif id_libro in self.libros: # Si el libro existe en la biblioteca general pero no es infantil
            print(f"[!]El libro '{self.libros[id_libro].titulo}' (ID: {id_libro}) no es un libro infantil en esta sección. No se prestará desde aquí.")
            # Si quisieras que la BibliotecaInfantil también preste libros no infantiles a través de este método,
            # descomenta la siguiente línea:
            # super().prestar_libro(id_libro)
        else:
            print(f"[!]El libro con ID {id_libro} no existe en la biblioteca infantil (ni general).\n")
            
    @property
    def mostrar_libro_ninos(self):
        if not self.libros_ninos:
            print("[!]No hay libros clasificados como infantiles.")
            return
        print("\n--- Libros clasificados como infantiles ---\n")
        for libro in self.libros_ninos.values():
            print(libro)
            
    @property
    def mostrar_libro_ninos_disponibles(self):
        disponibles_ninos = [libro for libro in self.libros_ninos.values() if libro.disponible]
        if not disponibles_ninos:
            print("[!]No hay libros infantiles disponibles.\n")
            return
        print("--- Libros infantiles disponibles ---\n")
        for libro in disponibles_ninos:
            print(libro)
                
    @property
    def mostrar_libros_ninos_prestados(self):
        prestados_ninos = [libro for libro in self.libros_ninos.values() if not libro.disponible]
        if not prestados_ninos:
            print("[!]No hay libros infantiles prestados.\n")
            return
        print("\n--- Libros infantiles prestados ---\n")
        for libro in prestados_ninos:
            print(libro)
        