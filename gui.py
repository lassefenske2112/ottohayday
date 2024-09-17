import pygame
from pygame import *
from datetime import datetime

class GUI:

    def __init__(self, coins, employees, rating, buildings, time, level):
        self.coins = coins
        self.employees = employees
        self.rating = rating
        self.buildings = buildings
        self.time = time
        self.level = level

    def draw_labels(self, coins, employees):
        # Texte rendern
        coins_text = pygame.font.render(f"Coins: {self.coins}", True, black)
        mitarbeiter_text = pygame.font.render(f"Mitarbeiter: {self.employees}", True, black)

        # Positionen berechnen
        coins_rect = coins_text.get_rect(topright=(width - 10, 10))
        mitarbeiter_rect = mitarbeiter_text.get_rect(topright=(width - 10, 50))

        # Texte zeichnen
        screen.blit(coins_text, coins_rect)
        screen.blit(mitarbeiter_text, mitarbeiter_rect)


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
