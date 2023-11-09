from Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, color, wheels, velocity, displacement):
        super().__init__(color, wheels)
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
        return (f'{super().__str__()}, Auto: [Velocidad: {self.velocity}, '
                f'Cilindrada: {self.displacement}]')
