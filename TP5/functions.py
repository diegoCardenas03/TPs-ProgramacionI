
# Función sumar dígitos de un número

def summation(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


def get_sum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total


""" ----FUNCIONES AHORCADO---- """
# Función para encontrar la posición correcta para remplazar correctamente cierto guion bajo


def find_position(list_hanged, random_word, letter):
    # Inicio un contador para que en el for se incremente y ese termine siendo la posición deseada.
    position = 0
    # Recorro las letras de la palabra
    for letter_RW in random_word:
        # Si la letra de la palabra es igual a la letra pasada como argumento
        # Se verifica si esa letra ya se encuentra en la lista, si la letra se encuentra, pero ya ha sido acertada
        # se retorna -1
        # Si no retorna la posición deseada
        if letter_RW == letter:
            if list_hanged[position] == '_':
                return position
        position += 1
    return -1


# Función para actualizar palabra descubierta del juego ahorcado


def updated_word(list_hanged, position, letter):
    # Le asigno la letra pasada como argumento a dicha posición
    list_hanged[position] = letter
    # Convierto la lista en un string y posteriormente le quito los espacios en blanco para así retornarla
    temporally_word = ' '.join(list_hanged)
    temporally_word = temporally_word.replace(" ", "")
    return temporally_word


def create_cardboard():
    cardboard_f = []
    line = []
    print('Ingrese un numero entre el 1 y el 75 sin repetir...')
    # Itero la cantidad de números que tendrá el carton
    for i in range(1, 26):
        while True:
            is_same = False
            number = int(input(f'Posición: {i}, Ingrese un numero: '))
            # Verifico si dentro de las listas de la lista madre el número está y hago demás validaciones...
            for tuple_f in zip(*cardboard_f):
                if number in tuple_f:
                    is_same = True
            if number < 0 or number > 75:
                print(f'El numero introducido no está en los parámetros indicados...')
                continue
            elif number in line or is_same:
                print(f'El numero ya ha sido ingresado antes...')
                continue
            else:
                break
        # Si el número ingresado pasa las validaciones lo agrego a la lista, si ya son 5 elementos los que contiene
        # La agrego a la lista madre como tupla y posteriormente la vacío para empezar otra vez.
        line.append(number)
        if i % 5 == 0:
            cardboard_f.append(tuple(line))
            line.clear()
    # Retorno el valor creado
    return cardboard_f


def horizontal_line(cardboard_f, cardboard_found_f):
    for i in range(0, 5):
        if cardboard_f[i] == cardboard_found_f[i]:
            print(f'BINGO!!, Horizontal en la fila {i+1}')
            return True
    return False


def vertical_line(cardboard_f, cardboard_found_f):
    vertical_card = []
    vertical_card_found = []
    for i in range(0, 5):
        for j in range(0, 5):
            # Creo listas de ambos cartones con sus verticales para verificar si son las mismas
            vertical_card.append(cardboard_f[j][i])
            vertical_card_found.append(cardboard_found_f[j][i])
            if j == 4:
                if vertical_card == vertical_card_found:
                    print(f'Bingo!!! Vertical en la columna {i+1}')
                    return True
                else:
                    vertical_card.clear()
                    vertical_card_found.clear()
    return False


def major_diagonal_line(cardboard_f, cardboard_found_f):
    diagonal_card = []
    diagonal_card_found = []
    for i in range(0, 5):
        # Creo listas de ambos cartones con sus diagonales para verificar si son las mismas
        diagonal_card.append(cardboard_f[i][i])
        diagonal_card_found.append(cardboard_found_f[i][i])
    if diagonal_card == diagonal_card_found:
        print(f'Bingo!!! en la diagonal principal')
        return True
    return False


def reverse_diagonal_line(cardboard_f, cardboard_found_f):
    diagonal_card = []
    diagonal_card_found = []
    j = 4
    for i in range(0, 5):
        # Creo listas de ambos cartones con sus diagonales para verificar si son las mismas
        diagonal_card.append(cardboard_f[i][j])
        diagonal_card_found.append(cardboard_found_f[i][j])
        j -= 1
    if diagonal_card == diagonal_card_found:
        print(f'Bingo!!! en la diagonal inversa')
        return True
    return False


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # El último is elementos ya están en su lugar correcto, así que no es necesario revisarlos nuevamente
        for j in range(0, n-i-1):
            # Intercambia si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        # El último is elementos ya están en su lugar correcto, así que no es necesario revisarlos nuevamente
        for j in range(0, n-i-1):
            # Intercambia si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr):
    n = len(arr)

    # Iterar a través de todos los elementos del arreglo
    for i in range(n):
        # Encontrar el valor mínimo en el arreglo sin ordenar
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Intercambiar el elemento mínimo encontrado con el primer elemento sin ordenar
        arr[i], arr[min_index] = arr[min_index], arr[i]


def bubble_sort_dicts(list_f, key):
    n = len(list_f)
    for i in range(n):
        for j in range(0, n-i-1):
            if list_f[j][key] > list_f[j + 1][key]:
                list_f[j], list_f[j + 1] = list_f[j + 1], list_f[j]


def insertion_sort_len(arr):
    n = len(arr)

    # Recorremos desde el segundo elemento hasta el último
    for i in range(1, n):
        # Guardamos el valor actual para compararlo e insertarlo en la posición correcta
        current_value = arr[i]
        position = i

        # Movemos los elementos mayores hacia la derecha
        while position > 0 and len(arr[position - 1]) > len(current_value):
            arr[position] = arr[position - 1]
            position -= 1

        # Insertamos el valor actual en la posición correcta
        arr[position] = current_value


def counting_sort(arr):
    # Encuentra el valor máximo en el arreglo para determinar el rango.
    max_val = max(arr)

    # Crea un arreglo de conteo con un tamaño igual al valor máximo + 1.
    count = [0] * (max_val + 1)

    # Llena el arreglo de conteo con la frecuencia de cada elemento.
    for num in arr:
        count[num] += 1

    # Reconstruye el arreglo ordenado a partir del arreglo de conteo.
    sorted_arr = []
    for i in range(max_val + 1):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1

    return sorted_arr


def merge_sort(arr):
    if len(arr) > 1:
        # Dividir la lista en dos mitades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamada recursiva para ordenar ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)

        # Fusionar las dos mitades ordenadas
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


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
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    return "El perimeter del radio ingresado es: " + str(perimeter) + " y el area es: " + str(area)


def login(password, user, attempt):
    if user == "usuario1" and password == "asdasd":
        return True
    else:
        attempt += 1
        return False


# Numero primo TP5-Ej13
def vector_magnitude(a, b, c):
    magnitude = math.sqrt(a ** 2 + b ** 2 + c ** 2)
    print(f"La magnitud de un vector que tiene componentes {a, b, c} es {abs(magnitude)}")


# Numero primo TP5-Ej14
def prime_number(number):
    prime_numb = True
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count > 2:
        prime_numb = False

    return prime_numb


# Factorial TP5-Ej15
def factorial(number):
    factorial = 1
    for n in range(1, number + 1):
        factorial *= n
    return factorial
    # print(f"El factorial de {number} es {factorial}")


# ej 10
def apply_discount(shopping_cart, discounts):
    final_prize = 0

    for product, prize in shopping_cart.items():

        if product in discounts:

            discount = discounts[product]
            discount_prize = prize * (1 - discount / 100)
            final_prize += discount_prize

        else:

            final_prize += prize

    return final_prize


# ej 11
def apply_function_to_list(func, input_list):
    result = []
    for element in input_list:
        result.append(func(element))
    return result


# ej 11
def square(x):
    return x ** 2


# ej 12
def word_length_dict(phrase):
    words = phrase.split()
    result = {}

    for word in words:
        result[word] = len(word)

    return result






