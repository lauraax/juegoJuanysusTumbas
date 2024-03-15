import pygame
from pygame.sprite import Sprite
from pygame import *
import util


class Zombie(Sprite):
    def __init__(self):
        self.imagenes = [util.cargar_imagen('imagenes/Zombie0.png'),
                                        util.cargar_imagen('imagenes/Zombie1.png'),
                                        util.cargar_imagen('imagenes/Zombie2.png'),
                                        util.cargar_imagen('imagenes/Zombie3.png'),
                                        util.cargar_imagen('imagenes/Zombie4.png')]
        self.cont = 0
        self.image = self.imagenes[self.cont]
        self.rect = self.image.get_rect()
        self.rect.move_ip(10, 325)
        self.vel = (2,3)
        self.vida = 100
        self.caminar = pygame.mixer.Sound('sonido/caminar.mp3')
        self.caminar.set_volume(0.1)
        
    def update(self,size):

        self.caminar.play()
        self.rect.x = (self.rect.x - self.vel[0]) % size[0]
        self.cont = (self.cont + 1) % 4
        self.image = self.imagenes[self.cont]
    
        self.caminar.play()
        self.cont = (self.cont + 1) % 4
        self.image = self.imagenes[self.cont]
        self.rect.x = (self.rect.x + self.vel[0]) % size[0]
