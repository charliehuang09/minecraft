import pygame
from math import pi

mapping = (
    (0,1,2,4,5,6),
    (2,5),
    (0,2,3,4,6),
    (0,2,3,5,6),
    (1,2,3,5),
    (0,1,3,5,6),
    (0,1,4,6,5,3),
    (0,2,5),
    (0,1,2,3,4,5,6),
    (0,1,2,3,5,6)
)

def drawStick(startingX, startingY, index):
    if (index == 0):
        pygame.draw.rect(screen, BLACK, [startingX, startingY, barWidth, barHeight]) # 0
    if (index == 1):
        pygame.draw.rect(screen, BLACK, [startingX - barHeight, startingY + barHeight, barHeight, barWidth]) # 1
    if (index == 2):
        pygame.draw.rect(screen, BLACK, [startingX + barWidth, startingY + barHeight, barHeight, barWidth]) # 2
    if (index == 3):
        pygame.draw.rect(screen, BLACK, [startingX ,startingY + barWidth + barHeight, barWidth, barHeight]) # 3
    if (index == 4):
        pygame.draw.rect(screen, BLACK, [startingX - barHeight, startingY + barHeight + barHeight + barWidth, barHeight, barWidth]) # 4
    if (index == 5):
        pygame.draw.rect(screen, BLACK, [startingX + barWidth, startingY + barHeight + barHeight + barWidth, barHeight, barWidth]) # 5
    if (index == 6):
        pygame.draw.rect(screen, BLACK, [startingX, startingY + barHeight + barWidth + barHeight + barWidth, barWidth, barHeight]) # 6

def drawDigit(startingX, startingY, num):
    for stick in mapping[num]:
        drawStick(startingX, startingY, stick)

# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [1200, 300]
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
    startingX = 50
    startingY = 40

    for n in range(10):
        drawDigit(startingX + n * (barWidth + barHeight * 3) , startingY, n)

    pygame.display.flip()
 
     
# Be IDLE friendly
pygame.quit()
