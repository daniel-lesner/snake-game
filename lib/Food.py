import pygame
import random
import sys

class Food:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.textColor = self.game.settings.textColor
        self.food = pygame.image.load("assets/food.bmp")
        self.foodRect = self.food.get_rect()
        self.foodRect.x = random.randrange(35, 1836, 50)
        self.foodRect.y = random.randrange(65, 1016, 50)
        self.foodCount = 0


    def blitme(self):
        self.text1 = self.font.render("PYTHON SNAKE", True, self.textColor)
        self.text2 = self.font.render(f"POINTS: {self.foodCount}",
            True, self.textColor)

        self.text1Rect = (
            self.screen.get_rect().midtop[0] - self.text1.get_rect()[2] / 2,
            10)

        self.screen.blit(self.text1, self.text1Rect)
        self.screen.blit(self.text2, (10, 10))
        self.screen.blit(self.food, self.foodRect)        
        

    def food_eaten(self):
        self.foodCount += 1
        self.foodRect.x = random.randrange(35, 1836, 50)
        self.foodRect.y = random.randrange(65, 1016, 50)