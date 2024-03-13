import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Juan(Sprite):
    def __init__(self):
        self.imagenes = [util.cargar_imagen('imagenes/p0.png'),
                                        util.cargar_imagen('imagenes/p1.png'),
                                        util.cargar_imagen('imagenes/p2.png'),
                                        util.cargar_imagen('imagenes/p3.png'),
                                        util.cargar_imagen('imagenes/p4.png')]
        self.cont = 0
        self.image = self.imagenes[self.cont]
        self.rect = self.image.get_rect()
        self.rect.move_ip(10, 325)
        self.vel = (2,3)
        self.puntos = 0
        self.vida = 100
        self.bullets=[]
        self.caminar = pygame.mixer.Sound('sonido/caminar.mp3')
        self.caminar.set_volume(0.1)
        
    def update(self,size):
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            self.caminar.play()
            self.rect.x = (self.rect.x - self.vel[0]) % size[0]
            self.cont = (self.cont + 1) % 4
            self.image = self.imagenes[self.cont]
        if teclas[K_RIGHT]:
            self.caminar.play()
            self.cont = (self.cont + 1) % 4
            self.image = self.imagenes[self.cont]
            self.rect.x = (self.rect.x + self.vel[0]) % size[0]