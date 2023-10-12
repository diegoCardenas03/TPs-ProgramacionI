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
number_4 = int(input("Ingrese un numero entero positivo:"))
arreglo=[]
for i in range((number_4),0,-1):
    arreglo.append(str(i))

arreglo_final = ",".join(arreglo)
print(arreglo_final)
