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
        self.jump = False
        self.height = CHARACTER_HEIGHT
        self.y = CHARACTER_Y_POS
        self.x = CHARACTER_X_POS
        self.character_img = pygame.image.load("images/Characters/Character1.png")
        self.jump_count = JUMP_COUNT


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

    def get_height(self):
        """Returns the player's character height"""
        return self.height

    def display_player(self):
        """Display the player character on the screen"""
        self.character_img = pygame.transform.scale(self.character_img, (CHARACTER_WIDTH, self.height))
        screen.blit(self.character_img, (self.x, self.y))

    def reset_player(self):
        """Reset the player Y and Height"""
        self.y = CHARACTER_Y_POS
        self.height = CHARACTER_HEIGHT
        self.down = False

    def get_down(self):
        """The character bending over"""
        self.height = CHARACTER_HEIGHT - 60
        self.y = CHARACTER_Y_POS + 60
        self.down = True

    def player_jump(self):
        """ The character jumping over"""
        if self.jump_count >= -10:
            self.y -= (self.jump_count * abs(self.jump_count)) * 0.5
            self.jump_count -= 1
        else:
            self.jump_count = 10
            self.jump = False



