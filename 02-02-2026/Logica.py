# 1. Escriba un programa que solicite repetidamente al usuario el nombre y el precio de los productos. Almacene todos estos datos en un diccionario cuyas claves sean los nombres de los productos. Almacene todos estos datos en un diccionario cuyas claves sean los nombres de los productos y cuyos valores sean los precios.

# Terminará al introducir un producto vacío.

# Se podrán introducir productos repetidos, pero solo se almacenarán una vez y se imprimirá el precio correspondiente o un mensaje si el producto no está en el diccionario.

productos = {}
while True:
    nombre = input("Dime el nombre del producto: ")
    if nombre == "":
        break
    
    precio = input("Dime el precio: ")
    productos[nombre] = precio

    from pprint import pprint
    # Por si quiere guardar el primer valor introducido
    if not nombre in producto:
        productos[nombre] = precio
    else:
        print(f'El producto "{nombre}" ya esta en el diccionario')
    
    from pprint import pprint
    pprint(productos)

# 2. Usando el diccionario creado en el problema anterior, permita al usuario ingresar una cantidad en dólares e imprima todos los productos cuyo precio sea menor a esa cantidad en dolares e imprima todos los productos cuyo precio sea menor a esa cantidad.

filtro = float(input("Dime el precio máximo: "))
for k,v in productos.items():
    if v < filtro:
        print(f"Producto: {k}, Precio: {v}")

# 3. Para este problema, cree un diccionario cuyas claves sean los nombres de los meses y cuyo valores sean el número de días de los meses correspondientes.

# (a) Pida al usuario que ingrese el nombre de un mes y use el diccionario para indicarle cuántos días tiene el mes.
# (b) Imprima todas las claves en orden alfabético.
# (c) Imprima todos los meses de 31 días.
# (d) Imprima los pares (clave-valor) ordenados por el número de días de cada mes.
# (e) Modifique el programa de la parte (a) y el diccionario para que el usuario no tenga que saber cómo escribir el nombre del mes con exactitud. Es decir, solo tiene que escribir correctamente las tres primeras letras del nombre del mes.

meses = {
    "Enero": 31,
    "Febrero": 28,
    "Marzo": 31,
    "Abril": 30,
    "Mayo": 31,
    "Junio": 30,
    "Julio": 31,
    "Agosto": 31,
    "Septiembre": 30,
    "Octubre": 31,
    "Noviembre": 30,
    "Diciembre": 31
}

mes = input("Dime el nombre del mes: ")
if mes in meses:
    print(f"El mes de {mes} tiene {meses[mes]} días")
else:
    print("Mes incorrecto")

# b)
claves = list(meses.keys())
claves.sort()
print(claves)
print(sorted(meses.keys()))

# c)
días = int(input("Cuantos días: "))
for m,d in meses.items():
    if d == 31:
        print(m)

# d)
for k,v in sorted(meses.items(),key=lambda)

# e)
