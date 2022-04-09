import pygame
from helpers import screen
from constants import *

class Character:
    def __init__(self, id, x, y, price, image):
        self.id = id
        self.price = price
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.width = CHARACTER_WIDTH
        self.height = CHARACTER_HEIGHT


    def get_price(self):
        """Returns the price for the character"""
        return self.price

    def display_character(self):
        """Display the character on the shop"""
        self.image = pygame.transform.scale(self.image, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
        screen.blit(self.image, (self.x, self.y))

        # Display the character price
        character_font = pygame.font.SysFont("Arial", SHOP_PRICE_SIZE)
        screen.blit(character_font.render("Price: {:,}".format(self.price), True, SHOP_COLOR),
                    (self.x+25, SHOP_PRICE_Y_POS))

    def is_own(self):
        """Return True/False if the player owns this character."""
        pass