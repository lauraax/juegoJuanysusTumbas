import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, pos, vel,cont):
        super().__init__()
        self.vel = vel
        self.contenedor = cont
        self.image = pygame.image.load("imagenes/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0],pos[1])
        
    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]
    

