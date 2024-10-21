from vehicle import Vehicle

class Motorbike(Vehicle):
    def __init__(self, manufacturer, model, type):
        super().__init__(manufacturer, model)
        self._type = type

    @property
    def status(self):
        return 'on.' if self._status else 'off.'

    def __str__(self):
        return f'{self._manufacturer} {self._model} - Type: {self._type} - Status: {self.status}'