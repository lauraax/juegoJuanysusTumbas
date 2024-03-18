import pygame, math
from pygame.sprite import Sprite
from pygame import *

class Bullet(Sprite):
    def __init__(self, pos, vel, cont):
        Sprite.__init__(self)
        self.vel = vel
        self.alcance = 25
        self.contenedor = cont
        self.image = pygame.image.load("imagenes/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0],pos[1])
        

    def update(self):
        self.alcance -= 1
        self.rect = self.rect.move(self.vel)
        self.rect.x = self.rect.x % self.contenedor[0]
        self.rect.y = self.rect.y % self.contenedor[1]
        

