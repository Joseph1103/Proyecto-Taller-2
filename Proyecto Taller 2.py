# Proyecto de Taller numero 2

import pygame
pygame.init()

# Creacion de ventana
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load("fondo1.png")
# Title and Icon
pygame.display.set_caption("Video Game")
icon = pygame.image.load("icono.png")
pygame.display.set_icon(icon)
running = True
while running:

    screen.fill((0, 0, 0))
#   background_image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    #running = False



