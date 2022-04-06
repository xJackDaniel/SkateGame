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





