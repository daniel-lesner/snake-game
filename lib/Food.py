import pygame
import random

class Food:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.food = pygame.image.load("assets/food.bmp")
        self.foodRect = self.food.get_rect()
        self.foodCount = 0


    def drawOnScreen(self):
        self.screen.blit(self.food, self.foodRect)        
        

    def spanFood(self):
        # While loop to make sure food does not span inside snake or it's body
        while True:
            self.foodRect.x = random.randrange(35, 1836, 50)
            self.foodRect.y = random.randrange(65, 1016, 50)
            if not (self.foodRect in self.game.snakePosition):
                break


    def increaseFoodCount(self):
        self.foodCount += 1