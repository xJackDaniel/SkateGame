import pygame

from constants import *

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





