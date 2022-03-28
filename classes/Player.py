from helpers import screen
import pygame
from constants import *

class Player:
    def __init__(self, hearts, skin, best_score, current_score):
        self.hearts = hearts
        self.skin = skin
        self.best_score = best_score
        self.current_score = current_score
        self.down = False
        self.character_img = pygame.image.load("images/Characters/Character1.png")

    def get_hearts(self):
        """Returns the amount of hearts left to the user"""
        return self.hearts

    def get_skin(self):
        """Returns the current skin of the player"""
        return self.skin

    def get_best_score(self):
        """Returns the best score of the player"""
        return self.best_score

    def get_current_score(self):
        """Returns the current score of the player"""
        return self.current_score

    def add_score(self):
        """Add score to the current_score"""
        pass

    def set_best_score(self):
        """Set a new best score to the player"""
        pass

    def display_player(self):
        """Display the player character on the screen"""
        self.character_img = pygame.transform.scale(self.character_img, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
        screen.blit(self.character_img, (CHARACTER_X_POS, CHARACTER_Y_POS))

    def get_down(self):
        """The character bending over"""
        self.character_img = pygame.transform.scale(self.character_img, (CHARACTER_WIDTH, CHARACTER_HEIGHT-60))
        screen.blit(self.character_img, (CHARACTER_X_POS, CHARACTER_Y_POS+60))


