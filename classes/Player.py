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
        return self.hearts

    def get_skin(self):
        return self.skin

    def get_best_score(self):
        return self.best_score

    def get_current_score(self):
        return self.currect_score

    def add_score(self):
        pass

    def set_best_score(self):
        pass

    def display_player(self):
        self.character_img = pygame.transform.scale(self.character_img, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
        screen.blit(self.character_img, (CHARACTER_X_POS, CHARACTER_Y_POS))

    def get_down(self):
        self.character_img = pygame.transform.scale(self.character_img, (CHARACTER_WIDTH, CHARACTER_HEIGHT-60))
        screen.blit(self.character_img, (CHARACTER_X_POS, CHARACTER_Y_POS+60))


