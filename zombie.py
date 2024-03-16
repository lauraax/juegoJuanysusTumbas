import pygame
from pygame.sprite import Sprite
from pygame import *
import util


class Zombie(Sprite):
    def __init__(self,contenedor):
        
        super().__init__()
        self.imagenes = [util.cargar_imagen('imagenes/Zombie0.png'),
                                        util.cargar_imagen('imagenes/Zombie1.png'),
                                        util.cargar_imagen('imagenes/Zombie2.png'),
                                        util.cargar_imagen('imagenes/Zombie3.png'),
                                        util.cargar_imagen('imagenes/Zombie4.png'),
                                        util.cargar_imagen('imagenes/Zombie5.png'),
                                        util.cargar_imagen('imagenes/Zombie6.png'),
                                        util.cargar_imagen('imagenes/Zombie7.png')]
        
        self.cont = 0
        self.sentido = 0
        self.image = self.imagenes[self.sentido]
        self.contenedor = contenedor
        self.rect = self.image.get_rect()
        self.rect.x = contenedor[0]
        self.rect.y = contenedor[1]
        self.vel = 2
        self.caminar = pygame.mixer.Sound('sonido/gruñido.mp3')
        self.caminar.set_volume(2)
        
        print("Coordenadas iniciales del zombie:", self.rect.x, self.rect.y)
    def update(self):
        self.rect.x -= self.vel
        self.cont += 1
        if self.cont >= len(self.imagenes):
            self.cont = 0
        self.image = self.imagenes[self.cont]
   