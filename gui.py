import pygame
from datetime import datetime



class GUI:

    coins = 0
    employees = 0
    rating = 0
    buildings = []
    time = datetime.now()
    level = 0

    def __init__(self):
        pass

class Button:
    def createButton(self, pos, size):

        pass

    def __init__(self, posX, posY, width, height):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.pos = (self.posX, self.posY)
        self.size = (self.width, self.height)
        self.createButton(self.pos, self.size)
        self.buttonSurface = pygame.Surface(self.size)
        self.button_rect = pygame.Rect(self.pos, self.size)
