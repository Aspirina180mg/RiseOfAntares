class Planeta:
    def __init__(self, nombre, recursos, naves=None):
        self.nombre = nombre
        self.recursos = recursos  # Diccionario de recursos (ej. {'dinero': 1000, 'minerales': 500})
        self.naves = naves if naves else []  # Lista de naves asignadas a este planeta
    
    def agregar_nave(self, nave):
        self.naves.append(nave)
    
    def eliminar_nave(self, nave):
        self.naves.remove(nave)
    
    def mostrar_info(self):
        return f"Planeta: {self.nombre}, Recursos: {self.recursos}, Naves: {len(self.naves)}"
