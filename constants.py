# Data
BEST_SCORE = "best_score"
START_HEARTS = 3
ERROR_COLOR = (255, 0, 0)
SUCCESS_COLOR = (76, 153, 0)

# Coin value
DEFAULT_COIN_VALUE = 1
BIG_COIN_VALUE = 50

# COLORS
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Width and Height of the project window
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 616

# Character's location
CHARACTER_HEIGHT = 150
CHARACTER_WIDTH = 150
CHARACTER_X_POS = 30
CHARACTER_Y_POS = 310

# Characters
CHARACTERS_AMOUNT = 5
CHARACTER_EQUIPPED = "equipped"
CHARACTER_OWN = "yes"
CHARACTER_NOT_OWN = "no"
CHARACTER_PATH = "images/Characters/"

# Coins homepage
COIN_TEXT_X = WINDOW_WIDTH-70
COIN_IMAGE_X = WINDOW_WIDTH-110
COIN_Y = 20
COIN_SIZE = 30
COIN_COLOR = (255, 255, 255)
COIN_WIDTH = 35
COIN_HEIGHT = 35
COIN_PATH = "images/Objects/Coin.png"

# SkateGame logo
LOGO_TEXT_X = 110
LOGO_IMAGE_X = 68
LOGO_Y = 20
LOGO_SIZE = 30
LOGO_COLOR = (255, 255, 255)
LOGO_WIDTH = 35
LOGO_HEIGHT = 35
LOGO_PATH = "images/Objects/Skate.png"


# Play button
PLAY_PATH = "images/buttons/Play.png"
PLAY_WIDTH = 290
PLAY_HEIGHT = 230
PLAY_X = 25
PLAY_Y = 150
PLAY_ID = "PLAY"

# Shop button
SHOP_PATH = "images/buttons/Shop.png"
SHOP_WIDTH = 100
SHOP_HEIGHT = 70
SHOP_X = 76
SHOP_Y = 400
SHOP_ID = "SHOP"

# Home button
HOME_X = WINDOW_WIDTH-70
HOME_Y = 20
HOME_WIDTH = 50
HOME_HEIGHT = 50
HOME_PATH = "images/buttons/Home.png"
HOME_ID = "HOME"

# Shop positions
SHOP_CHARACTER_HEIGHT = 150
SHOP_CHARACTER_WIDTH = 150
SHOP_CHARACTER_X_POS_1 = 50
SHOP_CHARACTER_X_POS_2 = 250
SHOP_CHARACTER_X_POS_3 = 450
SHOP_CHARACTER_X_POS_4 = 650
SHOP_CHARACTER_X_POS_5 = 850
SHOP_CHARACTER_Y_POS = 310
SHOP_PRICE_Y_POS = 465
SHOP_PRICE_SIZE = 20
SHOP_COLOR = (255, 255, 255)
STATUS_COLOR = (0, 0, 255)

# Shop message
SHOP_MESSAGE_Y = 520
SHOP_MESSAGE_X = WINDOW_WIDTH/2-200
SHOP_MESSAGE_SIZE = 25

# Arrow
ARROW_Y_POS = 210
ARROW_PATH = "images/Objects/Arrow.png"
ARROW_WIDTH = 50
ARROW_HEIGHT = 70
ARROW_X = -100

# Shop prices
PRICES = [None, 0, 5000, 7500, 10000, 12000]
CHARACTER_PRICE_1 = 0
CHARACTER_PRICE_2 = 5000
CHARACTER_PRICE_3 = 7500
CHARACTER_PRICE_4 = 10000
CHARACTER_PRICE_5 = 12000

# Background
BACKGROUND_PATH = "images/backgrounds/background.png"

# Ground
GROUND_COLOR = (192, 192, 192)
GROUND_Y = 450
GROUND_X = 0
GROUND_HEIGHT = 166
GROUND_WIDTH = WINDOW_WIDTH

# jump
JUMP_COUNT = 10

# pause button
PAUSE_X_POS = 1000
PAUSE_Y_POS = -10
PAUSE_WIDTH = 100
PAUSE_HEIGHT = 100
PAUSE_PATH = "images/buttons/Pause.png"
PAUSE_ID = "PAUSE"

# score
SCORE_X_POS = 15
SCORE_Y_POS = 40
SCORE_SIZE = 20
SCORE_COLOR = (255, 255, 255)

# Game coins
COIN_GAME_TEXT_X = 50
COIN_GAME_IMAGE_X = 10
COIN_GAME_Y = 60
COIN_GAME_SIZE = 30
COIN_GAME_COLOR = (255, 255, 255)



# Hearts
HEART_X_POS_1 = 10
HEART_X_POS_2 = 45
HEART_X_POS_3 = 80
HEART_X_OUT = -50
HEART_Y_POS = 10
HEART_WIDTH = 30
HEART_HEIGHT = 30
HEART_PATH = "images/objects/Heart.png"
HEART_ID = "HEART"

# Best score message
BEST_SCORE_MESSAGE_X = 380
BEST_SCORE_MESSAGE_Y = 200
BEST_SCORE_MESSAGE_SIZE = 50

# Best score homepage
BEST_SCORE_TEXT_X = WINDOW_WIDTH-70
BEST_SCORE_Y = 70
BEST_SCORE_SIZE = 30
BEST_SCORE_COLOR = (255, 255, 255)
TROPHY_IMAGE_X = WINDOW_WIDTH-108
TROPHY_WIDTH = 33
TROPHY_HEIGHT = 33
TROPHY_PATH = "images/Objects/Trophy.png"

# Railing
RAILING_TYPE = "railing"
RAILING_WIDTH = 400
RAILING_HEIGHT = 300
RAILING_START_X = WINDOW_WIDTH + RAILING_WIDTH
RAILING_Y = 198
RAILING_IMAGE = "images/obsticles/Railing.png"

# Stairs
STAIRS_TYPE = "stairs"
STAIRS_WIDTH = 100
STAIRS_HEIGHT = 100
STAIRS_START_X = WINDOW_WIDTH + STAIRS_WIDTH
STAIRS_Y = 350
STAIRS_IMAGE = "images/obsticles/Stairs.png"

# Bird
BIRD_TYPE = "bird"
BIRD_WIDTH = 160
BIRD_HEIGHT = 160
BIRD_START_X = WINDOW_WIDTH + BIRD_WIDTH
BIRD_Y = 200
BIRD_IMAGE = "images/obsticles/Bird.png"

# Clouds
CLOUD_WIDTH = 200
CLOUD_HEIGHT = 100
CLOUD_Y = [0, 20, 10, 25, -10, 5]
CLOUD_X = [WINDOW_WIDTH, WINDOW_WIDTH+200, WINDOW_WIDTH+400, WINDOW_WIDTH+600, WINDOW_WIDTH+800, WINDOW_WIDTH+1000]
CLOUD_IMAGE = "images/Objects/Cloud.png"

# Resume button
RESUME_PATH = "images/buttons/Resume.png"
RESUME_WIDTH = 150
RESUME_HEIGHT = 150
RESUME_X = WINDOW_WIDTH/2 - 230
RESUME_Y = 350
RESUME_ID = "RESUME"

# Quit button
QUIT_PATH = "images/buttons/Quit.png"
QUIT_WIDTH = 250
QUIT_HEIGHT = 250
QUIT_X = WINDOW_WIDTH/2 - 30
QUIT_Y = 300
QUIT_ID = "QUIT"

# Game Paused image
PAUSED_IMAGE_PATH = "images/GameSituation/GamePaused.png"
PAUSED_IMAGE_WIDTH = 300
PAUSED_IMAGE_HEIGHT = 300
PAUSED_IMAGE_X = WINDOW_WIDTH/2 - 170
PAUSED_IMAGE_Y = 120
PAUSED_IMAGE_ID = "GAME_PAUSED"

# Game over image
OVER_PATH = "images/GameSituation/GameOver.png"
OVER_WIDTH = 500
OVER_HEIGHT = 250
OVER_X = WINDOW_WIDTH/2 - 250
OVER_Y = 140
OVER_ID = "GAME_OVER"

# Game over score
OVER_SCORE_X_POS = WINDOW_WIDTH/2 - 100
OVER_SCORE_Y_POS = 370
OVER_SCORE_SIZE = 50
OVER_SCORE_COLOR = (255, 255, 255)

# HEART AWARD
HEART_AWARD_TYPE = "heart"
HEART_AWARD_WIDTH = 50
HEART_AWARD_HEIGHT = 50
HEART_AWARD_START_X = WINDOW_WIDTH + HEART_AWARD_WIDTH
HEART_AWARD_Y = 200
HEART_AWARD_IMAGE = "images/Objects/Heart.png"

# COIN AWARD
COIN_AWARD_TYPE = "coin"
COIN_AWARD_WIDTH = 50
COIN_AWARD_HEIGHT = 50
COIN_AWARD_START_X = WINDOW_WIDTH + COIN_AWARD_WIDTH
COIN_AWARD_Y = 200
COIN_AWARD_IMAGE = "images/Objects/Coin.png"




# The inner white rectangle where the tips will be writen.
COLOR_RECT = (255, 255, 255)
X_RECT = 480
Y_RECT = 200
WIDTH_RECT = 590
HEIGHT_RECT = 370

# A black layer of our rectangle which will be displayed behind it.
X_FRAME = 470
Y_FRAME = 190
WIDTH_FRAME = 610
HEIGHT_FRAME = 390

# The title inside the rectangle
TITLE_INFO_TEXT = "Tips and Help:"
TITLE_INFO_COLOR = (0, 0, 0)
TITLE_INFO_X = 655
TITLE_INFO_Y = 200

# Text explanation on how to avoid the bird
BIRD_INFO_X_POS = 555
BIRD_INFO_Y_POS = 250
BIRD_TEXT_INFO = " - To get past the bird, press the bottom arrow button to crouch."
BIRD_TEXT_INFO_COLOR = (0, 0, 0)

# Bird image for display
BIRD_PATH = "images/obsticles/Bird.png"
INFO_BIRD_WIDTH = 50
INFO_BIRD_HEIGHT = 50
INFO_BIRD_X = 490
INFO_BIRD_Y = 230

# Text explanation on how to avoid the railing
RAILING_INFO_X_POS = 555
RAILING_INFO_Y_POS = 300
RAILING_TEXT_INFO = " - To get past the railing, press the bottom arrow button to crouch."
RAILING_TEXT_INFO_COLOR = (0, 0, 0)

# Railing image for display
RAILING_PATH = "images/obsticles/Railing.png"
INFO_RAILING_WIDTH = 50
INFO_RAILING_HEIGHT = 50
INFO_RAILING_X = 490
INFO_RAILING_Y = 285

# Text explanation on how to avoid the stairs
STAIRS_INFO_X_POS = 555
STAIRS_INFO_Y_POS = 350
STAIRS_INFO = " - To get past the stairs, press the upper arrow button to jump."
STAIRS_INFO_COLOR = (0, 0, 0)

# Stairs image for display
STAIRS_PATH = "images/obsticles/Stairs.png"
INFO_STAIRS_WIDTH = 50
INFO_STAIRS_HEIGHT = 50
INFO_STAIRS_X = 490
INFO_STAIRS_Y = 340

# Upper arrow button
UPPER_ARROW_PATH = "images/Arrow_buttons/Upper_arrow_button.png"
UPPER_ARROW_WIDTH = 50
UPPER_ARROW_HEIGHT = 50
UPPER_ARROW_X = 910
UPPER_ARROW_Y = 350

# bottom arrow button
BOTTOM_ARROW_PATH = "images/Arrow_buttons/Bottom_arrow_button.png"
BOTTOM_ARROW_WIDTH = 50
BOTTOM_ARROW_HEIGHT = 50
BOTTOM_ARROW_X = 910
BOTTOM_ARROW_Y = 220

# The second bottom arrow button
BOTTOM_ARROW_X_2 = 910
BOTTOM_ARROW_Y_2 = 280

# Text explanation for the hearts that appear randomly while the game is running
HEART_TEXT_INFO = " - These hearts will randomly spawn while the game is running. Jump to get bonus health. "
HEART_TEXT_COLOR = (0, 0, 0)
HEART_TEXT_X = 555
HEART_TEXT_Y = 420

# Heart image which will be displayed next to its text explanation
BONUS_HEART_WIDTH = 50
BONUS_HEART_HEIGHT = 50
BONUS_HEART_X = 490
BONUS_HEART_Y = 400

# Text explanation for the coins that appear randomly while the game is running
COIN_INFO = " - These coins will randomly spawn while the game is running. jump to get bonus 50 coins."
COIN_INFO_COLOR = (0, 0, 0)
COIN_INFO_X = 555
COIN_INFO_Y = 470

# Coin image which will be displayed next to its explanation
BONUS_COIN_WIDTH = 50
BONUS_COIN_HEIGHT = 50
BONUS_COIN_X = 490
BONUS_COIN_Y = 460

# Character changer button text info
CHAR_CHANGER_INFO = " - Using the 'c' button on your keyboard, you can change your character while playing."
CHAR_CHANGER_INFO_X = 555
CHAR_CHANGER_INFO_Y = 520
CHAR_CHANGER_INFO_COLOR = (0, 0, 0)

# C button image on keyboard
C_BUTTON_PATH = "images/Arrow_buttons/C_button_keyboard.png"
C_BUTTON_WIDTH = 50
C_BUTTON_HEIGHT = 50
C_BUTTON_X = 490
C_BUTTON_Y = 510
