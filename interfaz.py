import pygame
import sys

class Interfaz:
    def __init__(self, juego):
        pygame.init()
        self.juego = juego
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.SysFont("Arial", 24)
        self.font_small = pygame.font.SysFont("Arial", 18)
        pygame.display.set_caption("Rise of Antares")
    
    def actualizar_pantalla(self):
        self.screen.fill((0, 0, 0))  # Fondo negro
        self.dibujar_info()
        self.dibujar_botones()
        pygame.display.flip()
    
    def dibujar_info(self):
        # Mostrar recursos
        recursos_info = self.juego.recursos.mostrar_info()
        text = self.font.render(recursos_info, True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
        
        # Mostrar planetas y flotas
        y_offset = 50
        for planeta in self.juego.planetarios:
            planeta_info = planeta.mostrar_info()
            text_planeta = self.font_small.render(planeta_info, True, (255, 255, 255))
            self.screen.blit(text_planeta, (10, y_offset))
            y_offset += 30

        # Mostrar flota
        flota_info = self.juego.flota.mostrar_info()
        text_flota = self.font_small.render(flota_info, True, (255, 255, 255))
        self.screen.blit(text_flota, (10, y_offset))
    
    def dibujar_botones(self):
        # Botones básicos para interactuar
        pygame.draw.rect(self.screen, (0, 255, 0), (10, 300, 200, 40))  # Botón "Crear nave"
        pygame.draw.rect(self.screen, (0, 255, 0), (10, 350, 200, 40))  # Botón "Expandir planeta"
        pygame.draw.rect(self.screen, (0, 255, 0), (10, 400, 200, 40))  # Botón "Investigar tecnología"
        
        # Texto de los botones
        self._mostrar_texto_en_boton("Crear nave", (15, 310))
        self._mostrar_texto_en_boton("Expandir planeta", (15, 360))
        self._mostrar_texto_en_boton("Investigar tecnología", (15, 410))
    
    def _mostrar_texto_en_boton(self, texto, posicion):
        text = self.font_small.render(texto, True, (0, 0, 0))
        self.screen.blit(text, posicion)
    
    def ejecutar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 10 <= event.pos[0] <= 210:
                        if 300 <= event.pos[1] <= 340:
                            self.juego.crear_nave()
                        elif 350 <= event.pos[1] <= 390:
                            self.juego.expandir_planeta()
                        elif 400 <= event.pos[1] <= 440:
                            self.juego.investigar_tecnologia()
            self.actualizar_pantalla()
