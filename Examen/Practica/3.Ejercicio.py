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