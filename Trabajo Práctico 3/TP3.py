# Ejercicio 1

# palabra = input("Ingrese una palabra: ")

# for i in range(11):
#   print("N°"+ str(i) + " " +palabra)
""" 2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input('Ingrese su edad: '))
for i in range(edad):
    print(i+1)"""
""" 3- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 
1 hasta ese número separados por comas."""
"""number = int(input("Ingrese un número entero positivo: "))
for i in range(number):
    result = []
    if i % 2 != 0:
        result.append(str(i))

        final_result = ', '.join(result)
        print(final_result)"""
"""4- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
"""
number_4 = int(input("Ingrese un numero entero positivo:"))
arreglo=[]
for i in range((number_4),0,-1):
    arreglo.append(str(i))

arreglo_final = ",".join(arreglo)
print(arreglo_final)"""

"""5-Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""
#Ejercicio5
"""amount = int(input(f'Ingrese la cantidad a invertir: '))
interest = input(f'Ingrese el interés anual: ') 
interest = float(interest.strip('%')) / 100 #Convierto el string generado quitandole el signo porcentual '%', lo convierto a float y calculo el número. 
years = int(input(f'Ingrese el número de años: '))
for i in range(1, years+1):
    amount += amount * interest
    print(f'Capital obtenido el año {i}: ${amount}')"""

""" 6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido. """
#Ejercicio6

"""altura = int(input(f'Ingrese la altura: '))

for i in range(1,altura+1):
    print('*' * i)"""

""" 7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10. """
#Ejercicio7

"""for i in range(1,11):
    for j in range(1,11):
        print(f'{i}*{j} = {i*j}')"""

""" 8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo. """
#Ejercicio8
    
"""numTriangle = int(input("Ingrese un número entero: "))


for i in range(1, numTriangle + 1):
    for j in range(2 * i - 1, 0, -2): #Hago que los numeros se muestren de forma descendente.
        print(j, end=' ')
    print()"""