
"""1. Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse."""
"""new_list = []
number = None
while (True):
    number = int(input("Ingresa un número, ingresa 0 cuando desees salir: "))
    if number == 0:
        break

    else:
        new_list.append(number)
print(new_list)"""
"""2. A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar."""
"""number_choose = int(input("Ingrese un número para eliminar en la lista: "))
if number_choose in new_list:
    new_list.remove(number_choose)
    print(new_list)
else:
    print("El número " + str(number_choose) + " no pertenece a la lista.")"""
"""3. Imprimir la sumatoria de todos los números de la lista."""
"""addition = 0
for number in new_list:
    addition = addition + number
print("La suma de los valores de la lista es: " + str(addition))"""
"""4. Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella."""
"""number_for_list = int(input("Ingrese un número: "))
minor_list = []
for number in new_list:
    if number < number_for_list:
        minor_list.append(number)
for number in minor_list:
    print(number)"""

"""5. Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella.
 Por ejemplo, si la lista original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]"""
"""list_for_tuple = []
for number in new_list:
   numero = new_list.count(number)
   new_tuple = (number,numero)
   list_for_tuple.append(new_tuple)

unique_tuples = []
for number in set(new_list):
    count = new_list.count(number)
    unique_tuples.append((number, count))

print(unique_tuples)"""
"""6. Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. A continuación, 
solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.
a. Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
b. Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
c. Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
"""
"""students_primary = []
students_secondary = []
while(True):
    student_p = input("Ingrese el nombre de pila de los estudiantes de nivel primario, cuando quiera salir ingrese X: ")
    if student_p == "x":
        break
    else:
        students_primary.append(student_p)
while(True):
    student_s = input("Ingrese el nombre de pila de los estudiantes de nivel secundario, cuando quiera salir ingrese X: ")
    if student_s == "x":
        break
    else:
        students_secondary.append(student_s)
all_students =students_primary + students_secondary
unique_students = list(set(all_students))
print("Nombres de todos los alumnos de nivel primario y secundario (sin repeticiones):")
print(unique_students)
duplicates = [name for name in unique_students if all_students.count(name) > 1]
print("Nombres que se repiten entre los alumnos de nivel primario y secundario:")
print(duplicates)

unique_primary = list(set(students_primary))
unique_secondary = list(set(students_secondary))
names_unique_to_primary = [name for name in unique_primary if name not in unique_secondary]
print("Nombres de nivel primario que no se repiten en los de nivel secundario:")
print(names_unique_to_primary)

"""

