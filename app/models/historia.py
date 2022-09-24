class Detalle:
    def __init__(self, description, duration, start,stop):
        self.description = description
        self.duration = duration
        self.start = start
        self.stop = stop
class Detalles:
    def __init__(self):
        self.detalles = []
        # Seeders

    def listarHistorial(self):
        return self.detalles

    def listarHistorialJSON(self):
        lista =[]
        for lista in self.detalles:
            lista.append({
            'description': item.description,
            'duration': item.duration,
            'start': item.start,
            'stop': item.stop,
            })
        return lista
