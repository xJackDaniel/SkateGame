from screens import *

def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title and icon of the window
    pygame.display.set_caption('SkateGame')
    pygame.display.set_icon(pygame.image.load(LOGO_PATH))

    global clock
    clock = pygame.time.Clock()

    # Receive user data
    global data
    data = read_data()

    # Set up background image
    global img
    img = pygame.image.load(BACKGROUND_PATH)
    img = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
    # Display the background, presented Image, likes, comments, tags and
    # location(on the Image)
    screen.blit(img, (0, 0))

     # Display home screen
    home(img, clock, data)



main()