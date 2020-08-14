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
        screen, thus, it allows us to control the snake's speed
        '''
        self.clock = pygame.time.Clock()
        self.time_delay = 10
        

        ## Initialize the game screen on FullScreen Mode
        self.screen = pygame.display.set_mode(
            (0, 0), 
            pygame.FULLSCREEN
        )
        
        
        ## Create an instance of each class used for this game       
        self.settings = Settings(self)
        self.snake = Snake(self)
        self.snakeBody = SnakeBody(self)
        self.food = Food(self)

        
        ## Define flags and other variables 
        self.screenRect = self.screen.get_rect()
        self.gameOn = True
        self.snakePosition = [self.screenRect.center]
        
        
    def playGame(self):
        while True:
            # Loop of the game
            self._playMusic()
            self._resetGame()
            self.food.spanFood()

            while self.gameOn:
                # Loop for the actual game
                print(self.food.highScore)
                self._checkEvents()
                self.snake.moveSnake()
                self._createListWithFoodAndSnakeCoordinates()
                self._checkIfSnakeAteFood()
                self.snake.checkIfSnakeHitWallOrItself()
                self._updateScreen()
                
            while not self.gameOn:
                # Loop of menu screen
                self._stopMusic()
                self._updateScreen()
                self._checkEvents()
  

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

            # Draw the game border and game screen play
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

            # Set up the score board and highscore board
            self.scoreBoard = self.settings.font.render(
                f"POINTS: {self.food.foodCount}",
                True, 
                self.settings.textColor
            )
            self.highScoreBoard = self.settings.font.render(
                f"HIGHSCORE: {self.food.highScore}",
                True, 
                self.settings.textColor
            )            

            self.screen.blit(self.scoreBoard, (10, 10))
            self.screen.blit(self.highScoreBoard, (
                1910 - self.highScoreBoard.get_rect()[2], 10
            ))
            self.snake.drawOnScreen()
            self.food.drawOnScreen()
            self.snakeBody.drawOnScreen(self.food.foodCount, self.snakePosition)

        else:
            self.screen.fill((self.settings.menuBackgroundColor))
            self.menuText = self.settings.font.render(
                f"You lost! Your last score was {self.food.foodCount} " 
                f" and your highest score is {self.food.highScore}."
                "Press R to restart or Q to quit!",
                True,
                self.settings.textColor
            )
            self.menuTextRect = (
                self.screenRect.center[0] - self.menuText.get_rect()[2] / 2,
                self.screenRect.center[1]
            )
            self.screen.blit(self.menuText, self.menuTextRect)

        self.screen.blit(self.settings.title, self.settings.titleRect)
        pygame.display.flip()


    def _checkIfSnakeAteFood(self):
        if (self.snake.imageRect.x in range(
            self.food.foodRect.x - 49, 
            self.food.foodRect.x + 50
            ) and 
            self.snake.imageRect.y in range(
                self.food.foodRect.y - 49,
                self.food.foodRect.y + 50
            )
        ):
            self.food.spanFood()
            self.food.increaseFoodCount()


    def _createListWithFoodAndSnakeCoordinates(self):
        ''' 
            This method is creating a list with the most recent snake head
        coordinates. Using this list, we will know what will be the coordinates
        of the snake's body, which will help us to render the whole snake on
        the screen
        '''
        self.snakePosition.append(self.snake.imageRect[:])
        if self.food.foodCount > 0:
            self.snakePosition = self.snakePosition[-self.food.foodCount - 2:]
        else:
            self.snakePosition = self.snakePosition[-2:]
        self.listOfBodyCoordinates = self.snakePosition[
            -self.food.foodCount - 1: -1
        ]


    def _resetGame(self):
        self.gameOn = self.snake.moveRight = True
        self.snake.moveLeft = self.snake.moveUp = self.snake.moveDown = False
        self.food.foodCount = 0
        self.snakePosition = [self.screenRect.center]
        self.snake.imageRect.center = self.screenRect.center
        self.food.foodRect.x = random.randrange(85, 1786, 50)
        self.food.foodRect.y = random.randrange(115, 966, 50)


    def _playMusic(self):
        pygame.mixer.music.play(-1, 0.0)

    
    def _stopMusic(self):
        pygame.mixer.music.stop()
        

while __name__ == "__main__":
    myGame = Game()
    myGame.playGame()