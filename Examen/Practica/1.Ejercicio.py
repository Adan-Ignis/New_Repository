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
nombre1 = input("¿cual es tu nombre?: ")
apellido1 = input("¿cual es tu 1º apellido?: ")
apellido2 = input("¿cual es tu 2º apellido?: ")

nombre_completo = f"{nombre1} {apellido1} {apellido2}"

mayusculas = nombre_completo.upper()
print(mayusculas)

minusculas = nombre_completo.lower()
print(minusculas)

total_caracteres = len(nombre_completo)
print(total_caracteres)

sin_espacios = nombre_completo.strip()
print(sin_espacios)