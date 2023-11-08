class Person:
    def __init__(self, name=None, age=None, dni=None):
        self._name = name
        self._age = age
        self._dni = dni

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    def show_details(self):
        return f'Persona: [Nombre: {self.name}, Edad: {self.age}, DNI: {self.dni}]'

    def is_older(self):
        return self.age >= 18
