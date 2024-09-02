class EventoNoCanonico:
    def __init__(self, año, nombre, caso1, caso2):
        self.año = año
        self.nombre = nombre
        self.caso1 = caso1
        self.caso2 = caso2

    def __str__(self):
        return f'{self.año} {self.nombre} ({self.caso1})'

