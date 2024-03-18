import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, pos, vel, contenedor):
        super().__init__()
        self.vel = vel
        self.image = pygame.image.load("imagenes/bullet.png")
        
        self.rect = self.image.get_rect(center=pos)
        
    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]
