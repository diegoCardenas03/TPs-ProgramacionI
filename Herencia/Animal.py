class Animal:
    def __init__(self, name="", age = 0, genre=""):
        self._name = name
        self._age = age
        self._genre = genre

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_genre(self):
        return self._genre

    def set_name(self, new_name):
        self._name = new_name

    def set_age(self, new_age):
        self._age = new_age

    def set_genre(self, new_genre):
        self._genre = new_genre

    def hacer_sonido(self):
        print("El animal hace un sonido genérico.")


class Perro(Animal):
    def __init__(self, name="", age=0, genre="", raza=""):
        super().__init__(name, age, genre)
        self._raza = raza

    def hacer_sonido(self):
        print("El perro ladra.")

    def informacion(self):
        print(f"Nombre: {self.get_name()}\nEdad: {self.get_age()}\nGenero: {self.get_genre()}")


class Pajaro(Animal):
    def __init__(self, name="", age=0, genre="", especie=""):
        super().__init__(name, age, genre)
        self._especie = especie

    def hacer_sonido(self):
        print("El pajaro canta.")

    def informacion(self):
        print(f"Nombre: {self.get_name()}\nEdad: {self.get_age()}\nGenero: {self.get_genre()}\nRaza: {self._especie}")


class Gato(Animal):

    def __init__(self, name="", age=0, genre="", raza=""):
        super().__init__(name, age, genre)
        self._raza = raza

    def hacer_sonido(self):
        print("El gato maulla.")

    def informacion(self):
        print(f"Nombre: {self.get_name()}\nEdad: {self.get_age()}\nGenero: {self.get_genre()}\nRaza: {self._raza}")


perro1 = Perro("Hulk", 5, "Macho", "Pastor Aleman")
perro1.hacer_sonido()
perro1.informacion()
print("--------------------")
pajaro1 = Pajaro("Plumita", 2, "Hembra", "Gorrión")
pajaro1.hacer_sonido()
pajaro1.informacion()
print("--------------------")
gato1 = Gato("Tiger", 4, "Macho", "Siamés")
gato1.hacer_sonido()
gato1.informacion()
