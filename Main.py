import pygame
import sys
import random

from Settings import Settings
from lib.Snake import Snake
from lib.Food import Food
from lib.Body import Body


class Game:
    def __init__(self):
        '''Initialize the game'''
        pygame.init()
        
        '''Set the time clock and delay'''
        self.clock=pygame.time.Clock()
        self.time_delay=15
        

        
        
        '''Initialize the main screen'''
        self.screen=pygame.display.set_mode((0,0),
                                            pygame.FULLSCREEN)
        self.screen2=pygame.display.set_mode((0,0),
                                             pygame.FULLSCREEN)
        
        
        '''Import other classes'''        
        self.settings=Settings()
        self.snake=Snake(self)
        self.food=Food(self)
        self.body=Body(self)
        
        
        '''Initialise other settings such as screen font or music'''
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.font2 = pygame.font.Font(pygame.font.get_default_font(), 36)
        pygame.display.set_caption(self.settings.caption)
        pygame.mixer.music.load("assets/firstSong.wav")
        pygame.mixer.music.play(-1,0.0)
        
        
        '''Set other working variables'''
        self.screen_rect=self.screen.get_rect()
        self.x=True
        self.y=False
        self.trigger=0
        self.list_of_snake_position=[]
        
        
    def play(self):
        
        while True:
            
            '''Set up the main loop of the game'''
            
            # Loop of playing game
            while self.x==True:
                self._reset_all_game_variables()
                
                self._check_events()
                
                self.snake.update_snake_position()
                
                self.list_of_snake_position.append(self.snake.image_rect[:])
                
                self.list_of_all_snakes_positions=self.list_of_snake_position[-self.food.points:-1]
                
                
                if (self.snake.image_rect.x in range(self.food.food_rect.x-50,self.food.food_rect.x+50) and
                    self.snake.image_rect.y in range(self.food.food_rect.y-50,self.food.food_rect.y+50)):
                    self.food.food_eaten()
                    
                self._check_if_snake_hit_wall()
                
                self._check_collision_between_snakes()
                
                self._update_screen()
                
            # Loop of stage between games
            while self.y==True:
                self._open_game_over_screen()
                self._check_new_events()
                self._reseset_settings_for_new_game()
  
    
    def _check_if_snake_hit_wall(self):
        if (self.snake.image_rect.x>1835 or
            self.snake.image_rect.x<35 or
            self.snake.image_rect.y>1015 or
            self.snake.image_rect.y<65):
            self.x=False
            self.y=True

    def _check_collision_between_snakes(self):
        if (self.snake.image_rect in self.list_of_all_snakes_positions
            and self.food.points>0):
            self.x=False
            self.y=True

    
    
    def _check_events(self):
        self.clock.tick(self.time_delay)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
                
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if not self.snake.moving_right:
                        self.snake.moving_left=True
                        self.snake.moving_right=False
                        self.snake.moving_up=False
                        self.snake.moving_down=False
                elif event.key==pygame.K_RIGHT:
                    if not self.snake.moving_left:                    
                        self.snake.moving_left=False
                        self.snake.moving_right=True
                        self.snake.moving_up=False
                        self.snake.moving_down=False
                elif event.key==pygame.K_UP:
                    if not self.snake.moving_down:
                        self.snake.moving_left=False
                        self.snake.moving_right=False
                        self.snake.moving_up=True
                        self.snake.moving_down=False
                elif event.key==pygame.K_DOWN:
                    if not self.snake.moving_up:
                        self.snake.moving_left=False
                        self.snake.moving_right=False
                        self.snake.moving_up=False
                        self.snake.moving_down=True
                elif event.key==pygame.K_q:
                    sys.exit()

                    
    def _update_screen(self):
        
        self.screen.fill(self.settings.bg_color)
        pygame.draw.line(self.screen, (0,0,0), (35,65), (1885,65), 2)
        pygame.draw.line(self.screen, (0,0,0), (35,1065), (1885,1065), 2)
        pygame.draw.line(self.screen, (0,0,0), (35,65), (35,1065), 2)
        pygame.draw.line(self.screen, (0,0,0), (1885,65), (1885,1065), 2)
        self.snake.blitme()
        
        self.food.blitme()
        self.food.blitme2()
        
        self.body.blitme(self.food.points,self.list_of_snake_position)
        
        pygame.display.flip()
        
    def _open_game_over_screen(self):
        self.screen2.fill((0,0,0))
        self.text2_surface=self.font2.render(f"You lost! Your score was {self.food.points}! Press R to restart or Q to quit",True,(250,250,250))
        self.screen2.blit(self.text2_surface, self.screen2.get_rect().midleft)  
        pygame.display.flip()
        
        
    def _reseset_settings_for_new_game(self):
        if self.trigger==1:
            self.y=False
            self.x=True
            self.screen2.set_alpha(255)
            self._update_screen()            
        
    def _check_new_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    sys.exit()
                elif event.key==pygame.K_r:
                    self.trigger=1
                    
    def _reset_all_game_variables(self):
        if self.trigger==1:
            self.list_of_all_snakes_positions=[]
            self.list_of_snake_position=[]
            self.food.points=0
            self.snake.image_rect.center=self.snake.screen_rect.center
            self.food.food_rect.x=random.randint(20,1900)
            self.food.food_rect.y=random.randint(70,1060)
            self.trigger=0
            self.time_delay=15

while __name__=="__main__":
    my_game=Game()
    my_game.play()