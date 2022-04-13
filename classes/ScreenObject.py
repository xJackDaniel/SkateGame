import pygame
from helpers import screen
from constants import *

class ScreenObject:
    def __init__(self, type, height, width, jump, x, image):
        self.type = type
        self.height = height
        self.width = width
        self.jump = jump
        self.moving = False
        self.x = x
        self.image = pygame.image.load(image)
        self.check = False

    def get_type(self):
        """Returns the object's type"""
        return self.type

    def get_height(self):
        """Returns the object's height"""
        return self.height

    def get_width(self):
        """Returns the object's width"""
        return self.width

    def get_jump(self):
        """Returns True/False if the player needs to jump over the object"""
        return self.jump

    def object_join(self, current_score):
        """Start moving the object"""
        if self.moving:
            if self.x > -300:
                self.x -= current_score * 0.1
            else:
                self.reset_object()

    def reset_object(self):
        """Reset the object's position"""
        if self.type == RAILING_TYPE:
            self.x = RAILING_START_X
        elif self.type == BIRD_TYPE:
            self.x = BIRD_START_X
        elif self.type == HEART_AWARD_TYPE:
            self.x = HEART_AWARD_START_X
        elif self.type == COIN_AWARD_TYPE:
            self.x = COIN_AWARD_START_X
        else:
            self.x = STAIRS_START_X
        self.moving = False

    def create_object(self):
        """Creates the object out of the screen"""
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if self.type == RAILING_TYPE:
            y = RAILING_Y
        elif self.type == BIRD_TYPE:
            y = BIRD_Y
        elif self.type == HEART_AWARD_TYPE:
            y = HEART_AWARD_Y
        elif self.type == COIN_AWARD_TYPE:
            y = COIN_AWARD_Y
        else:
            y = STAIRS_Y
        screen.blit(self.image, (self.x, y))


