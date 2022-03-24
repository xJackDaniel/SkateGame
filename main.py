import pygame
from constants import *
from helpers import screen


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('SkateGame')

    clock = pygame.time.Clock()

    # Set up background image
    img = pygame.image.load("images/backgrounds/background.png")
    img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
    # Display the background, presented Image, likes, comments, tags and
    # location(on the Image)
    screen.blit(img, (0, 0))

    # Display the ground
    pygame.draw.rect(screen, GROUND_COLOR, pygame.Rect(GROUND_X, GROUND_Y, GROUND_WIDTH, GROUND_HEIGHT))

    # display the character

    character_img = pygame.image.load("images/Characters/Character1.png")
    character_img = pygame.transform.scale(character_img, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
    screen.blit(character_img, (CHARACTER_X_POS, CHARACTER_Y_POS))

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Update the screen
        pygame.display.flip()
        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(10)
    pygame.quit()
    quit()


main()