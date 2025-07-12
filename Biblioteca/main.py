# coding:utf-8

class Libro:
    def __init__(self, id, titulo, autor, genero, disponible=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponible = disponible
        
    def __str__(self):
        return f"{self.id} - {self.titulo} - {self.autor} - {self.genero} - {self.disponible}"

    def __repr__(self) -> str:
        return self.__str__()

class Biblioteca():
   
    def __init__(self):
        self.libros = {}
        
    def agregar_libro(self, libro):
        if libro.id in self.libros:
            print("El libro ya existe\n")
        else:
            self.libros[libro.id] = libro
            print("Libro agregado\n")
            
    def prestar_libro(self, id):
        for libro in self.libros.values():
            if libro.id == id:
                if libro.disponible:
                    libro.disponible = False
                    print("Libro prestado\n")
                else:
                    print(f"El libro {libro.titulo} no está disponible\n")
                break
   
    @property
    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if libro.disponible]

    @property
    def mostrar_libros_prestados(self):
        return [libro for libro in self.libros.values() if not libro.disponible]


class BibliotecaInfantil(Biblioteca):
    
    def __init__(self):
        super().__init__() # Se crea el constructor de la clase padre
        self.libros_ninos = {}
        
    def agregar_libro(self, libro, es_para_ninos): # type: ignore
        super().agregar_libro(libro) # Se ejecuta el método de la clase padre
        self.libros_ninos[libro.id] = es_para_ninos

    def prestar_libro(self, id, es_nino): # type: ignore
        if id in self.libros and self.libros_ninos[id] == es_nino and not self.libros[id].disponible:
            self.libros[id].disponible = False
            print("Libro prestado\n")
        else:
            print("El libro no está disponible para prestar a niños\n")
            
    @property
    def mostrar_estado_libro_para_niños(self):
        return self.libros_ninos


if __name__ == "__main__":
    
    biblioteca = BibliotecaInfantil()
    #biblioteca_infantil = BibliotecaInfantil()
    
    libro1 = Libro(1, "El principito", "Antoine de Saint-Exupéry", "Fantasía")
    libro2 = Libro(2, "Cien años de soledad", "Gabriel García Márquez", "Realismo mágico")
    libro3 = Libro(3, "Aprendiendo Hacking", "Jaime Jonay Yanes García", "Educación")
    libro4 = Libro(4, "Aprendiendo a colorear desde cero", "Pepito Manolete", "Educación")
    libro5 = Libro(5, "La biblia para pequeños", "Jesus Cristopher", "Religión")
 
    biblioteca.agregar_libro(libro1, es_para_ninos=False)
    biblioteca.agregar_libro(libro2, es_para_ninos=False)
    biblioteca.agregar_libro(libro3, es_para_ninos=False)
    biblioteca.agregar_libro(libro4, es_para_ninos=True)
    biblioteca.agregar_libro(libro5, es_para_ninos=True)
    
    biblioteca.mostrar_libros
    
    biblioteca.prestar_libro(1 , es_nino=True)
    biblioteca.prestar_libro(4, es_nino=True)
    biblioteca.prestar_libro(5, es_nino=True)
    
    print(f"Libros prestados: {biblioteca.mostrar_libros_prestados}\n")
    print(f"Libros disponibles: {biblioteca.mostrar_libros}\n")
    print(f"Libros para niños: {biblioteca.mostrar_estado_libro_para_niños}\n")