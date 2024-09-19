class EventoNoCanonico:
    def __init__(self, id, año, nombre, muestra, descripcion):
        self.id =id
        self.año = año
        self.nombre = nombre
        self.muestra = muestra  # Ahora es un arreglo
        self.descripcion = descripcion

    def __str__(self):
        # Podemos iterar sobre la muestra para mostrar todos los valores
        muestra_str = ', '.join(map(str, self.muestra))
        return f'{self.año} {self.nombre} ({muestra_str}) {self.descripcion}'

