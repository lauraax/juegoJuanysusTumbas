import pygame
from pygame.sprite import Sprite
class Mano(Sprite):
    def __init__(self, posicion):
        super().__init__()
        self.image = pygame.image.load('imagenes/fantasma.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer >= 180:  # 180 frames = 3 segundos a 60 fps
            self.kill()
