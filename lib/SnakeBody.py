import pygame

class SnakeBody:
    def __init__(self, game):
        self.screen = game.screen
        self.image = pygame.image.load("assets/snakeBody.bmp")
        self.imageRect = self.image.get_rect()

        
    def drawOnScreen(self, foodCount, snakePosition):
        if foodCount > 0:
            for each_point in range(1, foodCount + 1):
                self.imageRect = snakePosition[-each_point - 1]
                self.screen.blit(self.image, self.imageRect)