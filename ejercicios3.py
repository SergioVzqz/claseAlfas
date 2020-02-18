"""
EJERCICIO #1
Funcion que pida un monto en dinero, decimal o no, y que devuelva el monto mas el 16 de IVA
"""

# num = float(input("Ingresa un numero: "))

# def iva (num):
#   total = num + (num * .16)
#   return total

# print("El valor "+ str(num) +" con el 16% de iva es: "+ str(iva(num)))


"""
EJERCICIO #2
Funcion que pida tres numeros y encuentre el mayor
"""


# num1 = float(input("Ingresa el primer numero: "))
# num2 = float(input("Ingresa el primer numero: "))
# num3 = float(input("Ingresa el primer numero: "))

# def mayor (num1, num2, num3):
#   if (num1 > num2 and num1 > num3):
#     print("El mayor es: "+str(num1))
#   elif(num2 > num1 and num2 > num3):
#     print("El mayor es: "+str(num2))
#   elif(num3 > num1 and num3 > num2):
#     print("El mayor el: "+str(num3))
#   else:
#     print("Algunos numeros son iguales")

# mayor(num1,num2,num3)


"""
EJERCICIO #3
Funcion que pida N numeros y los multiplique todos
"""
"""
def mult (num):
    resultado = 1;
    for i in range(num):
        number = float(input("Ingresa el valor:"))
        resultado *= number
    print("La multipliación de los numeros es: "+str(resultado))   
    
cant = int(input("Ingresa la cantidad de numeros a multiplicar: \n"))

mult(cant)


#Otra solución:

"""

"""

EJERCICIO #4
Funcion que calcule el factorial de un numero
"""
"""
def factorial(num):
    resultado = 1
    for x in range(1, num+1):
        resultado *= x
    return(resultado)

print("El factorial es: "+str(factorial(5)))

"""

"""
EJERCICIO #5
Pide un string y debera imprimirse en orden reverso
ejemplo: "Uriel se encuentra ocupado"
Salida: "ocupado encuentra se Uriel"
"""

Frase = "Hola esto es una prueba"


def Reversa(Text):
    palabras = Text.split(' ')
    palabra = ""
    for i in palabras[::-1]:
        palabra+= i + " "
    print(palabra)

Reversa("Hola como estas")

# def nombre(*args):
#     for arg in args:
#     return None

# nombre(a= 1, b= "Argumento posicional #2", c= [1,2,3,4,5], d= 2.24)


