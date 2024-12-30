class Tecnologia:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion  # en turnos
    
    def mostrar_info(self):
        return f"Tecnología: {self.nombre}, Duración: {self.duracion} turnos"
