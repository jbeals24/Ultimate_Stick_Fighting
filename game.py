import pygame
import sys

# Constants for the window dimensions
WIDTH = 1200
HEIGHT = 800


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def initialize():
    # Initialize Pygame
    pygame.init() 

    # Create the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Stick Figure")

    # Define the initial character position
    character_x = 800
    character_y = 400
    
    character_x1 = 200
    character_y1 = 400
    
    
    p1Health = 100
    p2Health = 100

    p1Jab = True

    return screen, character_x, character_y, character_x1, character_y1, p1Jab, p1Health, p2Health


def drawCharacters(screen, character_x, character_y, character_x1, character_y1, p1Jab, p1Health, p2Health):

    # Clear the screen
    screen.fill(WHITE)

    # Draw the stick figure at the updated position
    pygame.draw.circle(screen, BLACK, (character_x1, character_y1 - 30), 30)  # Head
    pygame.draw.line(screen, BLACK, (character_x1, character_y1), (character_x1 - 20, character_y1 + 100), 6)  # Body
    if p1Jab:
        pygame.draw.line(screen, BLACK, (character_x1 - 3, character_y1 + 15), (character_x1 + 8, character_y1 + 65), 6)  # Left arm
        pygame.draw.line(screen, BLACK, (character_x1 + 8, character_y1 + 65), (character_x1 + 30, character_y1 + 45), 6)  # Left forearm
        pygame.draw.circle(screen, BLACK, (character_x1 + 30, character_y1 + 45), 7) # Left hand
    else:
        pygame.draw.line(screen, BLACK, (character_x1 - 3, character_y1 + 15), (character_x1 + 50, character_y1 + 15), 6)  # Left arm
        pygame.draw.line(screen, BLACK, (character_x1 + 50, character_y1 + 15), (character_x1 + 90, character_y1 + 15), 6)  # Left forearm
        pygame.draw.circle(screen, BLACK, (character_x1 + 90, character_y1 + 15), 9) # Left hand
    pygame.draw.line(screen, BLACK, (character_x1 - 3, character_y1 + 15), (character_x1 + 20, character_y1 + 40), 6)  # Right arm
    pygame.draw.line(screen, BLACK, (character_x1 + 20, character_y1 + 40), (character_x1 + 40, character_y1 + 20), 6)  # Right forearm
    pygame.draw.circle(screen, BLACK, (character_x1 + 40, character_y1 + 20), 7) # Right hand
    pygame.draw.line(screen, BLACK, (character_x1 - 20, character_y1 + 100), (character_x1 - 45, character_y1 + 170), 6)  # Left leg
    pygame.draw.line(screen, BLACK, (character_x1 - 20, character_y1 + 100), (character_x1 + 20, character_y1 + 130), 6)  # Right leg
    pygame.draw.line(screen, BLACK, (character_x1 + 20, character_y1 + 130), (character_x1 + 35, character_y1 + 170), 6)  # Right calf



    pygame.draw.circle(screen, RED, (character_x, character_y - 30), 30)  # Head
    pygame.draw.line(screen, RED, (character_x, character_y), (character_x + 20, character_y + 100), 5)  # Body
    pygame.draw.line(screen, RED, (character_x + 3, character_y + 15), (character_x - 8, character_y + 65), 5)  # Left arm
    pygame.draw.line(screen, RED, (character_x - 8, character_y + 65), (character_x - 30, character_y + 45), 5)  # Left forearm
    pygame.draw.circle(screen, RED, (character_x - 30, character_y + 45), 7) # Left hand
    pygame.draw.line(screen, RED, (character_x + 3, character_y + 15), (character_x - 20, character_y + 40), 5)  # Right arm
    pygame.draw.line(screen, RED, (character_x - 20, character_y + 40), (character_x - 40, character_y + 20), 5)  # Right forearm
    pygame.draw.circle(screen, RED, (character_x - 40, character_y + 20), 7) # Right hand
    pygame.draw.line(screen, RED, (character_x + 20, character_y + 100), (character_x + 45, character_y + 170), 5)  # Left leg
    pygame.draw.line(screen, RED, (character_x + 20, character_y + 100), (character_x - 20, character_y + 130), 5)  # Right leg
    pygame.draw.line(screen, RED, (character_x - 20, character_y + 130), (character_x - 35, character_y + 170), 5)  # Right calf

    p1_bar = (p1Health / 100 ) * (WIDTH // 3)
    pygame.draw.rect(screen, RED, (WIDTH - p1_bar, 50, p1_bar, 20))
    
    p2_bar = (p2Health / 100 ) * (WIDTH // 3)
    pygame.draw.rect(screen, RED, (0, 50, p2_bar, 20))
    # Update the display
    pygame.display.flip()


def engine(screen, character_x, character_y, character_x1, character_y1, p1Jab, p1Health, p2Health):
    clock = pygame.time.Clock()
    frame = 0
    frameTracker1 = 0
    frameTracker2 = 0
    jabDuration = 6
    runSpeed = 4
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        frame += 1    
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            if p1Jab:
                p1Jab = False
                frameTracker1 = frame + jabDuration
                if character_x1 > character_x - 100: p1Health -= 5
        if keys[pygame.K_LEFT]: 
            left = True
            if character_x > 30 and character_x > character_x1 + 80: character_x -= runSpeed
            
            
        if keys[pygame.K_RIGHT]: 
            right = True
            if character_x < WIDTH - 50: character_x += runSpeed
            
        if keys[pygame.K_a]:
            if character_x1 > 50: character_x1 -= runSpeed
            
        if keys[pygame.K_d]:
            if character_x1 < WIDTH - 30 and character_x1 < character_x - 80: character_x1 += runSpeed

        drawCharacters(screen, character_x, character_y, character_x1, character_y1, p1Jab, p1Health, p2Health)
        clock.tick(30)
        if frame == frameTracker1: p1Jab = True
    pygame.quit()
    sys.exit()


def main():

    #initialize variables
    left = False
    right = False

    #set up the window and character placement
    screen, character_x, character_y, character_x1, character_y1, p1Jab, p1Health, p2Health = initialize()

    #run the game
    engine(screen, character_x, character_y, character_x1, character_y1, p1Jab, p1Health, p2Health)
 

main()
