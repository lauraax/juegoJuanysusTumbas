import pygame
from pygame.sprite import Sprite
import util

class Zombie(Sprite):
    def __init__(self, contenedor):
        super().__init__()
        self.contenedor = contenedor
        self.imagenes = [
            util.cargar_imagen('imagenes/Z0.png'),
            util.cargar_imagen('imagenes/Z1.png'),
            util.cargar_imagen('imagenes/Z2.png'),
            util.cargar_imagen('imagenes/Z3.png'),
            util.cargar_imagen('imagenes/Z4.png'),
            util.cargar_imagen('imagenes/Z5.png'),
            util.cargar_imagen('imagenes/Z6.png'),
            util.cargar_imagen('imagenes/Z7.png')
        ]
        self.cont = 0
        self.image = self.imagenes[self.cont]
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 320
        self.vel = 3.5
        self.velocidad_animacion = 8
        self.animacion_contador = 0 
        self.gruñido = pygame.mixer.Sound('sonido/gruñido.mp3')
        self.gruñido.set_volume(0.05)
        self.gruñido.play()

    def morir(self):
        self.image = pygame.image.load('imagenes/Zmuerto0.png')
    

    def update(self):
        self.animacion_contador += 1
        if self.animacion_contador >= self.velocidad_animacion:
            self.animacion_contador = 0
            self.cont += 1
            if self.cont >= len(self.imagenes):
                self.cont = 0
        self.rect.x -= self.vel
        if self.rect.right <= 0:
            self.rect.x = self.contenedor[0]
        self.image = self.imagenes[self.cont]

def main():
    pygame.init()
    pygame.mixer.init()



