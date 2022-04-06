import pygame
from constants import*
from helpers import*
import random

class Cloud:
    def __init__(self, moving, image, num):
        self.moving = moving
        self.image = image
        self.num = num
        self.x = CLOUD_X[num-1]

    def check_end(self):
        """Checks if the cloud is at the end of the screen"""
        if self.x > -CLOUD_WIDTH:
            self.moving = True
        else:
            self.moving = False

    def reset_cloud(self):
        """Reset the cloud x"""
        self.x = CLOUD_X[self.num-1]

    def display_cloud(self):
        """Displays the cloud on the screen"""
        self.image.set_alpha(128)
        self.image = pygame.transform.scale(self.image, (CLOUD_WIDTH, CLOUD_HEIGHT))
        screen.blit(self.image, (self.x, CLOUD_Y[self.num-1]))
        self.check_end()






