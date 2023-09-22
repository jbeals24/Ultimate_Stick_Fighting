import pygame
import sys

# Constants for the window dimensions
WIDTH = 1200
HEIGHT = 800

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def initialize():
    # Initialize Pygame
    pygame.init() 

    # Create the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Stick Figure")

    # Define the initial character position
    character_x = 200
    character_y = 200

    return screen, character_x, character_y


def drawCharacters(screen, character_x, character_y):

    # Clear the screen
    screen.fill(WHITE)

    # Draw the stick figure at the updated position
    pygame.draw.circle(screen, BLACK, (character_x, character_y - 30), 30)  # Head
    pygame.draw.line(screen, BLACK, (character_x, character_y), (character_x, character_y + 100), 5)  # Body
    pygame.draw.line(screen, BLACK, (character_x, character_y + 20), (character_x - 20, character_y + 70), 5)  # Left arm
    pygame.draw.line(screen, BLACK, (character_x, character_y + 20), (character_x + 20, character_y + 70), 5)  # Right arm
    pygame.draw.line(screen, BLACK, (character_x, character_y + 100), (character_x - 20, character_y + 170), 5)  # Left leg
    pygame.draw.line(screen, BLACK, (character_x, character_y + 100), (character_x + 20, character_y + 170), 5)  # Right leg

    # Update the display
    pygame.display.flip()


def engine(screen, character_x, character_y):

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]: 
            left = True
            if character_x > 30: character_x -= .5
            
            
        if keys[pygame.K_RIGHT]: 
            right = True
            if character_x < WIDTH - 30: character_x += .5

        drawCharacters(screen, character_x, character_y)

    pygame.quit()
    sys.exit()


def main():

    #initialize variables
    left = False
    right = False

    #set up the window and character placement
    screen, character_x, character_y = initialize()

    #run the game
    engine(screen, character_x, character_y)
 

main()
        

   
