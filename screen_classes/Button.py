import pygame
from constants import*
from helpers import*

class Button:
    def __init__(self, style, screen, text, id):
        self.style = style
        self.screen = screen
        self.text = text
        self.id = id
        self.pause_img = pygame.image.load("images/buttons/Pause.png")
        self.heart_img = pygame.image.load("images/backgrounds/Heart.png")


    def get_style(self):
        """Returns the button's style"""
        return self.style

    def get_screen(self):
        """Returns the screen to which the button moves"""
        return self.screen

    def get_text(self):
        """Returns the text on the button"""
        return self.text

    def get_id(self):
        """Returns the button's id"""
        return self.id

    def display_button(self):
        self.pause_img = pygame.transform.scale(self.pause_img, (PAUSE_WIDTH, PAUSE_HEIGHT))
        screen.blit(self.pause_img, (PAUSE_X_POS, PAUSE_Y_POS))

    def display_heart(self):
        self.heart_img = pygame.transform.scale(self.heart_img, (HEART_WIDTH, HEART_HEIGHT))
        screen.blit(self.heart_img, (HEART_X_POS_1, HEART_Y_POS))

