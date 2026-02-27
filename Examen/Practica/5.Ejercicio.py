inventario = {
    "manzanas": 10,
    "peras": 5,
    "naranjas": 8
}

while True:
    # Las variables se "resetean" en cada interración del bucle para evitar problemas con sus valores gaurdados en la cache
    clave = None
    valor = None

    print("1. Mostrar inventario")
    print("2. Añadir producto")
    print("3. Actualizar cantidad")
    print("4. Eliminar producto")
    print("5. Salir")
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
        valor = int(input("Pon la cantidad: "))
        inventario[clave] = valor

    elif numero == 4:
        print("4. Eliminar producto")
        clave = input("Pon el nombre del producto que quieres quitar: ")

        try:
            del inventario[clave]
        except KeyError:
            print("El producto no existe")
    
    elif numero == 5:
        break

    else:
        print("Opción invalida")