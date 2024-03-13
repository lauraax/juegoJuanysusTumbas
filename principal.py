import pygame 
from pygame.locals import *
import sys
from personaje import *
size = width, height = 900, 466

screen = pygame.display.set_mode(size)

def main():
    
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("sonido/musica fondo.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.09)
    
    background_image = pygame.image.load("imagenes/fondojuego.jpg")
    background_rect = background_image.get_rect()
    pygame.display.set_caption( "Juan" )
    juan = Juan(size)
    while 1:
        juan.update(size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, background_rect) 
        for bullet in juan.bullets:
            bullet.update()
            if bullet.alcance == 0:
                juan.bullets.remove(bullet)
            screen.blit(bullet.image, bullet.rect)

        screen.blit(juan.image, juan.rect)   
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    main()