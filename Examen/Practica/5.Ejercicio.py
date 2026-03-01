# El programa no funciona en "iOS", "iPadOS"
import os
# No he importado la biblioteca "readchar" porque no es nativa de "python" por lo que el usuario debe tenerla instalada antes de ejecutar el programa
#import readchar

def limpiar_terminal():
    # Sirve para Windows
    if os.name == "nt":
        os.system("cls")
    # Sirve para Linux y macOS
    else:
        os.system("clear")

inventario = {
    "manzanas": 10,
    "peras": 5,
    "naranjas": 8
}

limpiar_terminal()
while True:
    # Las variables se "resetean" en cada interración del bucle para evitar problemas con sus valores gaurdados en la cache
    clave = None
    valor = None

    print("1. Mostrar inventario")
    print("2. Añadir producto")
    print("3. Actualizar cantidad")
    print("4. Eliminar producto")
    print("5. Salir")
    

    try:
        numero = int(input("Selecciona una opcion: "))

        if numero == 1:
            print("1. Mostrar inventario")
            print(inventario)

        elif numero == 2:
            print("2. Añadir producto")
            clave = input("Pon el nombre del nuevo producto: ")
            inventario[clave] = valor

        elif numero == 3:
            print("3. Actualizar cantidad")
            clave = input("Pon el nombre del producto: ")

            if clave in inventario:
                try:
                    valor = int(input("Pon la cantidad: "))
                    inventario[clave] = valor
                except ValueError:
                    print("Valor invalido")
                    print("La cantidad del producto no se ha modificado")
            else:
                print("El producto no existe")

        elif numero == 4:
            print("4. Eliminar producto")
            clave = input("Pon el nombre del producto que quieres quitar: ")

            try:
                del inventario[clave]
            except KeyError:
                print("El producto no existe")
        
        elif numero == 5:
            break

    except ValueError:
        print("Opcion invalida")

    #Se puede escribir cualquier cosa antes de pulsar "Enter"
    input("Presiona Enter para continuar")
    limpiar_terminal()