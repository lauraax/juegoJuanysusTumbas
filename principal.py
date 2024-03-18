import pygame
from pygame.locals import *
import sys
from personaje import Juan
from tumbas import Tumbas
from zombie import Zombie
import util
import random
import os

os.chdir('C:\\Users\\lenovo\\Dropbox\\Mi PC (LAPTOP-DL0G2Q4C)\\Downloads\\JUAN Y SUS TUMBAS\\juegoJuanysusTumbas')
size = width, height = 900, 466
BLACK = (0, 0, 0)

def show_game_over(screen, game_over_sound):
    font = pygame.font.Font(None, 100)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
    screen.blit(game_over_text, text_rect)
    pygame.display.flip() 
    game_over_sound.play() 

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("sonido/maicol.mp3")
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.09)
    
    screen = pygame.display.set_mode(size)
    background_image = pygame.image.load("imagenes/fondojuego.jpg")
    background_rect = background_image.get_rect()
    pygame.display.set_caption("Juego Juan Y Sus Tumbas")

    juan = Juan(size)
    tumbas = []
    zombies = pygame.sprite.Group()

    clock = pygame.time.Clock()

    game_over = False

    game_over_sound = pygame.mixer.Sound('sonido/gameover.mp3')

    while True:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if not game_over:  
            juan.update(size)

            screen.blit(background_image, background_rect)

            if random.randint(0, 100) % 25 == 0 and len(tumbas) < 4:
                tumbas.append(Tumbas(size))


            if random.randint(0, 100) % 25 == 0 and len(zombies) < 3:
                zombies.add(Zombie(size))


            for tumba in tumbas:
                tumba.update() 
                screen.blit(tumba.image, tumba.rect)
                if juan.rect.colliderect(tumba.rect):
                    juan.puntos += 1
                    tumbas.remove(tumba)
            

            for zombie in zombies:
                zombie.update()
                screen.blit(zombie.image, zombie.rect)
                for bullet in juan.bullets:
                    if zombie.rect.colliderect(bullet.rect):
                        juan.bullets.remove(bullet)
                        zombies.remove(zombie)  


            bullets_to_remove = []  
            for bullet in juan.bullets:
                bullet.update()
                if bullet.rect.left > width:
                    bullets_to_remove.append(bullet)  
                else:
                    screen.blit(bullet.image, bullet.rect)
                

                zombies_hit = pygame.sprite.spritecollide(bullet, zombies, True)  
                if zombies_hit:
                    bullets_to_remove.append(bullet) 


            for bullet in bullets_to_remove:
                juan.bullets.remove(bullet)

            for zombie in zombies:
                if juan.rect.colliderect(zombie.rect):
                    juan.vida -= 10
                    zombies.remove(zombie)

            font = pygame.font.Font(None, 45)
            vida_text = font.render("Vida: " + str(juan.vida), 1, (255, 255, 255))
            puntos_text = font.render("Puntos: " + str(juan.puntos), 1, (255, 255, 255))
            screen.blit(vida_text, (20, 20))
            screen.blit(puntos_text, (20, 60))


            screen.blit(juan.image, juan.rect)

            if juan.vida <= 0:
                game_over = True
        else:
            show_game_over(screen, game_over_sound) 
        
        pygame.display.flip()

if __name__ == "__main__":
    main()  