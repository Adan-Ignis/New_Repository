# Ejericicio 1
print("Hola usuario")
nombre1 = input("¿cual es tu nombre?: ")
apellido1 = input("¿cual es tu 1º apellido?: ")
apellido2 = input("¿cual es tu 2º apellido?: ")

nombre_completo = f"{nombre1} {apellido1} {apellido2}"

mayusculas = nombre_completo.upper()
print(mayusculas)

minusculas = nombre_completo.lower()
print(minusculas)

total_caracteres = len(nombre_completo)

sin_espacios = nombre_completo.strip()

# Ejercicio 2

lista_numero = []

for i in range(5):
    numero = int(input(f"Introduce el número {i+1}º: "))
    lista_numero.append(numero)

print("Lista de numero completa: ", lista_numero)

# Ejercicio 3

nombre3 = None
edad = None
ciudad = None

print("Hola usuario")
nombre3 = input("¿cual es tu nombre?: ")
edad = int(input("¿cual es tu edad?: "))
ciudad = input("¿donde vives?: ")

persona = {
    "nombre": nombre3,
    "edad": edad,
    "ciudad": ciudad
}

print(persona["nombre"].value, " tiene ", persona["edad"].value, " y vive en ", persona["ciudad"].value)

# Ejercicio 4

def area_rectangulo(base, altura):
    return +base * +altura

base = int(input("Pon la longitud de la base: "))
altura = int(input("Pon la longitud de la altura: "))
print(area_rectangulo(base, altura))

# Ejercicio 5

inventario = {
    "manzanas": 10,
    "peras": 5,
    "naranjas": 8
}

do {
    # Las variables se "resetean" en cada interración del bucle para evitar problemas con sus valores gaurdados en la cache
    clave = None
    valor = None

    print("1. Mostrar inventario")
    print("2. Añadir producto")
    print("3. Actualizar cantidad")
    print("4. Eliminar producto")
    print("5. Salir")
    numero5 = int(input(Selecciona una opcion: ))

    if numero5 == 1:
        print("1. Mostrar inventario")
        print(inventario)

    elif numero5 == 2:
        print("2. Añadir producto")
        clave = input("Pon el nombre del nuevo producto: ")
        inventario[clave] = valor

    elif numero5 == 3:
        print("3. Actualizar cantidad")
        clave = input("Pon el nombre del producto: ")
        valor = int(input("Pon la cantidad: "))
        inventario[clave] = valor

    elif numero5 == 4:
        print("4. Eliminar producto")
        clave = input("Pon el nombre del producto que quieres quitar: ")

        try:
            del inventario[clave]
        except KeyError:
            print("El producto no existe")

    else:
        print("Opción invalida")

} while(numero5 != 5)

print("5.Salir")