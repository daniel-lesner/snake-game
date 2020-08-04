import pygame

class SnakeBody:
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("assets/snakeBody.bmp")
        self.image_rect = self.image.get_rect()

        
    def draw(self, foodCount, positionOfSnake):
        if foodCount == 0:
            pass

        else:
            for each_point in range(1, foodCount + 1):
                self.image_rect = positionOfSnake[- each_point - 1]
                self.screen.blit(self.image, self.image_rect)
