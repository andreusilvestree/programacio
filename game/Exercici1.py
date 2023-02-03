import pygame
pygame.init()
tamany = (640, 640)
blanc = (255,255,255)
negre = 0,0,0
pantalla = pygame.display.set_mode(tamany)
pygame.display.set_caption("Exercici 1")
pantalla.fill(blanc)

for i in range(6):
    pygame.draw.circle(pantalla, negre, (320, 320), 50*i, 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()