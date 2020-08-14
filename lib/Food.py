import pygame
import random

class Food:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.food = pygame.image.load("assets/food.bmp")
        self.foodRect = self.food.get_rect()
        self.foodCount = 0
        self.highScore = 0


    def drawOnScreen(self):
        self.screen.blit(self.food, self.foodRect)        
        

    def spanFood(self):
        # While loop to make sure food does not span inside snake or it's body
        while True:
            self.foodRect.x = random.randrange(85, 1786, 50)
            self.foodRect.y = random.randrange(115, 966, 50)
            if self.foodRect not in self.game.snakePosition : break


    def increaseFoodCount(self):
        if self.highScore <= self.foodCount: self.highScore += 1
        self.foodCount += 1

