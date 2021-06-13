# Proyecto de Taller numero 2

import pygame
pygame.init()

# Creacion de ventana
screen = pygame.display.set_mode([768, 768])
clock = pygame.time.Clock()

done = False
fondo = pygame.image.load("fondo.jpg").convert()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(fondo, [0,0])

    pygame.display.flip()
    clock.tick(60)

#pygame.quit()

