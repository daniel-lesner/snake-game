import pygame
import random

class Food:
    def __init__(self, game):
        self.screen = game.screen
        self.food = pygame.image.load("assets/food.bmp")
        self.foodRect = self.food.get_rect()
        self.foodRect.x = random.randrange(35, 1836, 50)
        self.foodRect.y = random.randrange(65, 1016, 50)
        self.foodCount = 0


    def drawOnScreen(self):
        self.screen.blit(self.food, self.foodRect)        
        

    def foodEaten(self):
        self.foodCount += 1
        self.foodRect.x = random.randrange(35, 1836, 50)
        self.foodRect.y = random.randrange(65, 1016, 50)