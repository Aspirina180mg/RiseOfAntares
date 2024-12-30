class Flota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.naves = []
    
    def agregar_nave(self, nave):
        self.naves.append(nave)
    
    def eliminar_nave(self, nave):
        self.naves.remove(nave)
    
    def atacar(self, flota_enemiga):
        print(f"{self.nombre} está atacando a {flota_enemiga.nombre}...")
        # Simulación de combate (esto se puede ampliar)
        return "Batalla terminada"
    
    def mostrar_info(self):
        return f"Flota: {self.nombre}, Naves: {len(self.naves)}"
