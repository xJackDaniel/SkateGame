import pygame
from constants import *
from helpers import screen
from classes.Player import *
from classes.Bar import *
from screen_classes.Button import *
import random

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

    #display pause button
    pause = Button(pygame.image.load("images/buttons/Pause.png"), None, None, "PAUSE", PAUSE_X_POS, PAUSE_Y_POS, PAUSE_WIDTH, PAUSE_HEIGHT)

    #display heart images
    heart_1 = Button(pygame.image.load(HEART_PATH), None, None, HEART_ID+"1", HEART_X_POS_1, HEART_Y_POS, HEART_WIDTH, HEART_HEIGHT)
    heart_2 = Button(pygame.image.load(HEART_PATH), None, None, HEART_ID+"2", HEART_X_POS_2, HEART_Y_POS, HEART_WIDTH, HEART_HEIGHT)
    heart_3 = Button(pygame.image.load(HEART_PATH), None, None, HEART_ID+"3", HEART_X_POS_3, HEART_Y_POS, HEART_WIDTH, HEART_HEIGHT)

    # Create railing bar
    railing = Bar(RAILING_TYPE, RAILING_HEIGHT, RAILING_WIDTH, False, RAILING_START_X, RAILING_IMAGE)

    # Create stairs bar
    stairs = Bar(STAIRS_TYPE, STAIRS_HEIGHT, STAIRS_WIDTH, True, STAIRS_START_X, STAIRS_IMAGE)

    # Create bird bar
    bird = Bar(BIRD_TYPE, BIRD_HEIGHT, BIRD_WIDTH, False, BIRD_START_X, BIRD_IMAGE)

    # Bars list
    bars = [stairs, railing, bird]

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_DOWN]:
                if not player.down and player.jump is False:
                    player.get_down()
            elif player.down:
                player.reset_player()

            if player.jump is False and pressed[pygame.K_SPACE]:
                player.jump = True

        if player.jump is True and player.down is False:
            player.player_jump()


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

        #Display the pasue button
        pause.display_button()

        #Display the score
        score_font = pygame.font.SysFont("Arial", SCORE_SIZE)
        screen.blit(score_font.render(f"SCORE: {int(player.current_score)}", True, SCORE_COLOR), (SCORE_X_POS, SCORE_Y_POS))

        #display the hearts
        heart_1.display_button()
        heart_2.display_button()
        heart_3.display_button()

        #display the bar
        railing.create_bar()
        railing.bar_join(player.get_current_score())

        stairs.create_bar()
        stairs.bar_join(player.get_current_score())

        bird.create_bar()
        bird.bar_join(player.get_current_score())

        # Start the moving of the railing
        if not railing.moving and not stairs.moving and not bird.moving:
            # Random bar to join the screen
            bar = random.choice(bars)
            # The stairs join only if the play is over 200 score
            # because if the stairs are slow the user can't jump
            while player.current_score < 200 and bar == stairs:
                bar = random.choice(bars)
            bar.moving = True

        #Add score to the player
        player.add_score()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(30)
    pygame.quit()
    quit()


main()