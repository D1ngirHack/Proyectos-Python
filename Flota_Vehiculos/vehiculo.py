class Vehiculo:
    def __init__(self, marca, modelo, matricula):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.disponible = True
        
    def alquilar(self):
        if self.disponible:
            self.disponible = False
            print(f"\nEl vehículo {self.matricula} ha sido alquilado.")
        else:
            print(f"\nEl vehículo {self.matricula} no está disponible para alquilar.")
                        
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"\nEl vehículo {self.matricula} ha sido devuelto.")
        else:
            print(f"\nEl vehículo {self.matricula} no ha sido alquilado.")
            
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Matrícula: {self.matricula}, Disponible: {self.disponible}"
