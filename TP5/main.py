from funciones import *

#  4. Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es múltiplo del otro.
# Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.


""" #Declaro e inicializo las variables para posteriormente enviar como argumentos

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))

is_multiple(num1, num2) """

# 5. Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de
# cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

"""
days = int(input('Ingrese la cantidad de días que ingresará: '))

# Ya teniendo los días, recorro esa cantidad en un for y retorno la función en un variable promedio para posteriormente
# imprimirla

for i in range(1, days+1):
    print(f'Día {i}'.center(50, '-'))
    mx_temp = int(input('Ingrese la temperatura máxima: '))
    mn_temp = int(input('Ingrese la temperatura mínima: '))
    average = avg_temperature(mx_temp, mn_temp)
    print(f'La temperatura promedio de este día fue: {average}')"""

#  6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada
# letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

"""

#Le pido al usuario la palabra a convertir, para posteriormente retornar el resultado de la función con dicho argumento
#En una variable nueva palabra


word = input('Ingrese una palabra: ')
new_word = return_wh_spaces(word)

print(new_word) """


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

"""
intentos = 0
while(True):
    user_choose = input("Ingrese el usuario: ")
    password_choose = input("Ingrese la contraseña: ")
    if login(password_choose,user_choose,intentos):
           print("Ingreso correctamente")
           break
    else:
        intentos += 1
        print("intento numero: " + str(intentos))"""



