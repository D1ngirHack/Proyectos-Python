
class Animal():
    
    def __init__(self, nombre, especie, salud):
        self.nombre = nombre
        self.especie = especie
        self.salud = salud
        self.alimentado = False
        self.jugando = False
        
        
    
    def agregar_animal(self, nombre, especie, salud):
        self.nombre = nombre
        self.especie = especie
        self.salud = salud
        self.alimentado = False
        
          
    def alimentar(self):
        if self.alimentado ==False:
            self.alimentado = True
            print(f"\n[+]{self.nombre} ha sido alimentado")
        else:
            print(f"\n[+]{self.nombre} ya ha sido alimentado")


    def jugar(self):
        if self.alimentado == True:
            self.jugando = True
            print(f"\n[+]{self.nombre} está jugando")
            self.salud -= 10
            self.alimentado = False
        else:
            print(f"\n[+]{self.nombre} no puede jugar, necesita alimentarse")
            self.jugando = False
        
        print(f"\n[i]{self.nombre} tiene una salud de {self.salud}, está perdiendo energía necesita alimentarse")
        
    
    def __str__(self):
        return f"\n[i]{self.nombre} es un {self.especie} con una salud de {self.salud} - {'Alimentado' if self.alimentado else 'Hambriento'}"