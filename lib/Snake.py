import pygame

class Snake:
    def __init__(self, game):
        self.screen = game.screen
        self.screenRect = game.screen.get_rect()
        self.image = pygame.image.load("assets/snake.bmp")
        self.imageRect = self.image.get_rect()
        self.imageRect.center = self.screenRect.center  
        self.moveRight = True
        self.moveLeft = self.moveUp = self.moveDown = False        
        self.speed=50
        
         
    def drawOnScreen(self):
        self.screen.blit(self.image, self.imageRect)
        
        
    def moveSnake(self):
        if self.moveRight:
            self.imageRect.x += self.speed
        elif self.moveLeft:
            self.imageRect.x -= self.speed
        elif self.moveUp:
            self.imageRect.y -= self.speed
        else:
            self.imageRect.y += self.speed