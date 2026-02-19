# Decorador
def saludar_decorador(func):
    def nueva_function():
        print("Antes de la función")
        func()
        print("Después de la función")
    return nueva_function

def saludar():
    print("Hola mundo")

# saludo = saludar_decorador(saludar)

# saludo()

saludar()

import time

def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"La función ha tardado {fin - inicio:.4f}")
        return resultado
    return envoltura

def sumatorio(limite):
    total = 0
    for i in range(limite):
        total += 1
    return total

x = sumatorio(1000)
print(f"Total: {x}")