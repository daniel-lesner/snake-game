import pygame

class Snake:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        
        self.image=pygame.image.load("Pictures/snake.bmp")
        self.image_rect=self.image.get_rect()
        
        self.image_rect.center=self.screen_rect.center
        
        
        self.moving_right=True
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        
        self.speed=50
        
        
        
        
    def blitme(self):
        self.screen.blit(self.image,self.image_rect)
        
        
    def update_snake_position(self):
        if self.moving_right and self.image_rect.right<self.screen_rect.right-34:
            self.image_rect.x+=self.speed
        elif self.moving_left and self.image_rect.left>34:
            self.image_rect.x-=self.speed
        elif self.moving_up and self.image_rect.top>64:
            self.image_rect.y-=self.speed
        elif self.moving_down and self.image_rect.bottom<self.screen_rect.bottom-14:
            self.image_rect.y+=self.speed