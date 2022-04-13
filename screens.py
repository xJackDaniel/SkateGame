import pygame
from constants import *
from helpers import screen
import helpers
from classes.Player import *
from classes.Bar import *
from classes.Character import *

from screen_classes.Button import *
from screen_classes.Cloud import *
import random

def game(data, img, clock, score=0, hearts=3):
    # Create the character
    character, character_num = equipped_character()
    player = Player(hearts, f"{CHARACTER_PATH}{character}.png", data.get(BEST_SCORE), score)
    # Create pause button
    pause_btn = Button(pygame.image.load(PAUSE_PATH), None, PAUSE_PATH, PAUSE_X_POS, PAUSE_Y_POS, PAUSE_WIDTH, PAUSE_HEIGHT)

    # Create heart images
    heart_1 = Button(pygame.image.load(HEART_PATH), None, HEART_ID + "1", HEART_X_POS_1, HEART_Y_POS, HEART_WIDTH,
                     HEART_HEIGHT)
    heart_2 = Button(pygame.image.load(HEART_PATH), None, HEART_ID + "2", HEART_X_POS_2, HEART_Y_POS, HEART_WIDTH,
                     HEART_HEIGHT)
    heart_3 = Button(pygame.image.load(HEART_PATH), None, HEART_ID + "3", HEART_X_POS_3, HEART_Y_POS, HEART_WIDTH,
                     HEART_HEIGHT)

    # Check hearts - if user pause and resume - we need to check the amount of hearts
    # on the screen
    player.hearts_check(heart_1, heart_2, heart_3)

    # Create clouds
    cloud1 = Cloud(True, pygame.image.load(CLOUD_IMAGE), 1)
    cloud2 = Cloud(True, pygame.image.load(CLOUD_IMAGE), 2)
    cloud3 = Cloud(True, pygame.image.load(CLOUD_IMAGE), 3)
    cloud4 = Cloud(True, pygame.image.load(CLOUD_IMAGE), 4)
    cloud5 = Cloud(True, pygame.image.load(CLOUD_IMAGE), 5)
    cloud6 = Cloud(True, pygame.image.load(CLOUD_IMAGE), 6)

    # Create railing bar
    railing = Bar(RAILING_TYPE, RAILING_HEIGHT, RAILING_WIDTH, False, RAILING_START_X, RAILING_IMAGE)

    # Create stairs bar
    stairs = Bar(STAIRS_TYPE, STAIRS_HEIGHT, STAIRS_WIDTH, True, STAIRS_START_X, STAIRS_IMAGE)

    # Create bird bar
    bird = Bar(BIRD_TYPE, BIRD_HEIGHT, BIRD_WIDTH, False, BIRD_START_X, BIRD_IMAGE)

    # Bars list
    bars = [stairs, railing, bird]

    # No bar moving at the start
    moving_bar = None

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if mouse_in_object(pause_btn, pos):
                    pause(score=player.current_score, hearts=player.hearts, img=img, clock=clock, data=data)

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

        # Display the clouds
        cloud1.display_cloud()
        cloud2.display_cloud()
        cloud3.display_cloud()
        cloud4.display_cloud()
        cloud5.display_cloud()
        cloud6.display_cloud()

        # Move the clouds
        clouds_move(cloud1, cloud2, cloud3, cloud4, cloud5, cloud6)

        # Display the score
        score_font = pygame.font.SysFont("Arial", SCORE_SIZE)
        screen.blit(score_font.render(f"SCORE: {int(player.current_score)}", True, SCORE_COLOR),
                    (SCORE_X_POS, SCORE_Y_POS))

        # Display the pause button
        pause_btn.display_button()

        # display the hearts
        heart_1.display_button()
        heart_2.display_button()
        heart_3.display_button()

        # display the bars
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
            # New bar - need reset to fields
            bar.moving = True
            bar.check = False
            moving_bar = bar

        # Check if user pass the bar
        if moving_bar:
            check = player.check_pass(moving_bar, heart_1, heart_2, heart_3)
            if check is not None:
                if check is False:
                    # If the user don't pass the bar - need to check his hearts
                    if player.hearts == 0:
                        # The user reached 0 hearts - end of the game
                        # Check if the player reach new best score
                        if player.current_score > data.get("best_score"):
                            data["best_score"] = int(player.current_score)
                            write_data(data)
                        # Add coins to the player
                        add_coins(data, player.current_score)
                        # Display game over screen

                        game_over(score=player.current_score,img=img, clock=clock, data=data)
                # In order not to check the same bar several times
                moving_bar.check = True

        # Add score to the player
        player.add_score()

        # Check if user reach new best score
        if (player.current_score > player.best_score) and (player.best_score > 0):
            new_best_score()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(30)

def home(img, clock, data):
    # Display the background, presented Image, likes, comments, tags and
    # location(on the Image)
    screen.blit(img, (0, 0))
    # Create buttons
    play = Button(pygame.image.load(PLAY_PATH), "play", PLAY_ID, PLAY_X, PLAY_Y, PLAY_WIDTH, PLAY_HEIGHT)
    shop_btn = Button(pygame.image.load(SHOP_PATH), "shop", SHOP_ID, SHOP_X, SHOP_Y, SHOP_WIDTH, SHOP_HEIGHT)
    # Display the buttons on the screen
    play.display_button()
    shop_btn.display_button()

    # Display the coins
    score_font = pygame.font.SysFont("Arial", COIN_SIZE)
    screen.blit(score_font.render(str(data.get("coins")), True, COIN_COLOR),
                (COIN_TEXT_X, COIN_Y))

    coin = pygame.image.load(COIN_PATH)
    coin = pygame.transform.scale(coin, (COIN_WIDTH, COIN_HEIGHT))
    screen.blit(coin, (COIN_IMAGE_X, COIN_Y))

    # Display the best score
    score_font = pygame.font.SysFont("Arial", BEST_SCORE_SIZE)
    screen.blit(score_font.render(str(data.get("best_score")), True, BEST_SCORE_COLOR),
                (BEST_SCORE_TEXT_X, BEST_SCORE_Y))

    trophy = pygame.image.load(TROPHY_PATH)
    trophy = pygame.transform.scale(trophy, (TROPHY_WIDTH, TROPHY_HEIGHT))
    screen.blit(trophy, (TROPHY_IMAGE_X, BEST_SCORE_Y))

    # Display the logo
    logo_font = pygame.font.SysFont("Arial", LOGO_SIZE)
    screen.blit(logo_font.render("SkateGame", True, COIN_COLOR),
                (LOGO_TEXT_X, LOGO_Y))

    logo = pygame.image.load(LOGO_PATH)
    logo = pygame.transform.scale(logo, (LOGO_WIDTH, LOGO_HEIGHT))
    screen.blit(logo, (LOGO_IMAGE_X, LOGO_Y))

    #Display the frame of the rectange
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(X_FRAME,  Y_FRAME, WIDTH_FRAME, HEIGHT_FRAME))

    #Display the "help" rectangle
    pygame.draw.rect(screen, COLOR_RECT, pygame.Rect(X_RECT, Y_RECT, WIDTH_RECT, HEIGHT_RECT))

    #Display the title of the information rectangle
    title_info_font = pygame.font.SysFont("Arial", 25)
    screen.blit(title_info_font.render(TITLE_INFO_TEXT, True, TITLE_INFO_COLOR), (TITLE_INFO_X, TITLE_INFO_Y))

    #Display the text info about the bird obstible
    info_font = pygame.font.SysFont("Arial", 15)
    screen.blit(info_font.render(BIRD_TEXT_INFO, True, BIRD_TEXT_INFO_COLOR), (BIRD_INFO_X_POS, BIRD_INFO_Y_POS))

    #Display the bird close to its obsticle informantion
    info_bird = pygame.image.load(BIRD_PATH)
    info_bird = pygame.transform.scale(info_bird, (INFO_BIRD_WIDTH, INFO_BIRD_HEIGHT))
    screen.blit(info_bird, (INFO_BIRD_X, INFO_BIRD_Y))

    #Display the text info about the railing obsticle
    info_railing_font = pygame.font.SysFont("Arial", 15)
    screen.blit(info_railing_font.render(RAILING_TEXT_INFO, True, RAILING_TEXT_INFO_COLOR), (RAILING_INFO_X_POS, RAILING_INFO_Y_POS))

    #Display the railing close to its obsticle informantion
    info_railing = pygame.image.load(RAILING_PATH)
    info_railing = pygame.transform.scale(info_railing, (INFO_RAILING_WIDTH, INFO_RAILING_HEIGHT))
    screen.blit(info_railing, (INFO_RAILING_X, INFO_RAILING_Y))

    #Display the text info about the stairs obsticle
    info_stairs_font = pygame.font.SysFont("Arial", 15)
    screen.blit(info_stairs_font.render(STAIRS_INFO, True, STAIRS_INFO_COLOR), (STAIRS_INFO_X_POS, STAIRS_INFO_Y_POS))

    #Display the stairs close to its obsticle informantion
    info_stair = pygame.image.load(STAIRS_PATH)
    info_stair = pygame.transform.scale(info_stair, (INFO_STAIRS_WIDTH, INFO_STAIRS_HEIGHT))
    screen.blit(info_stair, (INFO_STAIRS_X, INFO_STAIRS_Y))

    #Display the upper arrow button
    upper_arrow = pygame.image.load(UPPER_ARROW_PATH)
    upper_arrow = pygame.transform.scale(upper_arrow, (UPPER_ARROW_WIDTH, UPPER_ARROW_HEIGHT))
    screen.blit(upper_arrow, (UPPER_ARROW_X, UPPER_ARROW_Y))

    #Display the bottom arrow button
    bottom_arrow = pygame.image.load(BOTTOM_ARROW_PATH)
    bottom_arrow = pygame.transform.scale(bottom_arrow, (BOTTOM_ARROW_WIDTH, BOTTOM_ARROW_HEIGHT))
    screen.blit(bottom_arrow, (BOTTOM_ARROW_X, BOTTOM_ARROW_Y))

    #Display the second bottom arrow button
    bottom_arrow_2 = pygame.image.load(BOTTOM_ARROW_PATH)
    bottom_arrow_2 = pygame.transform.scale(bottom_arrow_2, (BOTTOM_ARROW_WIDTH, BOTTOM_ARROW_HEIGHT))
    screen.blit(bottom_arrow_2, (BOTTOM_ARROW_X_2, BOTTOM_ARROW_Y_2))

    # Display the text information about the bonus hearts that appear while the game is running
    bonus_heart_font = pygame.font.SysFont("Arial", 15)
    screen.blit(bonus_heart_font.render(HEART_TEXT_INFO, True, HEART_TEXT_COLOR), (HEART_TEXT_X, HEART_TEXT_Y))

    # Display heart image next to its text explanation
    bonus_heart = pygame.image.load(HEART_PATH)
    bonus_heart = pygame.transform.scale(bonus_heart, (BONUS_HEART_WIDTH, BONUS_HEART_HEIGHT))
    screen.blit(bonus_heart, (BONUS_HEART_X, BONUS_HEART_Y))

   # Display the text explanation about the bonus coins that appear while the game is running
    bonus_coins_font = pygame.font.SysFont("Arial", 15)
    screen.blit(bonus_coins_font.render(COIN_INFO, True, COIN_INFO_COLOR), (COIN_INFO_X, COIN_INFO_Y))

    # Display the coin image next to its text explanation
    bonus_coin = pygame.image.load(COIN_PATH)
    bonus_coin = pygame.transform.scale(bonus_coin, (BONUS_COIN_WIDTH, BONUS_COIN_HEIGHT))
    screen.blit(bonus_coin, (BONUS_COIN_X, BONUS_COIN_Y))


    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if mouse_in_object(play, pos):
                    game(data=data, img=img, clock=clock)
                elif mouse_in_object(shop_btn, pos):
                    shop(img=img, clock=clock, data=data)
        # Update the screen
        pygame.display.flip()
        # Update display - without input update everything
        pygame.display.update()
        clock.tick(30)

def shop(img, clock, data):

    # Create buttons
    home_btn = Button(pygame.image.load(HOME_PATH), "home", HOME_ID, HOME_X, HOME_Y, HOME_WIDTH, HOME_HEIGHT)

    # Create character objects
    character_1 = Character("1", SHOP_CHARACTER_X_POS_1, SHOP_CHARACTER_Y_POS, CHARACTER_PRICE_1, CHARACTER_PATH+"Character1.png")
    character_2 = Character("2", SHOP_CHARACTER_X_POS_2, SHOP_CHARACTER_Y_POS, CHARACTER_PRICE_2, CHARACTER_PATH+"Character2.png")
    character_3 = Character("3", SHOP_CHARACTER_X_POS_3, SHOP_CHARACTER_Y_POS, CHARACTER_PRICE_3, CHARACTER_PATH+"Character3.png")
    character_4 = Character("4", SHOP_CHARACTER_X_POS_4, SHOP_CHARACTER_Y_POS, CHARACTER_PRICE_4, CHARACTER_PATH+"Character4.png")
    character_5 = Character("5", SHOP_CHARACTER_X_POS_5, SHOP_CHARACTER_Y_POS, CHARACTER_PRICE_5, CHARACTER_PATH+"Character5.png")
    arrow_x = ARROW_X

    running = True
    # At first no message to display
    message_display = False
    message = None
    message_color = None

    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                pos = event.pos
                # Display arrow on mouse hover
                if mouse_in_object(character_1, pos):
                    arrow_x = character_1.x + 25
                elif mouse_in_object(character_2, pos):
                    arrow_x = character_2.x + 25
                elif mouse_in_object(character_3, pos):
                    arrow_x = character_3.x + 25
                elif mouse_in_object(character_4, pos):
                    arrow_x = character_4.x + 25
                elif mouse_in_object(character_5, pos):
                    arrow_x = character_5.x + 25
                else:
                    arrow_x = ARROW_X
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                # If home button clicked - display home screen
                if mouse_in_object(home_btn, pos):
                    home(img=img, clock=clock, data=data)
                # Check if left click(mouse)
                if event.button == 1:
                    # No character was clicked
                    char_num = 0
                    # Checks which character was clicked (if character clicked)
                    if mouse_in_object(character_1, pos):
                        message_display, message, message_color = True, "Character 1 successfully equipped!", SUCCESS_COLOR
                        data = equipe_character(1, data)
                        char_num = 1
                    elif mouse_in_object(character_2, pos):
                        char_num = 2
                    elif mouse_in_object(character_3, pos):
                        char_num = 3
                    elif mouse_in_object(character_4, pos):
                        char_num = 4
                    elif mouse_in_object(character_5, pos):
                        char_num = 5
                    # Make sure that a character clicked
                    if char_num > 1:
                        # Check if user own this character
                        if character_own(char_num):
                            # Success message
                            message_display, message, message_color = True, f"Character {char_num} successfully equipped!", SUCCESS_COLOR
                            data = equipe_character(char_num, data)
                        else:
                            # Check if user have enough money to buy this character
                            if int(data.get("coins")) >= PRICES[char_num]:
                                # Remove coins
                                data = remove_coins(PRICES[char_num], data)
                                # Set character as own
                                data = set_own_character(char_num, data)
                                # Success message
                                message_display, message, message_color = True, f"Character {char_num} bought successfully!", SUCCESS_COLOR
                            else:
                                # The user don't have enough money to buy this character
                                message_display, message, message_color = True, "You don't have enough money!", ERROR_COLOR


        # Update the screen
        pygame.display.flip()
        # Update display - without input update everything
        pygame.display.update()
        # New background
        screen.blit(img, (0, 0))
        # Display the coins
        score_font = pygame.font.SysFont("Arial", COIN_SIZE)
        screen.blit(score_font.render(str(data.get("coins")), True, COIN_COLOR),
                    (60, HOME_Y))

        coin = pygame.image.load(COIN_PATH)
        coin = pygame.transform.scale(coin, (COIN_WIDTH, COIN_HEIGHT))
        screen.blit(coin, (20, HOME_Y))
        # Display the ground
        pygame.draw.rect(screen, GROUND_COLOR, pygame.Rect(GROUND_X, GROUND_Y, GROUND_WIDTH, GROUND_HEIGHT))
        # Display the buttons on the screen
        home_btn.display_button()
        # Display character objects
        character_1.display_character()
        character_2.display_character()
        character_3.display_character()
        character_4.display_character()
        character_5.display_character()
        # Hover
        hover(arrow_x)
        # Display the message
        if message_display is True:
            message_font = pygame.font.SysFont("Arial", SHOP_MESSAGE_SIZE)
            screen.blit(message_font.render(message, True, message_color),
                        (SHOP_MESSAGE_X, SHOP_MESSAGE_Y))


        clock.tick(30)

def pause(score, hearts, img, clock, data):
    # Display the background, presented Image, likes, comments, tags and
    # location(on the Image)
    screen.blit(img, (0, 0))
    # Create buttons
    resume = Button(pygame.image.load(RESUME_PATH), "game", RESUME_ID, RESUME_X, RESUME_Y, RESUME_WIDTH, RESUME_HEIGHT)
    quit_btn = Button(pygame.image.load(QUIT_PATH), "home", QUIT_ID, QUIT_X, QUIT_Y, QUIT_WIDTH, QUIT_HEIGHT)
    game_paused_btn = Button(pygame.image.load(PAUSED_IMAGE_PATH), None, PAUSED_IMAGE_ID, PAUSED_IMAGE_X, PAUSED_IMAGE_Y, PAUSED_IMAGE_WIDTH, PAUSED_IMAGE_HEIGHT)
    # Display the buttons on the screen
    resume.display_button()
    quit_btn.display_button()
    game_paused_btn.display_button()

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if mouse_in_object(resume, pos):
                    game(score=score, hearts=hearts, data=data, img=img, clock=clock)
                elif mouse_in_object(quit_btn, pos):
                    home(img=img, clock=clock, data=data)
        # Update the screen
        pygame.display.flip()
        # Update display - without input update everything
        pygame.display.update()
        clock.tick(30)

def game_over(score, img, clock, data):
    # Display the background, presented Image, likes, comments, tags and
    # location(on the Image)
    screen.blit(img, (0, 0))
    # Create buttons
    game_over_btn = Button(pygame.image.load(OVER_PATH), None, OVER_ID, OVER_X,
                             OVER_Y, OVER_WIDTH, OVER_HEIGHT)
    # Display the buttons on the screen
    game_over_btn.display_button()

    # Display the score
    score_font = pygame.font.SysFont("Arial", OVER_SCORE_SIZE)
    screen.blit(score_font.render(f"SCORE: {int(score)}", True, OVER_SCORE_COLOR),
                (OVER_SCORE_X_POS, OVER_SCORE_Y_POS))


    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        # Update the screen
        pygame.display.flip()
        # Update display - without input update everything
        pygame.display.update()
        # Cooldown for 3 seconds
        time.sleep(3)
        # Display home screen
        home(img=img, clock=clock, data=data)
