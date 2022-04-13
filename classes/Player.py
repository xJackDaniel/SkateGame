from helpers import screen
import pygame
from constants import *

class Player:
    def __init__(self, hearts, character_num, skin, best_score, current_score, coins):
        self.hearts = hearts
        self.skin = skin
        self.character_num = character_num
        self.best_score = best_score
        self.current_score = current_score
        self.down = False
        self.jump = False
        self.height = CHARACTER_HEIGHT
        self.y = CHARACTER_Y_POS
        self.x = CHARACTER_X_POS
        self.character_img = pygame.image.load(skin)
        self.jump_count = JUMP_COUNT
        self.coins = coins
        self.blink = False
        self.blinkCount = 30


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
        self.current_score += 0.5

    def add_coins(self, coins):
        """Add coins to the player's code"""
        self.coins += coins

    def get_height(self):
        """Returns the player's character height"""
        return self.height

    def set_new_character(self, num):
        """Set new character skin"""
        self.skin = f"{CHARACTER_PATH}Character{num}.png"
        self.character_img = pygame.image.load(self.skin)
        self.character_num = num



    def display_player(self):
        """Display the player character on the screen"""
        self.character_img = pygame.transform.scale(self.character_img, (CHARACTER_WIDTH, self.height))
        screen.blit(self.character_img, (self.x, self.y))

    def reset_player(self):
        """Reset the player Y and Height"""
        self.y = CHARACTER_Y_POS
        self.height = CHARACTER_HEIGHT
        self.down = False
        self.character_img = pygame.image.load(self.skin)

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
        # Jump sound
        jump_sound = pygame.mixer.Sound(JUMP_SOUND)
        pygame.mixer.Sound.play(jump_sound)
        pygame.mixer.music.stop()

    def check_pass(self, object, heart_1, heart_2, heart_3):
        """Checks if player pass the object"""
        # Check that the bar is not already checked
        if object.check is False:
            # Check if the bar is found on the player
            if (self.x <= object.x) and ((self.x + CHARACTER_WIDTH) >= object.x):
                if object.jump:
                    # If the user needs to jump in this bar - check jump + make the character blink
                    if self.jump is False:
                        self.hearts -= 1
                        # If the user didn't jump - remove heart
                        self.hearts_check(heart_1, heart_2, heart_3)
                    return self.jump
                else:
                    # If the user needs to get down in this bar - check down
                    if self.down is False:
                        # If the user didn't get down - remove heart + make the character blink.
                        self.hearts -= 1
                        self.hearts_check(heart_1, heart_2, heart_3)
                    return self.down

    def claim_check(self, object):
        """Checks if player claim the object"""
        # Check that the object is not already checked
        if object.check is False:
            # Check if the bar is found on the player
            if (self.x <= object.x) and ((self.x + CHARACTER_WIDTH) >= object.x):
                if object.jump:
                    return self.jump
                else:
                    return self.down

    def hearts_check(self, heart_1, heart_2, heart_3):
        """Removes heart and update hearts"""
        if self.hearts > 0:
            # Reset all the hearts at their positions
            if self.hearts == 3:
                heart_1.x = HEART_X_POS_1
                heart_2.x = HEART_X_POS_2
                heart_3.x = HEART_X_POS_3
            elif self.hearts == 2:
                heart_1.x = HEART_X_POS_1
                heart_2.x = HEART_X_POS_2
                heart_3.x = HEART_X_OUT
            else:
                heart_1.x = HEART_X_POS_1
                heart_2.x = HEART_X_OUT
                # If user pause and resume we need to move the 3rd heart again
                heart_3.x = HEART_X_OUT
        else:
            heart_1.x = HEART_X_OUT
            heart_2.x = HEART_X_OUT
            heart_3.x = HEART_X_OUT

    def glowing_character(self):
        """Makes the character blink"""
        if self.blinkCount >= 0 and self.blink:
            if self.blinkCount % 2 == 0:
                # Return the character to base
                self.character_img = pygame.image.load(self.skin)
            else:
                # Set alpha to the character
                self.character_img.set_alpha(128)
            self.blinkCount -= 1
        else:
            self.blinkCount = 10
            self.blink = False
