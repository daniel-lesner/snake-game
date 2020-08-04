import pygame

class Body:
    def __init__(self,game):
        self.screen=game.screen
        self.screen_rect=game.screen.get_rect()
        
        self.image=pygame.image.load("assets/snakeBody.bmp")
        self.image_rect=self.image.get_rect()
        
        self.points=game.food.points

        
    def blitme(self,points,list_of_snake_position):
        if points<1:
            pass
        else:
            for each_point in range(1,points+1):
                self.image_rect=list_of_snake_position[-each_point-1]
                self.screen.blit(self.image,self.image_rect)
