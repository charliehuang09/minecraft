import pygame
from math import pi
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("LED Digit")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)
      
    # Draw a solid rectangle
    barWidth = 50
    barHeight = 20
    startingX = 150
    startingY = 10

    pygame.draw.rect(screen, BLACK, [startingX, startingY, barWidth, barHeight]) # 0
    pygame.draw.rect(screen, BLACK, [startingX - barHeight, startingY + barHeight, barHeight, barWidth]) # 1
    # pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    # pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    # pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    # pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    # pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

    pygame.display.flip()
 
     
# Be IDLE friendly
pygame.quit()