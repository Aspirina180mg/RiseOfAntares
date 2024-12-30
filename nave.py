class Nave:
    def __init__(self, tipo, ataque, defensa, velocidad):
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
    
    def mostrar_info(self):
        return f"{self.tipo} - Ataque: {self.ataque}, Defensa: {self.defensa}, Velocidad: {self.velocidad}"
