from motocicleta import Motocicleta
# Creo una instancia de la clase motocicleta
moto_1 = Motocicleta("Blanco", "GG-717-XD", 10, 2, "Yamaha", "YZF-R1", 2014, 300, 200)
moto_2 = Motocicleta("Rojo", "TA-583-OP", 10, 2, "Honda", "Rebel 300", 2017, 145, 165)

# Programa
print("**** Bienvenido al concesionario ****")
print("** Las motocicletas que le ofrecemos el dia de hoy son estas:")

# Pruebas con las motocicletas
while True:
    # Muestro la motocicleta
    while True:
        print(f'1. {moto_1.brand} "{moto_1.model}" \n2. {moto_2.brand} "{moto_2.model}"')
        choice = int(input("\nPulse el numero correspondiente a la motocicleta de la cual quiere ver su ficha tecnica: "))
        if choice == 1:
            current_motorcycle = moto_1
            moto_1.showing_motorcycle()
            break
        elif choice == 2:
            current_motorcycle = moto_2
            moto_2.showing_motorcycle()
            break
        else:
            print("La opcion ingresada no se encuentra en nuestro catalogo, ingrese nuevamente")

    # Pruebo el motor
    print("\n*** Prueba de motor ***")
    while True:
        while True:
            if current_motorcycle.engine == False:
                status = "Apagado"
            else:
                status = "Encendido"
            print(f"< ESTADO DEL MOTOR: {status} >")
            choice = int(input("** Ingrese el número correspondiente a la acción que desee realizar:\n \n1. Encender motor \n2. Apagar motor\n"))
            if choice == 1:
                current_motorcycle.start()
            elif choice == 2:
                current_motorcycle.stop()
            else:
                print("Ingrese una opción válida")
            
            finish = int(input("\n** Desea realizar más pruebas con el motor: \n1. Realizar más pruebas \n2. Terminar pruebas\n"))
            if finish == 2:
                break
            elif finish == 1:
                continue
            else:
                print("Ingrese una opcion valida")

        if finish == 2:
            break

    # Pregunto si quiere ver otra motocicleta:
    finish = int(input("\n** Desea probar otra motocicleta del catálogo? \n1. SI \n2. No, salir\n"))
    if finish == 1:
        continue
    elif finish == 2:
        break
    else:
        print("Ingrese una opcion válida")
