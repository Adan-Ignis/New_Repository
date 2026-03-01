# Para simplificar el codigo he hecho que si los valores que se pongan en las variables no sean numericas se ponga por defecto 0, en vez de hacer que la función lidie con parametros de entrada que no sea lo que espere en un principio

# El programa no funciona en "iOS", "iPadOS"
import os

def area_rectangulo(base, altura):
    return +base * +altura

# No es una funcion porque se ejecuta una sola vez
# Sirve para Windows
if os.name == "nt":
    os.system("cls")
# Sirve para Linux y macOS
else:
    os.system("clear")

try:
    base = int(input("Pon la longitud de la base: "))
except ValueError:
    print("Valor invalido")
    print("Se le asignara por defecto 0")
    base = 0

try:
    altura = int(input("Pon la longitud de la altura: "))
except ValueError:
    print("Valor invalido")
    print("Se le asignara por defecto 0")
    altura = 0

print("El area del rectangulo es: ", area_rectangulo(base, altura))