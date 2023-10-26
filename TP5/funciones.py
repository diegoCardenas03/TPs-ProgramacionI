import math

# Funcion verificacion dni (ejercicio 1)
def dni_verification(document):
    if (len(document) == 7) or (len(document) == 8):
        valid = True
    else:
        valid = False
    return valid

# Funcion verificacion largo ultima palabra de un string (ejercicio 2)
def last_word_lenght(w_list):
    last_word = w_list[-1]
    l_w_length = len(last_word)

    return l_w_length

# Funcion para ingresar y verificar nombre del integrante (ejercicio 3)
def name_verification(m_name):
    valid_name = True
    if (len(m_name) < 2) or (len(m_name) > 3):
        valid_name = False
    
    return valid_name

# Funcion para generar el identificador del integrante (ejercicio 3)
def member_id_generator(m_name, dni):
    first_name = str(m_name[0]).replace(',', '').strip().capitalize()
    last_name_length = str(len(m_name[-1]))
    first_numbers_dni = str(dni[0:3])
    member_id = str(first_name + last_name_length + first_numbers_dni)
    return member_id

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
