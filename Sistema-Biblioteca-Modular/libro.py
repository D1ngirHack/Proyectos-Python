
class Libro():
    def __init__(self, id_libro, titulo, autor, disponible = True):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible
        
    def __str__(self):
        return f"ID: {self.id_libro}, Título: {self.titulo}, Autor: {self.autor}, Disponible: {self.disponible}"
    
    def __repr__(self) -> str:
        return self.__str__()