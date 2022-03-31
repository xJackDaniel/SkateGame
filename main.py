import pygame
from constants import *
from helpers import screen
from classes.Player import *


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('SkateGame')

    clock = pygame.time.Clock()

    # Set up background image
    img = pygame.image.load("images/backgrounds/background.png")
    img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))


    # display the character
    player = Player(3, "images/Characters/Character1.png", 0, 0)

    jumpCount = 10

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_DOWN]:
                if not player.down:
                    player.get_down()
            elif player.down:
                player.reset_player()

            if player.jump is False and pressed[pygame.K_SPACE]:
                player.jump = True

            if player.jump is True:
                if jumpCount >= -10:
                    player.y -= (jumpCount * abs(jumpCount)) * 0.5
                    jumpCount -= 1
                else:
                    jumpCount = 10
                    player.jump = False


        # Update the screen
        pygame.display.flip()
        # Update display - without input update everything
        pygame.display.update()

        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        screen.blit(img, (0, 0))

        # Display the player
        player.display_player()

        # Display the ground
        pygame.draw.rect(screen, GROUND_COLOR, pygame.Rect(GROUND_X, GROUND_Y, GROUND_WIDTH, GROUND_HEIGHT))

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(30)
    pygame.quit()
    quit()


main()