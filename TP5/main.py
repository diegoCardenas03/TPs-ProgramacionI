from funciones import mayor_menor
from funciones import circunferencia
from funciones import login
"""7. Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
 Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior."""
"""numeros = []
for i in range(5):
    numero = input("Ingrese los numeros de la lista: ")
    numeros.append(numero)

print(mayor_menor(numeros))"""

"""8. Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa 
principal 
que lea el radio de una circunferencia y muestre su área y perímetro."""
"""radio_elegido = int(input("Ingrese el radio de la circunferencia: "))
print(circunferencia(radio_elegido))"""

"""9. Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero
 si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha 
 intentado hacer login y si no se ha podido hacer login incremente este valor."""

intentos = 0
while(True):
    user_choose = input("Ingrese el usuario: ")
    password_choose = input("Ingrese la contraseña: ")
    if login(password_choose,user_choose,intentos):
           print("Ingreso correctamente")
           break
    else:
        intentos += 1
        print("intento numero: " + str(intentos))



