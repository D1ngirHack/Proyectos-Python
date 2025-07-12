import os

from src.gestor_notas import GestorNotas


gestor = GestorNotas()

def main():
    print("\n-------- Bienvenido a la gestion de notas --------\n")
    
    while True:
        print("\n ----------------\n MENU\n ----------------\n")
        print("1. Agregar una nota")
        print("2. Leer todas las notas")
        print("3. Buscar una nota")
        print("4. Eliminar una nota")
        print("5. Salir\n")    

        try:
            opcion = int(input("[+] Escoge una opción: "))
        except ValueError:
            print("[!]Opcion no valida")
            continue
        
        if opcion == 1:
            contenido = input("\n[+]Contenido de la nota: ")
            gestor.agregar_nota(contenido)
        elif opcion == 2:
            notas = gestor.leer_todas_las_notas()
            print("\n[+] Mostrando todas las notas almacenadas:\n")
            for i, nota in enumerate(notas):
                print(f"{i}. {nota}")
        elif opcion == 3:
            busqueda = input("\n[+]Contenido de la nota a buscar: ")
            nota_encontradas = gestor.buscar_nota(busqueda)
            print("\n[+] Mostrando las notas encontradas:\n")
            if nota_encontradas:
                for i, nota in enumerate(nota_encontradas, start=1):
                    print(f"{i}. {nota}")
            else:
                print("[!]No se encontraron notas que coincidan con la búsqueda")
        elif opcion == 4:
            # Eliminar una nota
            try:
                indice = int(input("\n[+]Indice de la nota a eliminar: "))
                gestor.eliminar_nota(indice)
                gestor.guardar_notas()
                print("[+]Nota eliminada")
            except ValueError:
                print("[!]Opcion no valida")
                continue
        elif opcion == 5:
            break

        else:
            print("[!]Opcion no valida")
            continue

        input("\n[+]Presione enter para continuar...")

        os.system("cls" if os.name == "nt" else "clear")




if __name__ == '__main__':
    main()