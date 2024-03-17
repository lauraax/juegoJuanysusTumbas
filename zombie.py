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
        self.rect.x = 800
        self.rect.x = random.randint(0, contenedor[0])
        self.rect.y = 320
        self.vel = 1.5
        self.velocidad_animacion= 8
        self.animacion_contador= 0 
        self.gruñido = pygame.mixer.Sound('sonido/gruñido.mp3')
        self.gruñido.set_volume(0.1)
        self.gruñido.play()
        
                
        print("mimiCoordenadas iniciales del zombie:", self.rect.x, self.rect.y)
    def update(self):
        
        self.animacion_contador += 1
        if self.animacion_contador >= self.velocidad_animacion:
            self.animacion_contador = 0
            self.cont +=1
            if self.cont >= len(self.imagenes):
                self.cont = 0
        self.rect.x -= self.vel
        if self.rect.right <= 0: # hace que los zombies vuelvan a aparecer y no desaparezcan de pantalla 
            self.rect.x = self.contenedor[0]
        #self.cont += 1
        #if self.cont >= len(self.imagenes):
         #   self.cont = 0
        self.image = self.imagenes[self.cont]
    