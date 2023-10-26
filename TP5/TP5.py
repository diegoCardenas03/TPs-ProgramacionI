#  4. Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es múltiplo del otro.
# Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

""" Defino la función

def is_multiple(a, b):
    if a % b == 0:
        return print('El primer número ingresado es múltiplo del segundo.')
    else:
        return print('El primer número no es múltiplo del segundo')


Declaro e inicializo las variables para posteriormente enviar como argumentos

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))

is_multiple(num1, num2) """

# 5. Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de
# cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

"""Defino la función que retorna el promedio de las dos temperaturas

def avg_temperature(max_temp, min_temp):
    return (max_temp + min_temp) / 2


days = int(input('Ingrese la cantidad de días que ingresará: '))

Ya teniendo los días, recorro esa cantidad en un for y retorno la función en un variable promedio para posteriormente
imprimirla

for i in range(1, days+1):
    print(f'Día {i}'.center(50, '-'))
    mx_temp = int(input('Ingrese la temperatura máxima: '))
    mn_temp = int(input('Ingrese la temperatura mínima: '))
    average = avg_temperature(mx_temp, mn_temp)
    print(f'La temperatura promedio de este día fue: {average}')"""

#  6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada
# letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

""" Defino una función, incluyo un bucle for para recorrer cada carácter, si este es una letra habrá un espacio, si no,
 Solo concatenará el carácter


def return_wh_spaces(a_string):
    new_string = ""
    for character in a_string:
        if character.isalpha():
            new_string += character + " "
        else:
            new_string += character
    return new_string

Le pido al usuario la palabra a convertir, para posteriormente retornar el resultado de la función con dicho argumento
En una variable nueva palabra


word = input('Ingrese una palabra: ')
new_word = return_wh_spaces(word)

print(new_word) """
