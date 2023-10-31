import sys
sys.path.append("D:/GIT/Proyectos/Programacion_Grupo/FUNCIONES")
import funciones

"""9.	Escribir un programa que simule el juego clásico de Memoria (Memotest) utilizando matrices. El juego 
consiste en un tablero de cartas boca abajo y el objetivo es encontrar todas las parejas de cartas iguales."""
# Ejercicio 9
couples = [
        ["AA", "BB", "CC", "DD"],
        ["FF", "AA", "EE","FF"],
        ["BB", "DD", "EE", "CC"]]

cards = [
        ["㋡", "㋡", "㋡", "㋡"],
        ["㋡", "㋡", "㋡", "㋡"],
        ["㋡", "㋡", "㋡", "㋡"]]

count = 0

print("        ---- Bienvenido a MemoTest ----")
print("** Encuentre las 6 parejas del siguente tablero indicando las respectivas filas y columnas:")
print("** ATENCION: Los indices tanto para fila y columna van desde 0 a 3")
while True:
    # Muestro el estado de las cartas adivinadas (o no)
    print("* Estado actual *")
    for row in cards:
        for element in row:
            print(element, end= "  ")
        print()
    
    # Pido las posiciones de las cartas a adivinar
    while True:
        print("\n** PRIMERA CARTA:")
        row_1 = int(input("- Fila: "))
        column_1 = int(input("- Columna: "))
        valid_index = funciones.valid_index(row_1, column_1)

        if valid_index == False:
            continue

        print("** SEGUNDA CARTA:")
        row_2 = int(input("- Fila: "))
        column_2 = int(input("- Columna: "))
        valid_index = funciones.valid_index(row_2, column_2)

        if valid_index == False:
            continue
        else:
            break

    # Verifico si se ha acertado
    if (row_1 == row_2) and (column_1 == column_2):
        print("\n** Ha ingresado la misma posicion, intente nuevamente!")
    elif couples[row_1][column_1] == couples[row_2][column_2]:
        # En caso de acertar, "volteo" las cartas adivinadas
        print("\n** ¡Pareja adivinada! **")
        cards[row_1][column_1] = couples[row_1][column_1]
        cards[row_2][column_2] = couples[row_2][column_2]
        # Sumo 1 al contador, que si llega a 6 indica que se han encontrado todas las parejas
        count += 1
    else:
        print("\n** ¡Mala suerte! **")

    if count == 6:
        print("\n **** JUEGO TERMINADO, ¡HA ENCONTRADO TODAS LAS PAREJAS ****")
        break