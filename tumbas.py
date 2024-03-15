import pygame, random
from pygame.sprite import Sprite 
from random import randint

class Tumbas(Sprite):
    def __init__(self,contenedor):
        self.contenedor = contenedor
        self.image = pygame.image.load("imagenes/tumba.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(random.randint(100,self.contenedor[0]),contenedor[1]/1.47)