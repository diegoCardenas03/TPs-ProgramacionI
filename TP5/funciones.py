import math

def is_multiple(a, b):
    if a % b == 0:
        return print('El primer número ingresado es múltiplo del segundo.')
    else:
        return print('El primer número no es múltiplo del segundo')

def avg_temperature(max_temp, min_temp):
    return (max_temp + min_temp) / 2

def return_wh_spaces(a_string):
    new_string = ""
    for character in a_string:
        if character.isalpha():
            new_string += character + " "
        else:
            new_string += character
    return new_string

def mayor_menor(number_list):
    el_mayor = number_list[0]
    el_menor = number_list[0]
    for i in number_list:
        if i > el_mayor:
                el_mayor = i
        if i < el_menor:
                el_menor = number_list[i]
    return "El mayor valor es: " + str(el_mayor) + " el menor valor es: " + str(el_menor)
def circunferencia(radius):
    area = math.pi*(radius ** 2)
    perimeter = 2 * math.pi * radius
    return "El perimeter del radio ingresado es: " + str(perimeter) + " y el area es: " + str(area)

def login(user,password, attempt):
    if user == "usuario1" and password == "asdasd":
        return True
    else:
        attempt += 1
        return False


#Numero primo TP5-Ej13    
def vector_magnitude(a,b,c):
    magnitude = math.sqrt(a**2 + b**2 + c**2)
    print(f"La magnitud de un vector que tiene componentes {a,b,c} es {abs(magnitude)}")
 
#Numero primo TP5-Ej14  
def prime_number(number):
    prime_numb = True
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    
    if count > 2:
        prime_numb = False
    
    return prime_numb

#Factorial TP5-Ej15
def factorial(number):
    factorial = 1    
    for n in range(1, number+1):
        factorial *= n
        
    print(f"El factorial de {number} es {factorial}")
         