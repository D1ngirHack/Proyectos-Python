from libro import Libro
from biblioteca_infaltil import BibliotecaInfantil



if __name__ == "__main__":

    biblioteca = BibliotecaInfantil()


    libro1 = Libro(1, "El principito", "Antoine de Saint-Exupéry")
    libro2 = Libro(2, "Cien años de soledad", "Gabriel García Márquez")
    libro3 = Libro(3, "Aprendiendo Hacking", "Jaime Jonay Yanes García")
    libro4 = Libro(4, "Aprendiendo a colorear desde cero", "Pepito Manolete")
    libro5 = Libro(5, "La biblia para pequeños", "Jesus Cristopher")

    # agregar libros
    biblioteca.agregar_libro(libro1, es_para_ninos=True)
    biblioteca.agregar_libro(libro2, es_para_ninos=False)
    biblioteca.agregar_libro(libro3, es_para_ninos=False)
    biblioteca.agregar_libro(libro4, es_para_ninos=True)
    biblioteca.agregar_libro(libro5, es_para_ninos=True)


    # mostrar libros
    biblioteca.mostrar_libros

    # mostrar libros ninos  
    biblioteca.mostrar_libro_ninos
    
    print("\n------ Se prestó de la sección infantil ------")
    # prestar libro
    biblioteca.prestar_libro(1)
    
    print("\n------ Se prestó de la sección general ------")
    # prestar libro
    biblioteca.prestar_libro(2)
    
    
    # mostrar libros disponibles
    biblioteca.libros_disponibles
    
    print("\n------ Se prestó de la sección infantil ------")
    # prestar libro infantil
    biblioteca.prestar_libro(4)
    
    
    # mostrar libros ninos
    biblioteca.mostrar_libro_ninos
    
    
    # mostrar libros prestados
    biblioteca.libros_prestados
    
    
    # mostrar libros prestados ninos
    biblioteca.mostrar_libros_ninos_prestados
    
    print("\n------ Se devolvió de la sección infantil ------")
    # devolver libro
    biblioteca.devolver_libro(1)
        
   
    # mostrar libros
    biblioteca.mostrar_libros
    
    
    print("\n------ Se devolvió de la sección infantil ------")
    # devolver libro ninos
    biblioteca.devolver_libro(4)
    
    
    # mostrar libros ninos
    biblioteca.mostrar_libro_ninos
    
    
    
    


