import vehiculo
from flota import Flota


if __name__ == '__main__':
   
   flota = Flota() 

   flota.agregar_vehiculo(vehiculo.Vehiculo('Seat', 'Ibiza', '1234ABC'))
   flota.agregar_vehiculo(vehiculo.Vehiculo('Renault', 'Clio', '4321CBA'))
   flota.agregar_vehiculo(vehiculo.Vehiculo('Ford', 'Focus', '1111AAA'))
   flota.agregar_vehiculo(vehiculo.Vehiculo('Opel', 'Corsa', '2222BBB'))
   
   print("\n ------- Flota Inicial --------")
   print(flota)
   
   flota.alquilar_vehiculo('1234ABC')
   flota.alquilar_vehiculo('4321CBA')
   
   print("\n ------- Flota despues de haber alquilado")
   print(flota)
   
   flota.devolver_vehiculo('1234ABC')
   flota.devolver_vehiculo('4321CBA')
   
   print("\n ------- Flota despues de haber devuelto")
   print(flota)
   
   print("\n ------- Flota despues de haber alquilado")
   flota.alquilar_vehiculo('1234ABC')
   print(flota)
