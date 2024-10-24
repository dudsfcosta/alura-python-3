from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, manufacturer, model, color):
        super().__init__(manufacturer, model)
        self._color = color

    @property
    def status(self):
        return 'on.' if self._status else 'off.'

    def ligar(self):
        self._status = True