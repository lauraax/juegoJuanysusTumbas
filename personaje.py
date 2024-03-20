import pygame
from pygame.sprite import Sprite
from pygame import *
import util
from bullets import *
class Juan(Sprite):
    def __init__(self,contenedor):
        self.imagenes = [[util.cargar_imagen('imagenes/p0.png'),
                                        util.cargar_imagen('imagenes/p1.png'),
                                        util.cargar_imagen('imagenes/p2.png'),
                                        util.cargar_imagen('imagenes/p3.png'),
                                        util.cargar_imagen('imagenes/p4.png')],
                        [util.cargar_imagen('imagenes/I0.png'),
                                        util.cargar_imagen('imagenes/I1.png'),
                                        util.cargar_imagen('imagenes/I2.png'),
                                        util.cargar_imagen('imagenes/I3.png'),
                                        util.cargar_imagen('imagenes/I4.png')]]
        
        self.cont = 0
        self.sentido = 0
        self.image = self.imagenes[self.sentido][self.cont]
        self.contenedor = contenedor
        self.rect = self.image.get_rect()
        self.rect.move_ip(contenedor[0]/30, contenedor[1]/1.47)
        self.vel = (2,3)
        self.puntos = 0
        self.vida = 100
        self.bullets=[]
        self.caminar = pygame.mixer.Sound('sonido/caminar.mp3')
        self.caminar.set_volume(0.05)
        self.invencible = False
        self.invencible_duration = 2000 
        self.invencible_timer = 0

    def ser_alcanzado(self):
        self.invencible = True
        self.invencible_timer = pygame.time.get_ticks()

    def update(self,size):
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            self.sentido = 1
            self.caminar.play()
            self.rect.x = (self.rect.x - self.vel[0]) % size[0]
            self.cont = (self.cont + 1) % 4
            self.image = self.imagenes[self.sentido][self.cont]
        if teclas[K_RIGHT]:
            self.sentido = 0
            self.caminar.play()
            self.cont = (self.cont + 1) % 4
            self.image = self.imagenes[self.sentido][self.cont]
            self.rect.x = (self.rect.x + self.vel[0]) % size[0]
        if teclas[K_SPACE]:
            self.disparar()
        if self.invencible:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.invencible_timer > self.invencible_duration:
                self.invencible = False   

    def disparar(self):
        
        if self.sentido == 0:
            pos = [self.rect.x + 64, self.rect.y+40]
            vel = [10,0]
        else:
            pos = [self.rect.x, self.rect.y+40]
            vel = [-10,0]
        self.bullets.append(Bullet(pos, vel, self.contenedor)) 
        