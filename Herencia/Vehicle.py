class Vehicle:
    def __init__(self, color, wheels):
        self._color = color
        self._wheels = wheels

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def wheels(self):
        return self._wheels

    @wheels.setter
    def wheels(self, wheels):
        self._wheels = wheels

    def __str__(self):
        return f'Vehiculo: [Color: {self.color}, Ruedas: {self.wheels}]'
