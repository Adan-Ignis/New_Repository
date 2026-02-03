# Funciones

# Una función debe hacer una sola cosa y hacerla bien.

def nombre_function(parametros):
    # cuerpo de la function
    return

def hola():
    print("Hola mundo")

x = hola()
# print(x)

def varios():
    return 1, "a", 2, "b"

x1, x2, x3, x4 = varios()
print(x1, x2, x3, x4)

def saludar(nombre: str) -> str:
    return f"Hola {nombre}"