from Car import Car


class Van(Car):
    def __init__(self, color, wheels, velocity, displacement, load):
        super().__init__(color, wheels, velocity, displacement)
        self._load = load

    @property
    def load(self):
        return self._load

    @load.setter
    def load(self, load):
        self._load = load

    def __str__(self):
        return f'{super().__str__()}, Camioneta: [Carga: {self.load}]'
