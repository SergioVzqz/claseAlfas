"""
Estrucutura de una función en python

def nombre_de_la_funcion(argumentos):
    operacion
    operacion2
    return operacion3
"""
"""
# def saludo(name):
#     print("Hola "+ name + "!!")

# nombre = input("Ingresa un nombre: ")

# saludo(nombre)

numero = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))

# def suma(n1, n2):
#     return n1 + n2

# print(suma(numero,numero2))

def resta(n1 = 10, n2 = 5):
    return n1 - n2

print(resta())

"""

# def posicional(*argumentos):
#     for arg in argumentos:
#         print(arg)
#     return None

# posicional(1, "Argumento posicional #2", [1,2,3,4,5], "Args pos #4")
"""
def nombre(**z):
    for argumento in z:
        print(str(argumento) + " = " + str(z[argumento]))
    return None

nombre(a= 1, b= "Argumento posicional #2", c= [1,2,3,4,5], d= 2.24)

"""

"""
Pasar varios argumentos con o sin nombre
Para los argumentos sin nombre, debera imprimir su valor
Para los argumentos con nombre, debera imprimir el nombre y su valor
"""


def combinacional(*args, **kwargs):
    suma = 0
    for arg in args:
        suma += args
    print("Suma= " + str(suma))

    for kwarg in kwargs:
        print(str(kwarg) + "=" + str(kwargs[kwarg]))

combinacional(1, 2, 3, a="A", b="b" )

# def combinacional(*args, **kwargs):
#     for argumento in kwargs:
#         print(str(argumento) + " = " + str(z[argumento]))
#     return None


# combinacional(a='Hola', "10" , b="3", [1, 2, 3])
