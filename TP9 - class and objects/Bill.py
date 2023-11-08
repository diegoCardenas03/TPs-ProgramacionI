class Bill:
    def __init__(self, holder=None, amount=None):
        self._holder = holder
        self._amount = amount

    @property
    def holder(self):
        return self._holder

    @holder.setter
    def holder(self, holder):
        self._holder = holder

    @property
    def amount(self):
        return self._amount

    def show_details(self):
        return f'Cuenta: [Titular: {self.holder}, Cantidad: {self.amount}]'

    def deposit(self, amount):
        if amount > 0:
            self._amount += amount

    def withdraw(self, amount):
        self._amount -= amount
