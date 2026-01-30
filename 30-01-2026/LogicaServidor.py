# Ignacio Gómez Vázquez

    # 1. Escriba un programa que solicite al usuario que ingrese una cadena. El programa debería mostrar lo siguiente:
    # (a) El número total de caracteres de la cadena
    # (b) La cadena repetida 10 veces
    # (c) El primer carácter de la cadena (recuerde que los índices de cadena empiezan en 0)
    # (d) Los tres primeros caracteres de la cadena
    # (e) Los tres últimos caracteres de la cadena
    # (f) La cadena al revés
    # (g) El séptimo carácter de la cadena si la cadena es lo suficientemente larga; en caso contrario, un mensaje
    # (h) La cadena sin el primer y el último carácter
    # (i) La cadena en mayúsculas
    # (j) La cadena con cada a reemplazada por una e
    # (k) La cadena con cada letra reemplazada por un espacio

cadena = input("Dame un cadena") # A | Igual que el profesor

for i in range(11): # B
    print(cadena)

print(f'(a) La cadena tiene {len(cadena)} caracteres') # Profesor

for i in range(10): # B | Profesor
    print(f'(b) {cadena}')

# print((cadena + '\n')* 10) Hace lo mismo que el bucle for | Profesor

for i in (cadena(0)): # C
    print(cadena[i])

print(f'(c) {cadena[0]}') # C | Profesor

for i in (cadena(2)): # D
    print(cadena[i])

print(f'(d) {cadena[:3]}') # D | Profesor

for i in (cadena(-3, -1)): # E
    print(cadena[i])

print(f'(e) {cadena[-3:]}') # E | Profesor

for i in (cadena(::-1)): # F
    print(cadena[i])

print(f'(f) {cadena[::-1]}') # F | Profesor

for i in (cadena(6, 6)): # G
    if cadena(6) != none:
        print(cadena[5])
    else
        print("La cadena tiene menos de 6 caracteres alfanumericos")

if len(cadena) > 6: # G | Profesor
    print(f'(g) {cadena[6]}')
else:
    print(f'(g) {La cadena es corta}')

for i in (cadena(1,-2, 1)): # H
    print(cadena[i])

print(f'(f) {cadena[1:-1]}') # H | Profesor

for i in (cadena()): # I
    mayuscula = cadena[i]
    print(mayuscula)

print(f'(i) {cadena.upper()}') # I | Profesor

for i in (cadena()): # J
    if cadena[i] == "a":
        cadena[i] = "e"
    print(cadena[i])

print(f'(j) {cadena.replace('a', 'e')}') # J | Profesor
# print(f'(j) {cadena.replace('a', 'e').replace('A', 'E')}') # Solución propuesta por mi compañero Luisma en donde contatena varias intrucciones para tambien tener en cuenta las mayusculas

for i in (cadena()): # K
    if cadena[i] == #caracter alfanumerico
        cadena[i] = " " #espacio en blanco
    print cadena[i]

# otra = '' # K | Profesor
# for letra in cadena:
#     otra += '*'

# print(f'(k) {otra}')

# print(f'{"*" * len(cadena)}') # Solución propuesta por mi compañero sergai

    # 2. Una forma sencilla de estimar el número de palabras en una cadena es contar el número de espacios en la cadena. <br>Escriba un programa que solicite al usuario una cadena y devuelva una estimación de cuántas palabras tiene.

cadena = "Esta es una cadena de prueba" # Profesor
print(f"{cadena.count(' ') + 1}")

    # 3. A menudo se olvida cerrar los paréntesis al introducir fórmulas.
    #Escriba un programa que solicite al usuario que introduzca una fórmula e imprima si esta tiene el mismo número de paréntesis de apertura y cierre.

    # 9. Solicite al usuario un número e imprima lo siguiente, donde el patrón termina en el número ingresado por el usuario.
    
    # 1
    #  2
    #   3
    #    4

cadena = input("Dame un numero")

for i in (len(cadena)):
    print(f' ' * i + f'{cadena}')

# Solución del profesor
numero = int(input('Dame un número'))
for i in range(numero):
    print(' ' * i, i + 1)