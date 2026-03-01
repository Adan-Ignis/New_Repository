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
    numero_clave = i
    print("Lista de numeros: ")
    for valor in lista_numero:
        print(f"clave {numero_clave+1}: {valor}")

    while True:
        try:
            numero = int(input(f"Introduce el número {i+1}º: "))
            lista_numero.append(numero)
            break
        except ValueError:
            print("Valor invalido")
            print("Pon el valor de nuevo")
    
    input('Pulsa "Enter" para continuar')
    limpiar_terminal()

print("Lista de numero completa: ", lista_numero)