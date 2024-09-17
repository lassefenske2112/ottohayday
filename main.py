import pygame
from pygame import MOUSEBUTTONDOWN

from gui import *
import sys

from ottomatisch.saveState import saveStats

#game setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("OTTOmatisch")
clock = pygame.time.Clock()
running = True

testButton = Button(125, 125, 150, 150)
screen.fill("purple")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            if testButton.button_rect.collidepoint(event.pos):
                screen.fill("white")

    # fill the screen with a color to wipe away anything from last frame
    gui = GUI()
    GUI.draw_labels(safeState.get_coins, )

    screen.blit(testButton.buttonSurface, (testButton.button_rect.x, testButton.button_rect.y))
    # flip() the display to put your work on screen
    #pygame.draw.rect(screen, "black", pygame.Rect(400, 400, 150, 150), 2, 10)
    pygame.display.flip()

    clock.tick(30) #FPS

pygame.quit()