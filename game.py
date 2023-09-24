import pygame
import sys

# Constants for the window dimensions
WIDTH = 1200
HEIGHT = 800


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (155, 155, 155)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 200, 255)


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


def drawCharacters(screen, character_x, character_y, character_x1, character_y1, p1Jab, p2Jab, p1Health, p2Health, frameTracker1, frameTracker2, p1Block, p2Block, p1HitStun, p2HitStun, p1BlockHealth, p2BlockHealth, p1Kick, p2Kick, p1Special, p2Special, p1Kame, p2Kame, p1KameX, p2KameX):

    # Clear the screen
    screen.fill(WHITE)
    
    font = pygame.font.Font(None, 36)

    # Draw the stick figure at the updated position
    if p1HitStun > 0:
        pygame.draw.circle(screen, GREY, (character_x1 - 3, character_y1 - 28), 30)  # Head
    else:
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
    if p1Kick:
            pygame.draw.line(screen, BLACK, (character_x1 + 20, character_y1 + 130), (character_x1 + 60, character_y1 + 155), 6)  # Right calf
    else:
        pygame.draw.line(screen, BLACK, (character_x1 + 20, character_y1 + 130), (character_x1 + 35, character_y1 + 170), 6)  # Right calf


    if p2HitStun > 0:
        pygame.draw.circle(screen, GREY, (character_x + 3, character_y - 28), 30)  # Head
    else:
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
    if p2Kick:
        pygame.draw.line(screen, RED, (character_x - 20, character_y + 130), (character_x - 60, character_y + 155), 5)  # Right calf
    else:
        pygame.draw.line(screen, RED, (character_x - 20, character_y + 130), (character_x - 35, character_y + 170), 5)  # Right calf

    p1_health = (p1Health / 100 ) * (WIDTH // 3)
    pygame.draw.rect(screen, RED, (0, 50, p1_health, 20))
    
    p2_health = (p2Health / 100 ) * (WIDTH // 3)
    pygame.draw.rect(screen, RED, (WIDTH - p2_health, 50, p2_health, 20))
    
    p1_block = (p1BlockHealth / 100) * (WIDTH // 5)
    pygame.draw.rect(screen, GREEN, (0, 80, p1_block, 15))
    
    p2_block = (p2BlockHealth / 100) * (WIDTH // 5)
    pygame.draw.rect(screen, GREEN, (WIDTH - p2_block, 80, p2_block, 15))
    
    if p1Special > 100: p1Special = 100
    if p2Special > 100: p2Special = 100
    p1_special = (p1Special / 100) * (WIDTH // 5)
    if p1Special == 100:
        pygame.draw.rect(screen, BLUE, (0, HEIGHT - 100, p1_special, 10))
    else: 
        pygame.draw.rect(screen, BLACK, (0, HEIGHT - 100, p1_special, 10))
    p2_special = (p2Special / 100) * (WIDTH // 5)
    if p2Special == 100:
        pygame.draw.rect(screen, BLUE, (WIDTH - p2_special, HEIGHT - 100, p2_special, 10))
    else: 
        pygame.draw.rect(screen, BLACK, (WIDTH - p2_special, HEIGHT - 100, p2_special, 10))
    # Update the display
    if p1Health <= .5 and p2Health <= .5:
        screen.fill(WHITE)
        text = font.render("TIE     press (r) to restart", True, (0,0,0))  # Text, antialiasing, color
        text_rect = text.get_rect()
        text_rect.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(text, text_rect)
    elif p1Health <= .5:
        screen.fill(WHITE)
        text = font.render("PLAYER 2 WINS   press (r) to restart", True, (0,0,0))  # Text, antialiasing, color
        text_rect = text.get_rect()
        text_rect.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(text, text_rect)
    elif p2Health <= .5:
        screen.fill(WHITE)
        text = font.render("PLAYER 1 WINS   press (r) to restart", True, (0,0,0))  # Text, antialiasing, color
        text_rect = text.get_rect()
        text_rect.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(text, text_rect)
    if p1Kame:
        pygame.draw.circle(screen, CYAN, (p1KameX, character_y + 10), 19)
    if p2Kame:
        pygame.draw.circle(screen, CYAN, (p2KameX, character_y + 10), 19)
    pygame.display.flip()

def engine(screen, character_x, character_y, character_x1, character_y1, p1Jab, p2Jab, p1Health, p2Health, gameOver, p1Block, p2Block):
    clock = pygame.time.Clock()
    frame = 0
    jabTracker1 = 0
    jabTracker2 = 0
    kickTracker1 = 0
    kickTracker2 = 0
    kickDuration = 8
    jabDuration = 13
    p1JabConnect = False
    p2JabConnect = False
    p1HitStun = 0
    p2HitStun = 0
    p1BlockHealth = 100
    p2BlockHealth = 100
    p1Kick = False
    p2Kick = False
    p1KickConnect = False
    p2KickConnect = False
    p1KickHit = False
    p2KickHit = False
    p1Kame = False
    p2Kame = False
    p1KameX = 0
    p2KameX = 0
    p1Special = 0
    p2Special = 0
    runSpeed = 5
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if p1Health <= .5 or p2Health <= .5:
            gameOver = True 
        frame += 1    
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: running = False
        if gameOver == False:
            if keys[pygame.K_c] and p1Jab and p1HitStun == 0 and not p1Kick:
                p1Jab = False
                    
            if keys[pygame.K_SLASH] and p2Jab and p2HitStun == 0 and not p2Kick:
                    p2Jab = False
            if keys[pygame.K_LEFT] and p2HitStun == 0: 
                if character_x > 30 and character_x > character_x1 + 80: character_x -= runSpeed
                
                
            if keys[pygame.K_RIGHT] and p2HitStun == 0: 
                if character_x < WIDTH - 50: character_x += runSpeed
                
            if keys[pygame.K_UP] and p2HitStun == 0:
                if p2Jab and not p2Kick:
                    p2Block = True
            else: p2Block = False
            if keys[pygame.K_DOWN] and p2HitStun == 0:
                if p2Jab and not p2Block:
                    p2Kick = True
            if keys[pygame.K_l] and p2Special >= 100:
                p2Kame = True
                p2KameX = character_x - 10
                p2Special = 0
            if keys[pygame.K_a] and p1HitStun == 0:
                if character_x1 > 50: character_x1 -= runSpeed
                
            if keys[pygame.K_d] and p1HitStun == 0:
                if character_x1 < WIDTH - 30 and character_x1 < character_x - 80: character_x1 += runSpeed
            
            if keys[pygame.K_w] and p1HitStun == 0:
                if p1Jab and not p1Kick:
                    p1Block = True
            else: p1Block = False
            
            if keys[pygame.K_s] and p1HitStun == 0:
                if p1Jab and not p1Block:
                    p1Kick = True
            if keys[pygame.K_q] and p1Special >= 100:
                p1Kame = True
                p1KameX = character_x1 + 10
                p1Special = 0
            if frame == kickTracker1:
                p1Kick = False
                kickTracker1 = 0
                p1KickConnect = False
            if frame == kickTracker2:
                p2Kick = False
                kickTracker2 = 0
                p2KickConnect = False  
            if frame == jabTracker1: 
                p1Jab = True
                jabTracker1 = 0
                p1JabConnect = False
            if frame == jabTracker2: 
                p2Jab = True
                jabTracker2 = 0
                p2JabConnect = False
            if not p1Jab and not p1JabConnect:
                jabTracker1 += 1
                if jabTracker1 == 4:
                    jabTracker1 = frame + jabDuration
                    p1JabConnect = True
                    if character_x1 > character_x - 120 and p2Health != 0: 
                        if not p2Block or p2BlockHealth < 20:
                            p2Health -= 5
                            p2HitStun = 1 
                            if p1Special != 100:
                                p1Special += 7
                        else: p2BlockHealth -= 20
            if not p2Jab and not p2JabConnect:
                jabTracker2 += 1
                if jabTracker2 == 4:
                    jabTracker2 = frame + jabDuration
                    p2JabConnect = True
                    if character_x < character_x1 + 120 and p1Health != 0: 
                        if not p1Block or p1BlockHealth < 20:
                            p1Health -= 5
                            p1HitStun = 1
                            if p2Special != 100:
                                p2Special += 7
                        else: p1BlockHealth -= 20
                            
            if p1Kick and not p1KickConnect:
                kickTracker1 += 1
                if kickTracker1 == 4:
                    kickTracker1 = frame + kickDuration
                    p1KickConnect = True
                    if character_x1 > character_x - 95 and p2Health != 0:
                        if p2Block or p2BlockHealth < 20:
                            p2Health -= 4
                            p2HitStun = 1
                            p1KickHit = True
                            if p1Special != 100:
                                p1Special += 7
                        else: p2BlockHealth -= 20
            if p2Kick and not p2KickConnect:
                kickTracker2 += 1
                if kickTracker2 == 4:
                    kickTracker2 = frame + kickDuration
                    p2KickConnect = True
                    if character_x < character_x1 + 95 and p1Health != 0:
                        if p1Block or p1BlockHealth < 20:
                            p1Health -= 4
                            p1HitStun = 1
                            p2KickHit = True
                            if p2Special != 100:
                                p2Special += 7
                        else: p1BlockHealth -= 20
        if gameOver == True:
            if keys[pygame.K_r]:
                main()
        if p1HitStun > 0:
            p1HitStun += 1
            if p1HitStun > 7:
                p1HitStun = 0
        if p2HitStun > 0:
            p2HitStun += 1
            if p2HitStun > 7:
                p2HitStun = 0
        if p1HitStun == 0 and not gameOver: 
            if p1Health < 100:
                p1Health += .05
            if p1BlockHealth < 100:
                p1BlockHealth += .2
        if p2HitStun == 0 and not gameOver: 
            if p2Health < 100:
                p2Health += .05
            if p2BlockHealth < 100:
                p2BlockHealth += .2
        if p1Kame: p1KameX += 6
        if p2Kame: p2KameX -= 6
        if p1KameX >= character_x - 10 and p1Kame:
            p1Kame = False
            p2Health -= 30
        if p2KameX <= character_x1 + 10 and p2Kame:
            p2Kame = False
            p1Health -= 30
        drawCharacters(screen, character_x, character_y, character_x1, character_y1, p1Jab, p2Jab, p1Health, p2Health, jabTracker1, jabTracker2, p1Block, p2Block, p1HitStun, p2HitStun, p1BlockHealth, p2BlockHealth, p1Kick, p2Kick, p1Special, p2Special, p1Kame, p2Kame, p1KameX, p2KameX)
        clock.tick(30)
        p1KickHit = False
        p2KickHit = False
        
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
