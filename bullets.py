import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, pos, vel):
        super().__init__()
        self.vel = vel
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        
    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]
