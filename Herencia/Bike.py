from Vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self, color, wheels, type_b):
        super().__init__(color, wheels)
        self._type_b = type_b

    @property
    def type_b(self):
        return self._type_b

    @type_b.setter
    def type_b(self, type_b):
        self._type_b = type_b

    def __str__(self):
        return f'{super().__str__()}, Bicicleta: [Tipo: {self._type_b}]'
