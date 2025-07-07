
import pickle
from .nota import Nota


class GestorNotas:
    def __init__(self, archivo_nota = "notas.pkl"):
        self.archivo_nota = archivo_nota
        
        try:
            with open(self.archivo_nota, "rb") as archivo:
                self.notas = pickle.load(archivo)
        except FileNotFoundError:
            self.notas = []
            
    
    def guardar_notas(self):
        with open(self.archivo_nota, "wb") as archivo:
            pickle.dump(self.notas, archivo)
            
            
    def agregar_nota(self, contenido):
        self.notas.append(Nota(contenido))
        self.guardar_notas()
            
    def leer_todas_las_notas(self):
       return self.notas

    def buscar_nota(self, texto_buscar):
        encontradas = []
        for nota in self.notas:
            if isinstance(nota, Nota):
                if texto_buscar.lower() in nota.contenido.lower():
                    encontradas.append(nota)
            else:
                # Soporte si la nota es un str (por errores previos)
                if texto_buscar.lower() in nota.lower():
                    encontradas.append(nota)
        return encontradas
        
    def eliminar_nota(self, indice):
        if 0 <= indice < len(self.notas):
            del self.notas[indice]
            self.guardar_notas()
            return True
        else:
            return False
            