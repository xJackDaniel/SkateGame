import pygame
from helpers import screen
from constants import *

class Bar:
    def __init__(self, type, height, width, jump, x, image):
        self.type = type
        self.height = height
        self.width = width
        self.jump = jump
        self.moving = False
        self.x = x
        self.image = pygame.image.load(image)

    def get_type(self):
        """Returns the bar's type"""
        return self.type

    def get_height(self):
        """Returns the bar's height"""
        return self.height

    def get_width(self):
        """Returns the bar's width"""
        return self.width

    def get_jump(self):
        """Returns True/False if the player needs to jump over the bar"""
        return self.jump

    def bar_join(self):
        """Start moving the bar"""
        if not self.moving:
            self.moving = True
            while(self.x != -100):
                self.x -= 20
            self.moving = False
            self.x = RAILING_START_X + 100

    def create_bar(self):
        """Creates the bar out of the screen"""
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        screen.blit(self.image, (self.x, RAILING_Y))

