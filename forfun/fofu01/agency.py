from bank import Bank

class Agency(Bank):
    def __init__(self, name, address, number):
        super().__init__(name, address)
        self._number = number