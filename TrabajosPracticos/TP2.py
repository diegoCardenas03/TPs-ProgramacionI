
#Ejercicio 1 y 2
"""
years = int(input("Ingrese la cantidad de años de nuestra computadora: "))
if years< 0:
    print('Error, el numero ingresado es menor a 0')
else:
    resultado = "El computador es nuevo" if years<=2 else "El computador es viejo"

    print(resultado)
"""

#Ejercicio 3
""""
first_name = input("Ingrese un nombre: ")
second_name = input("Ingrese un segundo nombre: ")

resultado = "Coincidencia" if first_name[0] == second_name[0]  else "No hay coincidencia"

print(resultado)

"""

#Ejercicio 4 
"""
print('Ingrese A si su candidato elegido es el Verde')
print('Ingrese B si su candidato elegido es el Rojo')
candidato_elegido = input('Ingrese C si su candidato es el Azul: ')
candidato_elegido=candidato_elegido.upper()
if candidato_elegido == 'A':
    print('Su candidato elegido es el Verde.')
elif candidato_elegido == 'B':
    print('Su candidato elegido es el Rojo.')
elif candidato_elegido == 'C':
    print('Su candidato elegido es el Azul.')
else:
    print('el valor ingresado no es correcto')
"""
#Ejercicio 5

"""letra = input("Ingrese una letra: ")
letra = letra.upper()

if len(letra) < 2 :
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print("Es vocal")
    else:
        print("No es vocal")
else:
    print("No se puede procesar el dato")"""

#Ejercicio 6
""""
years = int(input('Ingrese un año: '))
if years % 4 ==0 and (years % 100 != 0 or (years%100==0 and years%400==0)):
    print('Es bisisesto')
else:
    print('No es bisisesto')
"""

#Ejercicio 7
"""
num1= int(input("Ingresa el primer numero: "))
num2= int(input("Ingresa un segundo numero: "))
num3= int(input("Ingresa un tercer numero: "))
menor = 0

if num1<=num2 and num1<num3:
    print("El numero menor es: " + str(num1))
elif num2<=num1 and num2<=num3:
    print("El numero menor es: " + str(num2))
else:
    print("El numero menor es: " + str(num3))
"""

#Ejercicio 8
"""nombre_usuario = input('Ingrese el nombre de usuario: ')
password = input('Ingrese la contraseña: ')
if nombre_usuario == 'Gwenevere' and password == 'excalibur':
    print('Usuario y contraseña correctos. Puede ingresar a Camelot')
else:
    print('Acceso denegado')"""

#Ejercicio 9
"""
name= input("Ingrese su nombre:")
sexo= input("Ingrese su sexo M/F: ")
sexo = sexo.upper()

if sexo == "M":
    if name[0]>"N":
        print("Pertenece al grupo A")
    elif name[0]<"P":
        print("Pertenece al grupo B") 
    else:
        print("Error al ingresar el nombre")
elif sexo == "F":
    if name[0]>"M":
        print("Pertenece al grupo A")
    elif name[0]>"N":
        print("Pertenece al grupo B")
    else:
        print("Error al ingresar el nombre")
else:
    print("Ingresaste mal el sexo")
"""

#Ejercicio 10
"""
age = int(input("Ingrese su edad: "))

if age < 4:
    print("Precio de entrada: GRATIS")
elif (age >= 4 and age < 18):
    print("Precio de entrada: $500")
else:
    print("Precio de entrada: $1000")
"""

#Ejercicio 11
"""
print('\n-- Pizzeria "Bella Napoli" --')

print("\nBienvenido.\nPara ordenar una pizza vegetariana ingrese A.\nPara ordenar una pizza NO vegetariana ingrese B")
pizza = input().upper()

print("\n-INGREDIENTES BASE-")
print(" > Mozzarella \n > Tomate")

print("\nPuede elegir uno de los siguientes ingredientes para agregarle:")

if pizza == "A":                                   # Pizza vegetariana
    print("1) Pimiento \n2) Tofu")
    ingredient = int(input())
    if ingredient == 1:
        ingredient = "Pimiento"
    elif ingredient == 2:
        ingredient = "Tofu"
elif pizza == "B":
    print("1) Peperoni \n2) Jamón \n3) Salmón ")    #Pizza no vegetariana
    ingredient = int(input())
    if ingredient == 1:
        ingredient = "Peperoni"
    elif ingredient == 2:
        ingredient = "Jamón"
    elif ingredient == 3:
        ingredient = "Salmón"

print("-------------------------")
if pizza == "A":
    print("PIZZA VEGETARIANA")
    print("Ingredientes:")
    print(" > Mozzarella \n > Tomate \n >", ingredient)
    print("Disfrute su comida!")
elif pizza == "B":
    print("PIZZA NO VEGETARIANA")
    print("Ingredientes:")
    print(" > Mozzarella \n > Tomate \n >", ingredient)
    print("Disfrute su comida!")
"""

#Ejercicio 12
"""
current_year = int(input("Ingrese el año actual: "))
year = int(input("Ingrese cualquier otro año: "))

if year == current_year:
    print("Los años ingresados son los mismos.")
elif (year < current_year):
    print("Han pasado ", (current_year - year), " años desde ", year, " hasta el año actual.")
else:
    print("Faltan ", (year - current_year), " años para llegar a ", current_year, ".")
"""

#Ejercicio 13
"""
num1 = int(input("Ingrese el primer numero (Mayor que 0): "))
num2 = int(input("Ingrese el segundo numero (Mayor que 0): "))

if num1 > num2:
    larger = num1
    smaller = num2
elif num2 > num1:
    larger = num2
    smaller = num1

print(" > Mayor: ", larger, "\n > Menor: ", smaller)

if ((larger <= 0) or (smaller <= 0)):
    print("Por lo menos uno de los numeros ingresados no es valido.")
else:
    if larger % smaller == 0:
        print(larger, " es multiplo de ", smaller)
    else:
        print(larger, " no es multiplo de ", smaller)
"""


"""14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba 
la solución.Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o 
que todos los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a"""
#Ejercicio 14
"""a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))

if a == 0:
    if b == 0:
        print("La ecuación {a}x + {b} = 0 tiene infinitas soluciones.")
    else:
        print("La ecuación {a}x + {b} = 0 no tiene solución.")
else:
    x = -b / a
    print(f"La solución de la ecuación {a}x + {b} = 0 es x = {x}")"""
    
    
"""15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un 
círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene 
que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de 
un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área."""
#Ejercicio 15
"""import math
print("Ingrese 'T' o 't' para calcular el area de un tiangulo \nIngrese 'C' o 'c' para calcular el area de un circulo")
area_toc = input("--> ")

if area_toc.lower() == 't':
    base =  int(input("Ingrese la base del triangulo: "))
    height = int(input("Ingrese la altura del triangulo: "))
    area = (base * height) / 2
    print(f"El area del triangulo es {area}")
elif area_toc.lower() == 'c':
    radius = int(input("Ingrese el radio del circulo: "))
    pi = math.pi
    area = (pi * radius ** 2)
    print(f"El area del circulo es {area}")"""
    
"""16-	Haz una calculadora básica pida al usuario dos valores, a y b.
Según la opción que desean, realizar la operación:
•	Si operación es 1 entonces debemos ver el resultado de a + b
•	Si operación es 2 entonces debemos ver el resultado de a * b
•	Si operación es 3 entonces debemos ver el resultado de a - b
•	Si operación es 4 entonces debemos ver el resultado de a / b"""
#Ejercicio 16
"""print("Calculadora")
number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

print("Operaciones: \n1.Suma \n2.Multiplicacion \n3.Resta \n4.Division")
opc = int(input("Segun las opciones ingrese el numero de la operacion que desea realizar: "))

if opc == 1:
    operation = "suma"
    result = number1 + number2
elif opc == 2:
    operation = "multiplicacion"
    result = number1 * number2
elif opc == 3:
    operation = "resta"
    result = number1 - number2
elif opc == 4:
    operation = "division"
    result = number1 / number2
   
print(f"La {operation} entre {number1} y {number2} es {result}")"""


"""17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje 
diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de 
esos, imprimir otro mensaje."""
#Ejercicio 17
"""day = input("Ingrese un dia de la semana: ")

if day.lower() == "lunes":
    print("Es lunes. Arranca la semana")
elif day.lower() == "viernes":
    print("Es viernes. Ya casi es fin de semana")
elif day.lower() == "sabado" or day.lower() == "domingo":
    print("Ya es fin de semana")
elif day.lower() == "martes" or day.lower() == "miercoles" or day.lower() == "jueves":
    print("No es un día relevante de la semana.")"""
    
    
"""18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora. La jornada de trabajo 
mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas 
laborales comunes."""
#Ejercicio 18
"""hours = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
salary_per_hour = int(input("Ingrese el salario por hora: "))
minimum_hous = 48
salary = hours * salary_per_hour

if hours > minimum_hous:
    extra_percentage = salary * 0.10
    salary += extra_percentage
    print(f"Trabajó horas extras, su salario es de ${salary}")
else:
    print(f"Su salario es de ${salary}")"""
    
    
"""19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe 
un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento."""
#Ejercicio 19
"""pencil = int(input("Ingrese la cantidad de lapices que quiere comprar: "))
price = pencil * 60

if pencil >= 1000:
    discount = price * 0.07
    price -= discount
else:
    price = price
    
print(f"Si compras {pencil} lapices el precio final es de ${price}")"""

"""20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) 
notas, es mayor o igual a 6; caso contrario saldrá desaprobado."""
#Ejercicio 20
"""sum = 0

for i in range(1,5):
    grade = int(input(f"Ingrese la {i}° notas del alumno: "))
    sum += grade

average = sum / 4
if average >= 6:
    print(f"El alumno está aprobado con promedio {average}")
else:
    print(f"El alumno está desaprobado con promedio {average}")"""
