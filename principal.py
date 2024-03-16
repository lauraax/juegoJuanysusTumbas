import pygame, random 
from pygame.locals import *
import sys
from personaje import *
from tumbas import *
from random import randint
from zombie import Zombie

size = width, height = 900, 466

screen = pygame.display.set_mode(size)

def main():
    
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("sonido/maicol.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.09)
    
    background_image = pygame.image.load("imagenes/fondojuego.jpg")
    background_rect = background_image.get_rect()
    pygame.display.set_caption( "Juego Juan Y Sus Tumbas" )

    juan = Juan(size)
    tumbas = []
    zombies = []
    while 1:
        juan.update(size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.font.init()
        screen.blit(background_image, background_rect) 
        fuente = pygame.font.Font(None,45)
        texto_puntos = fuente.render("Puntos: "+str(juan.puntos),1,(250,250,250))
        texto_vida = fuente.render("Vida: "+str(juan.vida),1,(250,250,250))  
        fuente_go = pygame.font.Font(None,100)
        texto_fin = fuente_go.render("FIN DEL JUEGO",1,(250,0,0))

        if random.randint(0,100) % 25 == 0 and len(tumbas) < 4:
            tumbas.append(Tumbas(size))
            
        if random.randint(0,100) % 25 == 0 and len(zombies) < 3:
            zombies.append(Zombie(size))
        
        for tumba in tumbas:
            tumba.update() 
            screen.blit(tumba.image, tumba.rect)
            if juan.rect.colliderect(tumba.rect):
                juan.puntos += 5
                for tumba in tumbas:
                    screen.blit(tumba.image, tumba.rect)
                    tumbas.remove(tumba)
        
        for zombie in zombies:
            zombie.update()
            screen.blit(zombie.image, zombie.rect)
          
        for bullet in juan.bullets:
            bullet.update()
            if bullet.alcance == 0:
                juan.bullets.remove(bullet)
            screen.blit(bullet.image, bullet.rect)

            
        if juan.vida > 0:
            screen.blit(texto_vida,(600,50))
            screen.blit(texto_puntos,(100,50))

        screen.blit(juan.image, juan.rect)   
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    main()