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

print("1. Mostrar inventario")
print("2. Añadir producto")
print("3. Actualizar cantidad")
print("4. Eliminar producto")
print("5. Salir")

# 1.- Escribe un programa que:
# 1. Pida al usuario su nombre completo.
# 2. Muestre:
# ○ El nombre en mayúsculas.
# ○ El nombre en minúsculas.
# ○ El número total de caracteres (incluyendo espacios).
# ○ El nombre sin espacios al inicio ni al final.

# 2.- Crea una lista con 5 números introducidos por el usuario.
# 1. Muestra:
# ○ La lista completa.
# ○ El número mayor.
# ○ El número menor.
# ○ La suma total de los números.

# 3.- Crea un programa que:
# 1. Solicite al usuario: Nombre, Edad y Ciudad.
# 2. Guarde los datos en un diccionario.
# 3. Muestre un mensaje como: "Juan tiene 25 años y vive en Madrid."

# 4.- Define una función llamada area_rectangulo(base, altura) que devuelva el área.
# 1. Pide al usuario base y altura.
# 2. Muestra el resultado llamando a la función.
# NOTA: Validar que los valores sean positivos.
# 5.- Sistema Básico de Gestión de Inventario
# Desarrollar un programa que permita gestionar un inventario utilizando:
# ● Diccionarios
# ● Bucles
# ● Condicionales

# Crea un programa que gestione un inventario de una tienda.
# El inventario debe almacenarse en un diccionario con la siguiente estructura:
# inventario = {
# "manzanas": 10,
# "peras": 5,
# "naranjas": 8 }
# El programa debe mostrar el siguiente menú repetidamente hasta que el usuario decida salir:
# 1. Mostrar inventario
# 2. Añadir producto
# 3. Actualizar cantidad
# 4. Eliminar producto
# 5. Salir