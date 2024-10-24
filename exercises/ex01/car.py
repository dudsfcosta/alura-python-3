from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, manufacturer, model, doors):
        super().__init__(manufacturer, model)
        self._doors = doors

    @property
    def status(self):
        return 'on.' if self._status else 'off.'

    def __str__(self):
        return f'{self._manufacturer} {self._model} - Doors: {self._doors} - Status: {self._status}'