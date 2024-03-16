import pygame
from pygame.sprite import Sprite
from pygame import *
import util
import random

class Zombie(Sprite):
    def __init__(self,contenedor):
        
        super().__init__()
        self.imagenes = [util.cargar_imagen('imagenes/Z0.png'),
                                        util.cargar_imagen('imagenes/Z1.png'),
                                        util.cargar_imagen('imagenes/Z2.png'),
                                        util.cargar_imagen('imagenes/Z3.png'),
                                        util.cargar_imagen('imagenes/Z4.png'),
                                        util.cargar_imagen('imagenes/Z5.png'),
                                        util.cargar_imagen('imagenes/Z6.png'),
                                        util.cargar_imagen('imagenes/Z7.png')]
        
        self.cont = 0
        self.sentido = 0
        self.image = self.imagenes[self.sentido]
        self.contenedor = contenedor
        self.rect = self.image.get_rect()
        self.rect.x =random.randint(0, contenedor[0])
        self.rect.y =random.randint(0, contenedor[1])
        self.vel = 0.9
        self.caminar = pygame.mixer.Sound('sonido/gruñido.mp3')
        self.caminar.set_volume(2)
        
        print("mimiCoordenadas iniciales del zombie:", self.rect.x, self.rect.y)
    def update(self):
        self.rect.x -= self.vel
        self.cont += 1
        if self.cont >= len(self.imagenes):
            self.cont = 0
        self.image = self.imagenes[self.cont]
   