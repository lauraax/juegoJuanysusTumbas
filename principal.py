import pygame 
from pygame.locals import *
import sys

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

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, background_rect) 
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    main()