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

saludar("Paco")


def parametros(uno, dos, tres, opcional1):
    return 0

parametros(tres=3, unos=1, dos=2, opcional1="nada")


print(1,2,3, sep="-----")


def parametros(uno, dos, tres, opcional1=""):
    print(uno, dos, tres)


def param_variales(uno, dos, tres, *args, **kwargs):
    print(uno, dos, tres)

param_variales(1,2,22,3)


def sumar(*args):
    print(type(args))
    return sum(args)

total = sumar(1,2,4,3,4,5,6,7,8)
print(total)


def mostrar_config(**Kawargs):
    USUARIO = kwargs.get("usr", "PACO")
    IP = kwargs.get("ip", "127.0.0.1")
    PUERTO = Kwargs.get("puerto", "80")

    print(USUARIO, PUERTO, IP)

mostrar_config(usr=teo,ip="1.2.3.4", altura=1.77)