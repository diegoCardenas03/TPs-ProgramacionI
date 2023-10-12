#Ejercicio 8
"""
num = int(input("Ingrese un numero: "));

for i in range(1, num +1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()

"""

#Ejercicio 9
"""
contraseña = input("Ingrese una contraseña: ")
opc = True
print()
while opc:
    palabra= input("Ingrese su contraseña: ")
    if contraseña == palabra:
        print("Contraseña correcta")
        opc = False3
    else:
        continue    
"""

#Ejercicio 10
"""
numPrimo = int(input("Ingrese un numero: "))
contador = 0

for x in range(0, numPrimo):
    if numPrimo%(x+1)==0:
        contador+=1

if contador==2:
    print("Es un numero primo")
else:
    print("No es un numero primo")
"""

#Ejercicio 11
"""
palabra = input("Ingrese una palabra: ")
print()

for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])
"""