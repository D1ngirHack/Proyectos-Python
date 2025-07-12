
class TiendaAnimales():
    def __init__(self,nombre):
        self.nombre = nombre
        self.animales = []
        self.cantidad_animales = 0
        self.cantidad_animales_vendidos = 0
                
    def agregar_animal(self, animal):
        self.animales.append(animal)
        self.cantidad_animales += 1
                
    def vender_animal(self, nombre_animal):
        animal_a_vender = None
        for animal in self.animales: # <-- Iteramos la lista para encontrar el animal
            if animal.nombre == nombre_animal:
                animal_a_vender = animal
                break # Encontramos el animal, salimos del bucle

        if animal_a_vender: # Si encontramos el animal
            self.animales.remove(animal_a_vender)
            self.cantidad_animales_vendidos =+ 1
            self.cantidad_animales -= 1
            print(f"[+] {animal_a_vender.nombre} ha sido vendido.") # Mensaje de confirmación
        else:
            print(f"[!] El animal '{nombre_animal}' no se encuentra en la tienda.")

            
    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)
            
    def mostrar_informacion(self):
        print(f"\n[i]Cantidad de animales en la tienda: ", {self.cantidad_animales})
        print(f"\n[i]Cantidad de animales vendidos: , {self.cantidad_animales_vendidos}")

    def alimentar_animales(self):
        for animal in self.animales:
            animal.alimentar()
            
    def jugar_con_animales(self):
        for animal in self.animales:
            animal.jugar()
            
                
    def __str__(self):
        return "Tienda de animales"
    
    
        
    
    