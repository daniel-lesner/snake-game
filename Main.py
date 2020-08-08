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
        self.time_delay = 10
        

        ## Initialize the game screen on FullScreen Mode
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)
        
        
        ## Create an instance of each class used for the game       
        self.settings = Settings()
        self.snake = Snake(self)
        self.snakeBody = SnakeBody(self)
        self.food = Food(self)

        
        ## Initialise other settings such as screens font or music
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        pygame.display.set_caption(self.settings.gameCaption)
        pygame.mixer.music.load("assets/firstSong.wav")
        self.title = self.font.render("PYTHON SNAKE", True, self.settings.textColor)
        self.titleRect = (
        self.screen.get_rect().midtop[0] - self.title.get_rect()[2] / 2,
        10)


        ## Define flags and other variables 
        self.screenRect = self.screen.get_rect()
        self.gameOn = True
        self.snakePosition = []
        
        
    def playGame(self):
        
        while True:
            # Loop of the game
            self._playMusic()
            self._resetGame()

            while self.gameOn:
                # Loop for the actual game
                self._checkEvents()
                self.snake.moveSnake()
                self.snakePosition.append(self.snake.imageRect[:])
                self.listWithBodyPosition = self.snakePosition[
                    -self.food.foodCount:-1
                    ]
                self._checkIfAteFood()
                self._checkIfSnakeHitWallOrItself()
                self._updateScreen()
                
            while not self.gameOn:
                # Loop of menu screen
                self._stopMusic()
                self._updateScreen()
                self._checkEvents()
  
    
    def _checkIfSnakeHitWallOrItself(self):
        if ((self.snake.imageRect.x > 1835 or
            self.snake.imageRect.x < 35 or
            self.snake.imageRect.y > 1015 or
            self.snake.imageRect.y < 65) or 
            (self.snake.imageRect in self.listWithBodyPosition
            and self.food.foodCount > 0)):

            self.gameOn = False

    def _checkIfAteFood(self):
        if (self.snake.imageRect.x in range(
            self.food.foodRect.x - 49, 
            self.food.foodRect.x + 50
            ) and self.snake.imageRect.y in range(
                self.food.foodRect.y - 49,
                self.food.foodRect.y + 50
                )):
            self.food.foodEaten()


    def _checkEvents(self):
        if self.gameOn:
            self.clock.tick(self.time_delay)

        for event in pygame.event.get():
                
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q: sys.exit()
                
                elif event.key == pygame.K_r and not self.gameOn:
                    self.gameOn = True

                elif event.key == pygame.K_LEFT and not self.snake.moveRight:
                        self.snake.moveLeft = True
                        self.snake.moveUp = self.snake.moveDown = False
                        break

                elif event.key == pygame.K_RIGHT and not self.snake.moveLeft:          
                        self.snake.moveRight = True
                        self.snake.moveUp = self.snake.moveDown = False
                        break

                elif event.key == pygame.K_UP and not self.snake.moveDown:
                        self.snake.moveUp = True
                        self.snake.moveLeft = self.snake.moveRight = False
                        break

                elif event.key == pygame.K_DOWN and not self.snake.moveUp:
                        self.snake.moveDown = True
                        self.snake.moveLeft = self.snake.moveRight = False
                        break


    def _updateScreen(self):
        if self.gameOn:
            self.screen.fill(self.settings.backgroundColor)
            pygame.draw.rect(
                self.screen,
                self.settings.gameBackgroundColor,
                [35, 65, 1850, 1000],
                0
                )
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                [35, 65, 1850, 1000],
                2
                )
            self.scoreBoard = self.font.render(
                f"POINTS: {self.food.foodCount}",
                True, 
                self.settings.textColor
                )
            self.screen.blit(self.scoreBoard, (10, 10))
            self.snake.drawOnScreen()
            self.food.drawOnScreen()
            self.snakeBody.drawOnScreen(self.food.foodCount, self.snakePosition)

        else:
            self.screen.fill((self.settings.menuBackgroundColor))
            self.menuText = self.font.render(
                f"You lost! Your score was {self.food.foodCount}! " 
                "Press R to restart or Q to quit",
                True,
                self.settings.textColor
                )
            self.menuTextRect = (
                self.screenRect.center[0] - self.menuText.get_rect()[2] / 2,
                self.screenRect.center[1]
                )
            self.screen.blit(self.menuText, self.menuTextRect)  
        self.screen.blit(self.title, self.titleRect)
        pygame.display.flip()
        
        
    def _resetGame(self):
        self.gameOn = self.snake.moveRight = True
        self.snake.moveLeft = self.snake.moveUp = self.snake.moveDown = False
        self.food.foodCount = 0
        self.listWithBodyPosition = self.snakePosition = []
        self.snake.imageRect.center = self.snake.screenRect.center
        self.food.foodRect.x = random.randrange(35, 1836, 50)
        self.food.foodRect.y = random.randrange(65, 1016, 50)


    def _playMusic(self):
        pygame.mixer.music.play(-1, 0.0)

    
    def _stopMusic(self):
        pygame.mixer.music.stop()
        

while __name__ == "__main__":
    my_game = Game()
    my_game.playGame()