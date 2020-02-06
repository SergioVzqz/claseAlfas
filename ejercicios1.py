"""
EJERCICIO #1
Crea un programa que pida el nombre y la edad del usuario.
El programa debera imprimir en que año el usuario cumplira 100 años
"""

name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))

age100 = 100 - age

print("Hola " + name + " tu edad en 100 años sera " + str(2020 + age100))

"""
EJERCICIO #2
Crea un programa que pida un numero entero positivo y le haga saber al usuario si es par o primo
(PISTA: investiga el operador modulo, denotado como % en muchos lenguajes de programacion)
"""

num = int(input("Ingresa un numero:\n"))

if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es primo")

"""
EJERCICIO #3
Tome estas listas: 
a = [1, 7, 22, 90, 32, 2, 92, 85, 12]
b = [1, 5, 77, 22, 90, 25, 83, 100, 02, 21, 90]
y crea un programa que cree una nueva lista (o array)
que contenga los elementos que NO se encuentran repetidos en ninguna de las dos lista anteriores
y se imprima la lista completa (tambien se puede imprimir cada elemento de la lista)
"""

a = [1, 7, 22, 90, 32, 2, 92, 85, 12]
b = [1, 5, 77, 22, 90, 25, 83, 100, 2, 21, 90]
c = []

for numberA in a:
    if numberA not in b:
        c.append(numberA)

for numberB in b:
    if numberB not in a:
        c.append(numberB)

print(c)

"""
EJERCICIO #4
Crea un programa que le pida al usuario una palabra y muestre si esa palabra es un palindromo
NOTA: un palindromo es una palabra que se puede escribir al derecho y al reves de la misma manera.
(Por ejemplo: ana, ala, oso)
(EXTRA: intenta hacerlo en 4 lineas de codigo solamente (investiga IF TERNARIO en Python))
"""

word = input("Ingresa una palabra: \n")
wordl = list(word)
print("Es palindromo") if wordl == list(reversed(wordl)) else print("No es palindromo")


"""
EJERCICIO #5
Crea un programa con un diccionario que contenga de llave un nombre
y de valor el cumpleaños de esta persona.
El programa pedira el nombre de la persona y se debera imprimir la fecha de su cumpleaños
"""

user = {'Sergio':'23/06/2000' , 'Sam': '09/06/200', 'Gerardo': '09/09/1971'}
name = input("Ingresa el nombre de la persona:\n")

print("El cumpleaños de "+ name + " es: " + user[name])