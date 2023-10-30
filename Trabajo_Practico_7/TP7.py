import sys
sys.path.append("D:/GIT/Proyectos/Programacion_Grupo/FUNCIONES")
import funciones

"""3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor,
año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en función de un campo 
específico, como el año de publicación o el autor."""

# Ejercicio 3

# Lista con diccionarios, cada diccionario contiene informacion sobre X libro
dictionary_list =  [
    {"name": "El código Da Vinci", "author": "Dan Brown", "year": 2003}, 
    {"name": "El gran Gatsby", "author": "Francis Scott Key Fitzgerald " ,"year": 1925},
    {"name": "El niño con el pijama de rayas", "author": "John Boyne", "year": 2006},
    {"name": "La naranja mecánica", "author": "Anthony Burgess", "year": 1962},
    {"name": "Cien años de soledad", "author": "Gabriel García Marquéz", "year": 1967},
    {"name": "Crimen y castigo", "author": "Fyodor Dostoevsky", "year": 1866}]   

# Muestro los libros disponibles
print("------------ Libros disponibles ------------")
for book in dictionary_list:
    print(f"- {book['name']}, ({book['year']}) de {book['author']}")

# Pregunto al usuario como desea ordenarlos
while True:
    option = int(input("\n1) Ordenar alfabeticamente en funcion del nombre del autor. \n2) Ordenar en funcion del año de publicacion. \n3) Salir\n"))
    
    if (option < 1) or (option > 3):
        print("Ingrese una opcion válida")
    else:
        # Si ingreso 1 se ordena por en funcion del nombre del autor
        if option == 1:
            dictionary_list = funciones.bubble_sort_3(dictionary_list, "author")
            print("\n")
            for book in dictionary_list:
                print(f"- {book['author']}: {book['name']}, ({book['year']})")

        # Si ingreso 2 se ordena por año de publicacion
        elif option == 2:
            dictionary_list = funciones.bubble_sort_3(dictionary_list, "year")
            print("\n")
            for book in dictionary_list:
                print(f"- {book['year']}: {book['name']}, de {book['author']}")
        # Si ingreso 3 el programa finaliza
        elif option == 3:
            break
