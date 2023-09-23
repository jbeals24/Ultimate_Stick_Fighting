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
    p2Jab = True
    
    p1Block = False
    p2Block = False
    
    gameOver = False

    return screen, character_x, character_y, character_x1, character_y1, p1Jab, p2Jab, p1Health, p2Health, gameOver, p1Block, p2Block


def drawCharacters(screen, character_x, character_y, character_x1, character_y1, p1Jab, p2Jab, p1Health, p2Health, frameTracker1, frameTracker2, p1Block, p2Block):

    # Clear the screen
    screen.fill(WHITE)
    
    font = pygame.font.Font(None, 36)

    # Draw the stick figure at the updated position
    pygame.draw.circle(screen, BLACK, (character_x1, character_y1 - 30), 30)  # Head
    pygame.draw.line(screen, BLACK, (character_x1, character_y1), (character_x1 - 20, character_y1 + 100), 6)  # Body
    if p1Block:
        pygame.draw.line(screen, BLACK, (character_x1 - 3, character_y1 + 15), (character_x1 + 15, character_y1 + 45), 5)  # Left arm
        pygame.draw.line(screen, BLACK, (character_x1 + 15, character_y1 + 45), (character_x1 + 15, character_y1 + 5), 5)  # Left forearm
        pygame.draw.circle(screen, BLACK, (character_x1 + 15, character_y1 + 5), 7) # Left hand
        pygame.draw.line(screen, BLACK, (character_x1 - 3, character_y1 + 15), (character_x1 + 25, character_y1 + 40), 5)  # Right arm
        pygame.draw.line(screen, BLACK, (character_x1 + 25, character_y1 + 40), (character_x1 + 25, character_y1 + 5), 5)  # Right forearm
        pygame.draw.circle(screen, BLACK, (character_x1 + 25, character_y1 + 5), 7) # Right hand
    elif p1Jab:
        pygame.draw.line(screen, BLACK, (character_x1 - 3, character_y1 + 15), (character_x1 + 8, character_y1 + 65), 6)  # Left arm
        pygame.draw.line(screen, BLACK, (character_x1 + 8, character_y1 + 65), (character_x1 + 30, character_y1 + 45), 6)  # Left forearm
        pygame.draw.circle(screen, BLACK, (character_x1 + 30, character_y1 + 45), 7) # Left hand
        pygame.draw.line(screen, BLACK, (character_x1 - 3, character_y1 + 15), (character_x1 + 20, character_y1 + 40), 6)  # Right arm
        pygame.draw.line(screen, BLACK, (character_x1 + 20, character_y1 + 40), (character_x1 + 40, character_y1 + 20), 6)  # Right forearm
        pygame.draw.circle(screen, BLACK, (character_x1 + 40, character_y1 + 20), 7) # Right hand
    else:
        if frameTracker1 == 1:
            pygame.draw.line(screen, BLACK, (character_x1 - 3, character_y1 + 15), (character_x1 + 13, character_y1 + 45), 6)  # Left arm
            pygame.draw.line(screen, BLACK, (character_x1 + 50, character_y1 + 15), (character_x1 + 35, character_y1 + 35), 6)  # Left forearm
            pygame.draw.circle(screen, BLACK, (character_x1 + 35, character_y1 + 35), 9) # Left hand
        elif frameTracker1 == 2:
            pygame.draw.line(screen, BLACK, (character_x1 + 13, character_y1 + 45), (character_x1 + 17, character_y1 + 40), 6)  # Left arm
            pygame.draw.line(screen, BLACK, (character_x1 + 35, character_y1 + 35), (character_x1 + 40, character_y1 + 25), 6)  # Left forearm
            pygame.draw.circle(screen, BLACK, (character_x1 + 40, character_y1 + 25), 9) # Left hand
        elif frameTracker1 == 3:
            pygame.draw.line(screen, BLACK, (character_x1 + 17, character_y1 + 40), (character_x1 + 25, character_y1 + 25), 6)  # Left arm
            pygame.draw.line(screen, BLACK, (character_x1 + 40, character_y1 + 25), (character_x1 + 55, character_y1 + 15), 6)  # Left forearm
            pygame.draw.circle(screen, BLACK, (character_x1 + 55, character_y1 + 15), 9) # Left hand
        else:
            pygame.draw.line(screen, BLACK, (character_x1 - 3, character_y1 + 15), (character_x1 + 50, character_y1 + 5), 6)  # Left arm
            pygame.draw.line(screen, BLACK, (character_x1 + 50, character_y1 + 5), (character_x1 + 90, character_y1 - 5), 6)  # Left forearm
            pygame.draw.circle(screen, BLACK, (character_x1 + 90, character_y1 - 5), 9) # Left hand
        pygame.draw.line(screen, BLACK, (character_x1 - 3, character_y1 + 15), (character_x1 + 20, character_y1 + 40), 6)  # Right arm
        pygame.draw.line(screen, BLACK, (character_x1 + 20, character_y1 + 40), (character_x1 + 40, character_y1 + 20), 6)  # Right forearm
        pygame.draw.circle(screen, BLACK, (character_x1 + 40, character_y1 + 20), 7) # Right hand
    pygame.draw.line(screen, BLACK, (character_x1 - 20, character_y1 + 100), (character_x1 - 45, character_y1 + 170), 6)  # Left leg
    pygame.draw.line(screen, BLACK, (character_x1 - 20, character_y1 + 100), (character_x1 + 20, character_y1 + 130), 6)  # Right leg
    pygame.draw.line(screen, BLACK, (character_x1 + 20, character_y1 + 130), (character_x1 + 35, character_y1 + 170), 6)  # Right calf



    pygame.draw.circle(screen, RED, (character_x, character_y - 30), 30)  # Head
    pygame.draw.line(screen, RED, (character_x, character_y), (character_x + 20, character_y + 100), 5)  # Body
    if p2Block:
        pygame.draw.line(screen, RED, (character_x + 3, character_y + 15), (character_x - 15, character_y + 45), 5)  # Left arm
        pygame.draw.line(screen, RED, (character_x - 15, character_y + 45), (character_x - 15, character_y + 5), 5)  # Left forearm
        pygame.draw.circle(screen, RED, (character_x - 15, character_y + 5), 7) # Left hand
        pygame.draw.line(screen, RED, (character_x + 3, character_y + 15), (character_x - 25, character_y + 40), 5)  # Right arm
        pygame.draw.line(screen, RED, (character_x - 25, character_y + 40), (character_x - 25, character_y + 5), 5)  # Right forearm
        pygame.draw.circle(screen, RED, (character_x - 25, character_y + 5), 7) # Right hand
    elif p2Jab:
        pygame.draw.line(screen, RED, (character_x + 3, character_y + 15), (character_x - 8, character_y + 65), 5)  # Left arm
        pygame.draw.line(screen, RED, (character_x - 8, character_y + 65), (character_x - 30, character_y + 45), 5)  # Left forearm
        pygame.draw.circle(screen, RED, (character_x - 30, character_y + 45), 7) # Left hand
        pygame.draw.line(screen, RED, (character_x + 3, character_y + 15), (character_x - 20, character_y + 40), 5)  # Right arm
        pygame.draw.line(screen, RED, (character_x - 20, character_y + 40), (character_x - 40, character_y + 20), 5)  # Right forearm
        pygame.draw.circle(screen, RED, (character_x - 40, character_y + 20), 7) # Right hand
    else:
        if frameTracker2 == 1:
            pygame.draw.line(screen, RED, (character_x + 3, character_y + 15), (character_x - 13, character_y + 45), 6)  # Left arm
            pygame.draw.line(screen, RED, (character_x - 50, character_y + 15), (character_x - 35, character_y + 35), 6)  # Left forearm
            pygame.draw.circle(screen, RED, (character_x - 35, character_y + 35), 9) # Left hand
        elif frameTracker2 == 2:
            pygame.draw.line(screen, RED, (character_x + 3, character_y + 45), (character_x - 17, character_y + 40), 6)  # Left arm
            pygame.draw.line(screen, RED, (character_x - 35, character_y + 35), (character_x - 40, character_y + 25), 6)  # Left forearm
            pygame.draw.circle(screen, RED, (character_x - 40, character_y + 25), 9) # Left hand
        elif frameTracker2 == 3:
            pygame.draw.line(screen, RED, (character_x - 17, character_y + 40), (character_x - 25, character_y + 25), 6)  # Left arm
            pygame.draw.line(screen, RED, (character_x - 40, character_y + 25), (character_x - 55, character_y + 15), 6)  # Left forearm
            pygame.draw.circle(screen, RED, (character_x - 55, character_y + 15), 9) # Left hand
        else:
            pygame.draw.line(screen, RED, (character_x + 3, character_y + 15), (character_x - 50, character_y + 5), 6)  # Left arm
            pygame.draw.line(screen, RED, (character_x - 50, character_y + 5), (character_x - 90, character_y - 5), 6)  # Left forearm
            pygame.draw.circle(screen, RED, (character_x - 90, character_y - 5), 9) # Left hand
        pygame.draw.line(screen, RED, (character_x + 3, character_y + 15), (character_x - 20, character_y + 40), 5)  # Right arm
        pygame.draw.line(screen, RED, (character_x - 20, character_y + 40), (character_x - 40, character_y + 20), 5)  # Right forearm
        pygame.draw.circle(screen, RED, (character_x - 40, character_y + 20), 7) # Right hand
    pygame.draw.line(screen, RED, (character_x + 20, character_y + 100), (character_x + 45, character_y + 170), 5)  # Left leg
    pygame.draw.line(screen, RED, (character_x + 20, character_y + 100), (character_x - 20, character_y + 130), 5)  # Right leg
    pygame.draw.line(screen, RED, (character_x - 20, character_y + 130), (character_x - 35, character_y + 170), 5)  # Right calf

    p1_bar = (p1Health / 100 ) * (WIDTH // 3)
    pygame.draw.rect(screen, RED, (0, 50, p1_bar, 20))
    
    p2_bar = (p2Health / 100 ) * (WIDTH // 3)
    pygame.draw.rect(screen, RED, (WIDTH - p2_bar, 50, p2_bar, 20))
    # Update the display
    if p1Health == 0 and p2Health == 0:
        screen.fill(WHITE)
        text = font.render("TIE     press (r) to restart", True, (0,0,0))  # Text, antialiasing, color
        text_rect = text.get_rect()
        text_rect.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(text, text_rect)
    elif p1Health == 0:
        screen.fill(WHITE)
        text = font.render("PLAYER 2 WINS   press (r) to restart", True, (0,0,0))  # Text, antialiasing, color
        text_rect = text.get_rect()
        text_rect.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(text, text_rect)
    elif p2Health == 0:
        screen.fill(WHITE)
        text = font.render("PLAYER 1 WINS   press (r) to restart", True, (0,0,0))  # Text, antialiasing, color
        text_rect = text.get_rect()
        text_rect.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(text, text_rect)
    pygame.display.flip()


def engine(screen, character_x, character_y, character_x1, character_y1, p1Jab, p2Jab, p1Health, p2Health, gameOver, p1Block, p2Block):
    clock = pygame.time.Clock()
    frame = 0
    frameTracker1 = 0
    frameTracker2 = 0
    jabDuration = 8
    p1JabConnect = False
    p2JabConnect = False
    p1HitStun = 0
    p2HitStun = 0
    
    runSpeed = 5
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if p1Health <= 0 or p2Health <= 0:
            gameOver = True 
        frame += 1    
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: running = False
        if gameOver == False:
            if keys[pygame.K_c] and p1Jab:
                p1Jab = False
                    
            if keys[pygame.K_SLASH] and p2Jab:
                if frameTracker1 - frame > 0 or frameTracker2 - frame < -10:
                    p2Jab = False
            if keys[pygame.K_LEFT]: 
                left = True
                if character_x > 30 and character_x > character_x1 + 80: character_x -= runSpeed
                
                
            if keys[pygame.K_RIGHT]: 
                right = True
                if character_x < WIDTH - 50: character_x += runSpeed
                
            if keys[pygame.K_UP]:
                p2Block = True
            else: p2Block = False
            if keys[pygame.K_a]:
                if character_x1 > 50: character_x1 -= runSpeed
                
            if keys[pygame.K_d]:
                if character_x1 < WIDTH - 30 and character_x1 < character_x - 80: character_x1 += runSpeed
            
            if keys[pygame.K_w]:
                p1Block = True
            else: p1Block = False
                
            if frame == frameTracker1: 
                p1Jab = True
                frameTracker1 = 0
                p1JabConnect = False
            if frame == frameTracker2: 
                p2Jab = True
                frameTracker2 = 0
                p2JabConnect = False
            if not p1Jab and not p1JabConnect:
                frameTracker1 += 1
                if frameTracker1 == 4:
                    frameTracker1 = frame + jabDuration
                    p1JabConnect = True
                    if character_x1 > character_x - 120 and p2Health != 0 and not p2Block: 
                        p2Health -= 5
                        p2HitStun = True
            if not p2Jab and not p2JabConnect:
                frameTracker2 += 1
                if frameTracker2 == 4:
                    frameTracker2 = frame + jabDuration
                    p2JabConnect = True
                    if character_x < character_x1 + 120 and p1Health != 0 and not p1Block: 
                        p1Health -= 5
                        p2HitStun = True
                    
        if gameOver == True:
            if keys[pygame.K_r]:
                main()
        drawCharacters(screen, character_x, character_y, character_x1, character_y1, p1Jab, p2Jab, p1Health, p2Health, frameTracker1, frameTracker2, p1Block, p2Block)
        clock.tick(30)
        
    pygame.quit()
    sys.exit()


def main():

    #initialize variables
    left = False
    right = False

    #set up the window and character placement
    screen, character_x, character_y, character_x1, character_y1, p1Jab, p2Jab, p1Health, p2Health, gameOver, p1Block, p2Block = initialize()

    #run the game
    engine(screen, character_x, character_y, character_x1, character_y1, p1Jab, p2Jab, p1Health, p2Health, gameOver, p1Block, p2Block)
 

main()
