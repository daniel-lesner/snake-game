import pygame

class Settings:
    def __init__(self, game):
        self.screen = game.screen

        # Define background collors
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


        # Set coordinates of game screen elements
        self.titleRect = (
            self.screen.get_rect().midtop[0] - self.title.get_rect()[2] / 2,
            10
        )