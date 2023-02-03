import pygame

# Initialize pygame
pygame.init()

# Set screen size and caption
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Pygame Chess Board")

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the chess board
    for i in range(16):
        for j in range(16):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, (10*(i+1),255,255), (i*40, j*40, 40, 40))
            else:
                pygame.draw.rect(screen, black, (i*40, j*40, 40, 40))
               
    # Update the screen
    pygame.display.update()