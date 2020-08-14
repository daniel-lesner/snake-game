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

            if event.type == pygame.MOUSEBUTTONDOWN and not self.gameOn:
                mouse = pygame.mouse.get_pos()

                # Respond to click press on NEW GAME button
                if (
                    mouse[0] in self.settings.newGameButtonXRange and 
                    mouse[1] in self.settings.newGameButtonYRange
                ): self.gameOn = True

                # Respond to click press on QUIT button
                if (
                    mouse[0] in self.settings.quitButtonXRange and 
                    mouse[1]in self.settings.quitButtonYRange
                ): sys.exit()         


    def _updateScreen(self):
        if self.gameOn:
            self.screen.fill(self.settings.backgroundColor)

            # Draw the game border and game screen
            pygame.draw.rect(
                self.screen,
                self.settings.gameBackgroundColor,
                self.settings.rectangleRect,
                0
            )
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                self.settings.rectangleRect,
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

            # Define the rect for highscore and score boards
            self.highScoreBoardRect = self.highScoreBoard.get_rect()
            self.scoreBoardRect = self.scoreBoard.get_rect()

            # Define the coordinates of the highscore board
            self.highScoreBoardCoord = (1910 - self.highScoreBoardRect[2], 10)

            # Draw all elements on screen
            self.screen.blit(self.scoreBoard, self.settings.scoreBoardCoord)
            self.screen.blit(self.highScoreBoard, self.highScoreBoardCoord)
            self.snake.drawOnScreen()
            self.food.drawOnScreen()
            self.snakeBody.drawOnScreen(self.food.foodCount, self.snakePosition)

        else:
            self.screen.fill((self.settings.menuBackgroundColor))

            # Create menu text item and it's size and coordinate variables
            self.menuText = self.settings.font.render(
                f"You lost! Your last score was {self.food.foodCount} " 
                f" and your highest score is {self.food.highScore}.",
                True,
                self.settings.textColor
            )
            self.menuTextRect = self.menuText.get_rect()
            self.menuTextCoord = (
                self.screenRect.center[0] - self.menuTextRect[2] / 2,
                self.screenRect[3] / 3
            )

            # Draw elements on screen
            self.screen.blit(
                self.settings.quitButton,
                self.settings.quitButtonCoord
            )
            self.screen.blit(
                self.settings.newGameButton,
                self.settings.newGameButtonCoord
            )
            self.screen.blit(self.menuText, self.menuTextCoord)

        self.screen.blit(self.settings.title, self.settings.titleCoord)
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
        else: self.snakePosition = self.snakePosition[-2:]

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