class Triangle:
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    @property
    def side1(self):
        return self._side1

    @side1.setter
    def side1(self, side1):
        self._side1 = side1

    @property
    def side2(self):
        return self._side2

    @side2.setter
    def side2(self, side2):
        self._side2 = side2

    @property
    def side3(self):
        return self._side3

    @side3.setter
    def side3(self, side3):
        self._side3 = side3

    def larger_size(self):
        if self.side1 >= self.side2 and self.side1 > self.side3:
            return f'El lado mayor: {self.side1}'
        elif self.side2 >= self.side1 and self.side2 > self.side3:
            return f'El lado mayor: {self.side2}'
        else:
            return f'El lado mayor: {self.side3}'

    def triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Su tipo es: Equilátero"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Su tipo es: Isósceles"
        else:
            return "Su tipo es: Escaleno"


side1 = int(input('Ingrese el primer lado del triangulo: '))
side2 = int(input('Ingrese el segundo lado del triangulo: '))
side3 = int(input('Ingrese el tercer lado del triangulo: '))

triangle1 = Triangle(side1, side2, side3)
print(triangle1.larger_size())
print(triangle1.triangle_type())
