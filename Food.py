import pygame
import random
import sys

class Food:
    def __init__(self,game):
        self.screen=game.screen
        self.screen_rect=game.screen.get_rect()
        
        self.food=pygame.image.load("Pictures/food.bmp")
        self.food_rect=self.food.get_rect()
        
        self.food_rect.x=random.randrange(35,1835,50)
        self.food_rect.y=random.randrange(65,1015,50)
        self.points=0
        
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        
        
        
    def blitme(self):
        self.screen.blit(self.food,self.food_rect)
        
    def blitme2(self):
        self.text_surface=self.font.render(f"    You have {self.points} points!     SNAKE ULTRA RELOADED",True,(0,0,0))
        self.screen.blit(self.text_surface, self.screen.get_rect().midtop)        
        
    def food_eaten(self):
        self.points+=1
        self.food_rect.x=random.randrange(35,1834,50)
        self.food_rect.y=random.randrange(65,1014,50)
        self.blitme()