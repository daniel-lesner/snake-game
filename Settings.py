import pygame
import pyautogui

class Settings:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen

        # Define background colors
        self.backgroundColor = (125,165, 176)
        self.gameBackgroundColor = (165, 175, 125)
        self.menuBackgroundColor = (98, 137, 148)

        # Set up title, caption font and other settings
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.textColor = (75, 84, 77)
        self.title = self.font.render("PYTHON SNAKE", True, self.textColor)
        self.gameCaption = ("SNAKE")

        # Set up music
        pygame.display.set_caption(self.gameCaption)
        pygame.mixer.music.load("assets/firstSong.wav")

        # Load buttons images
        self.newGameButton = pygame.image.load("assets/newGameButton.png")
        self.quitButton = pygame.image.load("assets/quitButton.png")
 
        # Create variable of buttons and elements dimensions
        self.screenRect = self.screen.get_rect()
        self.titleRect = self.title.get_rect()
        self.newGameButtonRect = self.newGameButton.get_rect()
        self.quitButtonRect = self.quitButton.get_rect()
        self.rectangleRect = [35, 65, 1850, 1000]  
        
        # Set the coordinates of buttons and elements
        self.titleCoord = (
            self.screenRect.midtop[0] - self.titleRect[2] / 2,
            10
        )

        self.scoreBoardCoord = (10, 10)

        self.newGameButtonCoord = (
            self.screenRect.center[0] - self.newGameButtonRect[2] / 2,
            self.screenRect.center[1] * 4 / 5
            )

        self.quitButtonCoord = (
            self.screenRect.center[0] - self.quitButtonRect[2] / 2,
            self.screenRect.center[1] * 4 / 5 + self.newGameButton.get_rect()[3]
        )   

        # Create variables for buttons X and Y coordinates in order to click them
        self.newGameButtonXRange = range(
            int(self.newGameButtonCoord[0]),
            int(self.newGameButtonCoord[0] + self.newGameButtonRect[2])
        )

        self.newGameButtonYRange = range(
            int(self.newGameButtonCoord[1]),
            int(self.newGameButtonCoord[1] + self.newGameButtonRect[3])
        )

        self.quitButtonXRange = range(
            int(self.quitButtonCoord[0]),
            int(self.quitButtonCoord[0] + self.quitButtonRect[2])
        )

        self.quitButtonYRange = range(
            int(self.quitButtonCoord[1]),
            int(self.quitButtonCoord[1] + self.quitButtonRect[3])
        )