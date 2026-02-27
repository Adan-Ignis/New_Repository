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