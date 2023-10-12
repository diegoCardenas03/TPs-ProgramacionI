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
