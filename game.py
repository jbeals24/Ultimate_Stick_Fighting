import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the window dimensions
WIDTH = 1200
HEIGHT = 800

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stick Figure")

# Define the initial character position
character_x = 200
character_y = 200

left = False
right = False

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
        

    
    
        



        # elif event.type == pygame.KEYDOWN:

        #     # if event.key == pygame.K_LEFT:
        #     #     while (event.type != pygame.KEYUP):
        #     #         character_x -= 20

        #     if event.key == pygame.K_LEFT:
        #         character_x -= 20  # Move character left
        #     elif event.key == pygame.K_RIGHT:
        #         character_x += 20  # Move character right

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

# Quit Pygame
pygame.quit()
sys.exit()
