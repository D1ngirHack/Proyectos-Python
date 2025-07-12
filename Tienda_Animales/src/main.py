from tienda_animales import TiendaAnimales
from animal import Animal


tienda = TiendaAnimales("Tienda de Animales RANDOM")


gato = Animal("Gato", "Persa", 100)
perro = Animal("Perro", "Labrador", 150)
hamster = Animal("Hamster", "Ruso", 50)
conejo = Animal("Conejo", "Angora", 80)
pez = Animal("Pez", "Guppy", 30)
canario = Animal("Canario", "Calopsita", 70)

tienda.agregar_animal(gato)
tienda.agregar_animal(perro)
tienda.agregar_animal(hamster)
tienda.agregar_animal(conejo)
tienda.agregar_animal(pez)
tienda.agregar_animal(canario)

tienda.mostrar_animales()

print("\n-------- Animales Alimentados ---------")
tienda.alimentar_animales()

print("\n-------- Animales Jugando ---------")
tienda.jugar_con_animales()

print("\n-------- Información de Animales ---------")
tienda.mostrar_animales()


print("\n-------- Animales Vendidos ---------")
tienda.vender_animal("Gato")
tienda.vender_animal("Perro")
tienda.vender_animal("Pez")
tienda.vender_animal("Canario")

print("\n-------- Animales Restantes ---------")
tienda.mostrar_animales()


print("\n-------- Animales Alimentados ---------")
tienda.alimentar_animales()

print("\n-------- Animales Jugando ---------")
tienda.jugar_con_animales()

print("\n-------- Información de Animales ---------")
tienda.mostrar_informacion()

print("\n-------- Animales Restantes ---------")
tienda.mostrar_animales()

print("\n-------- Alimentar Animales ---------")
tienda.alimentar_animales()

print("\n-------- Información de Animales ---------")
tienda.mostrar_informacion()

tienda.agregar_animal(Animal("Cocodrilo", "Saltador", 200))
tienda.agregar_animal(Animal("Tigre", "Bengala", 300))

tienda.mostrar_animales()



