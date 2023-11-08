from cuenta import Cuenta
cuenta1 = Cuenta("",0.0)
nombre = input("Ingrese el nombre del titular de la cuenta: ")
cuenta1.titular = nombre
monto_ingresado = float(input("ingrese el monto que desea depositar a su cuenta: "))
cuenta1.ingresar(monto_ingresado)
monto_extraido = float(input("ingrese el monto que desea extraer de la cuenta: "))
cuenta1.retirar(monto_extraido)
cuenta1.mostrar()