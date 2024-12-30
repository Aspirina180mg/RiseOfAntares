import pygame
import random
import sys

# Inicializamos Pygame
pygame.init()

# Constantes de la ventana
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
COLOR_FONDO = (0, 0, 0)  # Fondo negro

# Fuentes
fuente = pygame.font.SysFont('Arial', 24)

# Colores
COLOR_BLANCO = (255, 255, 255)
COLOR_VERDE = (0, 255, 0)
COLOR_AZUL = (0, 0, 255)
COLOR_ROJO = (255, 0, 0)

class Civilizacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.recursos = {"dinero": 1000, "minerales": 500, "comida": 300, "ciencia": 100}
        self.planetas = []
        self.tecnologias = ["Tecnología Básica"]
        self.flota = []

    def mostrar_info(self):
        return f"{self.nombre} - Dinero: {self.recursos['dinero']} - Minerales: {self.recursos['minerales']} - Ciencia: {self.recursos['ciencia']}"

    def expandir_planeta(self, planeta):
        if self.recursos["minerales"] >= 200:
            self.recursos["minerales"] -= 200
            planeta.expandir()
            print(f"{planeta.nombre} ha sido expandido.")
        else:
            print("No hay suficientes minerales para expandir el planeta.")

    def investigar_tecnologia(self):
        nuevas_tecnologias = ["Escudo Avanzado", "Propulsión Mejorada", "Láser Avanzado"]
        nueva_tecnologia = random.choice(nuevas_tecnologias)
        self.tecnologias.append(nueva_tecnologia)
        print(f"Investigación completada: {nueva_tecnologia}")

    def crear_nave(self, nombre, costo):
        if self.recursos["dinero"] >= costo:
            nave = Nave(nombre)
            self.flota.append(nave)
            self.recursos["dinero"] -= costo
            print(f"Nave creada: {nave.nombre}")
        else:
            print("No tienes suficientes recursos para crear una nave.")

class Planeta:
    def __init__(self, nombre, x, y):
        self.nombre = nombre
        self.recursos = {"minerales": 300, "comida": 150}
        self.expandido = False
        self.x = x
        self.y = y
        self.velocidad_x = random.randint(1, 2)  # Velocidad controlada en el eje X
        self.velocidad_y = random.randint(1, 2)  # Velocidad controlada en el eje Y

    def mostrar_info(self):
        return f"{self.nombre} - Minerales: {self.recursos['minerales']} - Comida: {self.recursos['comida']}"

    def expandir(self):
        self.expandido = True
        self.recursos["minerales"] += 100
        self.recursos["comida"] += 50

    def mover(self):
        """Mover el planeta dentro de los límites de la pantalla."""
        self.x += self.velocidad_x
        self.y += self.velocidad_y

        # Evitar que se mueva fuera de la pantalla en el eje X
        if self.x > ANCHO_VENTANA - 20 or self.x < 20:  # 20 es el radio del planeta
            self.velocidad_x = -self.velocidad_x  # Invertir dirección

        # Evitar que se mueva fuera de la pantalla en el eje Y
        if self.y > ALTO_VENTANA - 20 or self.y < 20:  # 20 es el radio del planeta
            self.velocidad_y = -self.velocidad_y  # Invertir dirección

class Nave:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = 50
        self.defensa = 30
        self.velocidad = 100

    def mostrar_info(self):
        return f"{self.nombre} - Ataque: {self.ataque} - Defensa: {self.defensa} - Velocidad: {self.velocidad}"

class SistemaEstelar:
    def __init__(self, nombre):
        self.nombre = nombre
        self.planetarios = [Planeta(f"Planeta {i}", random.randint(100, 700), random.randint(100, 500)) for i in range(1, 6)]  # Sistema con 5 planetas
    
    def mostrar_info(self):
        return f"Sistema {self.nombre} - {len(self.planetarios)} planetas"

class Batalla:
    def __init__(self, flota_1, flota_2):
        self.flota_1 = flota_1
        self.flota_2 = flota_2
        self.resultado = ""

    def simular(self):
        # Batalla simple por turnos
        fuerza_1 = sum(nave.ataque for nave in self.flota_1)
        fuerza_2 = sum(nave.ataque for nave in self.flota_2)

        if fuerza_1 > fuerza_2:
            self.resultado = "Flota 1 gana"
        elif fuerza_2 > fuerza_1:
            self.resultado = "Flota 2 gana"
        else:
            self.resultado = "Empate"
        
        print(f"Resultado de la batalla: {self.resultado}")

class Juego:
    def __init__(self):
        self.civilizacion = Civilizacion("Humanos")
        self.sistemas = [SistemaEstelar(f"Sistema {i}") for i in range(1, 4)]  # 3 sistemas estelares
        self.turno = 1
        self.civilizaciones_aliadas = []

    def mostrar_estado(self):
        texto_estado = f"Turno {self.turno}\n{self.civilizacion.mostrar_info()}"
        return texto_estado

    def avanzar_turno(self):
        self.turno += 1
        self.civilizacion.recursos["dinero"] += 50
        self.civilizacion.recursos["minerales"] += 100
        self.civilizacion.recursos["comida"] += 20
        print(f"Recursos aumentados: {self.civilizacion.recursos}")

    def explorar_sistema(self, sistema):
        return sistema

    def explorar_galaxia(self, ventana):
        ventana.fill(COLOR_FONDO)
        for sistema in self.sistemas:
            for planeta in sistema.planetarios:
                planeta.mover()  # Actualizar la posición del planeta
                pygame.draw.circle(ventana, COLOR_VERDE, (planeta.x, planeta.y), 20)
                texto = fuente.render(planeta.mostrar_info(), True, COLOR_BLANCO)
                ventana.blit(texto, (planeta.x + 10, planeta.y + 10))  # Mostrar información cerca del planeta
        pygame.display.update()

    def ejecutar(self):
        pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.display.set_caption('Rise of Antares - Juego de Estrategia Espacial')
        
        reloj = pygame.time.Clock()

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        self.avanzar_turno()
                    if evento.key == pygame.K_2:
                        sistema = self.sistemas[0]
                        self.explorar_sistema(sistema)
                    if evento.key == pygame.K_3:
                        self.explorar_galaxia(pantalla)

            pantalla.fill(COLOR_FONDO)

            # Mostrar información en la pantalla
            texto_estado = self.mostrar_estado()
            estado_texto = fuente.render(texto_estado, True, COLOR_BLANCO)
            pantalla.blit(estado_texto, (10, 10))

            # Mostrar galaxia
            self.explorar_galaxia(pantalla)

            pygame.display.update()
            reloj.tick(60)

if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()
