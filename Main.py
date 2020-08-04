## Import libraries used for the game
import pygame
import sys
import random


## Import classes created
from Settings import Settings
from lib.Snake import Snake
from lib.Food import Food
from lib.SnakeBody import SnakeBody


class Game:
    def __init__(self):
        pygame.init()


        ## Set the time clock and delay
        ''' 
        The time delay creates the lag with which the snake moves on the
        screen, thus, it controls the snake's speed
        '''
        self.clock = pygame.time.Clock()
        self.time_delay = 15
        

        ## Initialize the game screens on FullScreen Mode
        self.screen = self.screen2 = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)
        
        
        ## Create an instance of each class used for the game       
        self.settings = Settings()
        self.snake = Snake(self)
        self.food = Food(self)
        self.snakeBody = SnakeBody(self)
        
        
        ## Initialise other settings such as screen font or music
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        pygame.display.set_caption(self.settings.gameCaption)
        pygame.mixer.music.load("assets/firstSong.wav")
        pygame.mixer.music.play(-1, 0.0)
        
        
        ## Define flags and other variables 
        self.screen_rect = self.screen.get_rect()
        self.x = True
        self.y = False
        self.trigger = 0
        self.positionOfSnake = []
        
        
    def playGame(self):
        
        while True:
            # Set up the game loop
            while self.x == True:
                self._reset_all_game_variables()
                self._check_events()
                self.snake.update_snake_position()
                self.positionOfSnake.append(self.snake.imageRect[:])
                self.list_of_all_snakes_positions=self.positionOfSnake[-self.food.foodCount:-1]
                
                
                if (self.snake.imageRect.x in range(self.food.foodRect.x-49, self.food.foodRect.x+50) and
                    self.snake.imageRect.y in range(self.food.foodRect.y-49, self.food.foodRect.y+50)):
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
        if (self.snake.imageRect.x>1835 or
            self.snake.imageRect.x<35 or
            self.snake.imageRect.y>1015 or
            self.snake.imageRect.y<65):
            self.x=False
            self.y=True

    def _check_collision_between_snakes(self):
        if (self.snake.imageRect in self.list_of_all_snakes_positions
            and self.food.foodCount > 0):
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
        
        self.screen.fill(self.settings.backgroundColor)
        pygame.draw.line(self.screen, (0,0,0), (35,65), (1885,65), 2)
        pygame.draw.line(self.screen, (0,0,0), (35,1065), (1885,1065), 2)
        pygame.draw.line(self.screen, (0,0,0), (35,65), (35,1065), 2)
        pygame.draw.line(self.screen, (0,0,0), (1885,65), (1885,1065), 2)
        self.snake.blitme()
        
        self.food.blitme()
        
        self.snakeBody.draw(self.food.foodCount, self.positionOfSnake)
        
        pygame.display.flip()
        
    def _open_game_over_screen(self):
        self.screen2.fill((self.settings.menuBackgroundColor))
        self.menuText = self.font.render(
            f"You lost! Your score was {self.food.foodCount}! " 
            "Press R to restart or Q to quit",True,self.settings.textColor)
        self.menuTextRect = (self.screen_rect.center[0] - self.menuText.get_rect()[2] / 2, self.screen_rect.center[1])
        self.screen2.blit(self.menuText, self.menuTextRect)  
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
            self.positionOfSnake=[]
            self.food.foodCount = 0
            self.snake.imageRect.center=self.snake.screen_rect.center
            self.food.foodRect.x = random.randrange(35, 1836, 50)
            self.food.foodRect.y = random.randrange(65, 1016, 50)
            self.trigger=0
            self.time_delay=15

while __name__ == "__main__":
    my_game = Game()
    my_game.playGame()