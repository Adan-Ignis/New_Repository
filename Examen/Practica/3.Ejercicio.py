print("Hola usuario")
nombre = input("¿cual es tu nombre?: ")
edad = int(input("¿cual es tu edad?: "))
ciudad = input("¿donde vives?: ")

persona = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad
}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")