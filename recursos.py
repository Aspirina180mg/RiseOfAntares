class Recursos:
    def __init__(self):
        self.dinero = 1000
        self.trabajadores = 10
    
    def mostrar_info(self):
        return f"Dinero: {self.dinero}, Trabajadores: {self.trabajadores}"
    
    def gastar(self, cantidad):
        if self.dinero >= cantidad:
            self.dinero -= cantidad
            return True
        return False
    
    def ganar(self, cantidad):
        self.dinero += cantidad
