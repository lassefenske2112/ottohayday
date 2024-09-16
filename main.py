import pygame
import sys

#game setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("OTTOmatisch")
clock = pygame.time.Clock()
running = True

button = pygame.Surface((150, 150))
button_rect = pygame.Rect(125, 125, 150, 50)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    screen.blit(button, (button_rect.x, button_rect.y))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30) #FPS

pygame.quit()