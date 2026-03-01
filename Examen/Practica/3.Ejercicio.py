# El programa no funciona en "iOS", "iPadOS"
import os

# No es una funcion porque se ejecuta una sola vez
# Sirve para Windows
if os.name == "nt":
    os.system("cls")
# Sirve para Linux y macOS
else:
    os.system("clear")

print("Hola usuario")
nombre = input("¿cual es tu nombre?: ")

try:
    edad = int(input("¿cual es tu edad?: "))
except ValueError:
    print("valor invalido")
    print("Se le asignara por defecto nulo")
    edad = None
ciudad = input("¿donde vives?: ")

persona = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad
}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")