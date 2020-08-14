import pygame

class Snake:
    '''
    This class is creating the snake, draws it on the screen and increments the
    snake's position by 50 pixels depending the which of the arrow key the
    player is presses
    '''
    def __init__(self, game):
        self.game = game
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
        if self.moveRight: self.imageRect.x += self.speed
        elif self.moveLeft: self.imageRect.x -= self.speed
        elif self.moveUp: self.imageRect.y -= self.speed
        else: self.imageRect.y += self.speed

    def checkIfSnakeHitWallOrItself(self):
        if ((self.imageRect.x > 1835 or
            self.imageRect.x < 35 or
            self.imageRect.y > 1015 or
            self.imageRect.y < 65) or 
            (self.imageRect in self.game.listOfBodyCoordinates)
        ):
            self.game.gameOn = False