print("Hola usuario")
nombre = input("¿cual es tu nombre?: ")
edad = int(input("¿cual es tu edad?: "))
ciudad = input("¿donde vives?: ")

persona = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad
}

print(persona["nombre"].value, " tiene ", persona["edad"].value, " y vive en ", persona["ciudad"].value)