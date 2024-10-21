class Vehicle:
    def __init__(self, manufacturer, model):
        self._manufacturer = manufacturer
        self._model = model
        self._status = False

    def __str__(self):
        return f'{self._manufacturer} {self._model} - Status: {self.status}'