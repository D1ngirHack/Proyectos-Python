import vehiculo

class Flota:
    def __init__(self):
        self.vehiculos = []
        
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        
    def mostrar_vehiculos(self):
        for vehiculo in self.vehiculos:
            print(vehiculo)
    
    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()
                return True
        return False
    
    def devolver_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()
                return True
        return False
    
    def __str__ (self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)