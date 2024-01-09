from ESPACIO import ESPACIO
from OKUMURA import okumura
from Metodo3 import okomura_extension


if __name__ == '__main__':
    input("Presiona cualquier tecla para iniciar el programa...")
# Menu principal        
def mostrar_menu():
    print("----------------------------------------------------------------------------------------------------------------------")
    print("El programa cuenta con tres metodos: ")
    print("[1] PERDIDA EN EL ESPACIO LIBRE")
    print("[2] OKUMURA HATA")
    print("[3] EXTENSION PSC")
    print("[4] Salir")
    print("----------------------------------------------------------------------------------------------------------------------")
# Switch   Modelos de propagación 
opcion = int
while opcion != 4:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        print("----------------------------------------------------------------------------------------------------------------------")
        print("[Path Loss]")
        ESPACIO()
    elif opcion == 2:
        print("----------------------------------------------------------------------------------------------------------------------")
        print("[OKUMURA-HATA]")
        okumura()
    elif opcion == 3:
        print("----------------------------------------------------------------------------------------------------------------------")
        print("[EXTENSION PSC]")
        okomura_extension()
    else:
        print("----------------------------------------------------------------------------------------------------------------------")
        
        print("Opción inválida")

print("¡FIN DEL PROGRAMA!")