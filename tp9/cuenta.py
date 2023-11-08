"""2. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos."""
class Cuenta:
    cantidad = 0.0
    def __init__(self, titular, cantidad):
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, nuevo_titular):
        self._titular = nuevo_titular

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad

    def mostrar(self):
        print("El titular de la cuenta es: " + self._titular)
        print("El monto disponible es: " + str(self._cantidad))

    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        self._cantidad -= cantidad






