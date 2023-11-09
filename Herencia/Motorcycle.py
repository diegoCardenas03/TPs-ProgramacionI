from Bike import Bike


class Motorcycle(Bike):
    def __init__(self, color, wheels, type_b, velocity, displacement):
        super().__init__(color, wheels, type_b)
        self._velocity = velocity
        self._displacement = displacement

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        self._velocity = velocity

    @property
    def displacement(self):
        return self._displacement

    @displacement.setter
    def displacement(self, displacement):
        self._displacement = displacement

    def __str__(self):
        return f'{super().__str__()}, Motocicleta: [Velocidad: {self.velocity}, Cilindrada: {self.displacement}]'
    