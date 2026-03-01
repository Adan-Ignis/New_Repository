# El programa no funciona en "iOS", "iPadOS"
import os

def limpiar_terminal():
    # Sirve para Windows
    if os.name == "nt":
        os.system("cls")
    # Sirve para Linux y macOS
    else:
        os.system("clear")

lista_numero = []

limpiar_terminal()
for i in range(5):
    indice_lista = i
    while True:
        try:
            numero = int(input(f"Introduce el número {indice_lista + 1}º: "))
            lista_numero.append(numero)
            break
        except ValueError:
            print("Valor invalido")
            print("Pon el valor de nuevo")

    input('Pulsa "Enter" para continuar')
    limpiar_terminal()

print("Lista de numero completa: ", lista_numero)
print("numero mayor: ", max(lista_numero))
print("numero menor: ", min(lista_numero))
print("suma de todos los numeros: ", sum(lista_numero))