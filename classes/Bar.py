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

    def bar_join(self, current_score):
        """Start moving the bar"""
        if self.moving:
            if self.x > -300:
                self.x -= current_score * 0.1
            else:
                self.reset_bar()

    def reset_bar(self):
        """Reset the bar's position"""
        if self.type == RAILING_TYPE:
            self.x = RAILING_START_X
        elif self.type == BIRD_TYPE:
            self.x = BIRD_START_X
        else:
            self.x = STAIRS_START_X
        self.moving = False

    def create_bar(self):
        """Creates the bar out of the screen"""
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if self.type == RAILING_TYPE:
            screen.blit(self.image, (self.x, RAILING_Y))
        elif self.type == BIRD_TYPE:
            screen.blit(self.image, (self.x, BIRD_Y))
        else:
            screen.blit(self.image, (self.x, STAIRS_Y))
