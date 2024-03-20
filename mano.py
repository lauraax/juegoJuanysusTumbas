import pygame
from pygame.sprite import Sprite
import random
from personaje import Juan

class Mano(pygame.sprite.Sprite):
    def _init_(self, contenedor):
        super()._init_()
        self.contenedor = contenedor
        self.image = pygame.imagen.load('imagenes/mano.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, contenedor[0] - self.rect.width)  
        self.rect.y = contenedor[1] - self.rect.height 
        self.vel = random.uniform(0.5, 1.5)  
        self.daño = 10
        
    def update(self):
        self.rect.x += self.vel 
        if self.rect.right <= 0:  
            self.rect.x = self.contenedor[0]

        juan = pygame.sprite.spritecollideany(self, Juan) 
        if juan:  
            juan.recibir_dano(self.dano) 
        if juan and not juan.invencible: 
            juan.ser_alcanzado()