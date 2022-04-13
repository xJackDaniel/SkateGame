import pygame
import json
from constants import *
import time

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def clouds_move(cloud1, cloud2, cloud3, cloud4, cloud5, cloud6):
    clouds = [cloud1, cloud2, cloud3, cloud4, cloud5, cloud6]
    for cloud in clouds:
        # Check if cloud stop moving
        if cloud.moving is False:
            cloud.reset_cloud()
        cloud.x -= 3

def mouse_in_object(obj, mouse_pos):
    """
    The function get button and mouse press position on screen and return True
    if mouse click on button
    :param obj: Any object
        object on screen
    :param mouse_pos: tuple
        the x and y position of the mouse cursor
    :return: boolean
        True if mouse click on button, else False
    """
    if obj.x + obj.width > mouse_pos[0] > obj.x and \
            obj.y < mouse_pos[1] < obj.y + obj.height:
        return True

def read_data():
    """Read data and return as dictionary"""
    # Opening JSON file
    f = open('data.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    return data

def write_data(data):
    """Write data to the file"""
    with open('data.json', 'w') as data_file:
        json.dump(data, data_file)

def equipped_character():
    """Return the equipped user character"""
    data = read_data()
    for char in range(CHARACTERS_AMOUNT):
        if data.get(f"character_{char+1}") == CHARACTER_EQUIPPED:
            return f"Character{char+1}", char+1

def equipe_character(character_num, data):
    """Equip the character by its num
       *This function calls only if user owns the <character_num>*"""
    for char in range(CHARACTERS_AMOUNT):
        if (data.get(f"character_{char+1}") == CHARACTER_EQUIPPED) and (char+1 != character_num):
            # Unequipe the old character
           data[f"character_{char+1}"] = CHARACTER_OWN
        elif char+1 == character_num:
            # Equipe the new character
            data[f"character_{char + 1}"] = CHARACTER_EQUIPPED
    write_data(data)
    return data

def character_own(num):
    """Check if the player owns the character"""
    data = read_data()
    character = data.get(f"character_{num}")
    if character == CHARACTER_EQUIPPED or character == CHARACTER_OWN:
        return True
    else:
        return False


def add_coins(data, coins):
    """Add coins to user's data"""
    current_coins = data.get("coins")
    data["coins"] = int(current_coins + coins)
    write_data(data)
    return data

def remove_coins(coins: int, data):
    """Remove coins to user from data"""
    current_coins = data.get("coins")
    data["coins"] = current_coins - coins
    write_data(data)
    return data

def set_own_character(num: int, data):
    """Set a character as own by num"""
    data[f"character_{num}"] = CHARACTER_OWN
    write_data(data)
    return data

def get_character_status(num):
    """Return a character status by num"""
    data = read_data()
    return data.get(f"character_{num}")

def hover(x):
    """Display a green arrow above the character at the shop"""
    arrow = pygame.image.load(ARROW_PATH)
    arrow = pygame.transform.scale(arrow, (ARROW_WIDTH, ARROW_HEIGHT))
    screen.blit(arrow, (x + 20, ARROW_Y_POS))

def new_best_score():
    """A new best score message"""
    x = BEST_SCORE_MESSAGE_X
    message_font = pygame.font.SysFont("Arial", BEST_SCORE_MESSAGE_SIZE)
    screen.blit(message_font.render("NEW BEST SCORE!", True, SHOP_COLOR),
                (x, BEST_SCORE_MESSAGE_Y))


