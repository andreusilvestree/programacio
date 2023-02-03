import pygame
pygame.init()
tamany = (640, 640)
blanc = (255,255,255)
negre = 0,0,0
blau = (0, 0, 255)
pantalla = pygame.display.set_mode(tamany)
pygame.display.set_caption("Exercici 1")
pantalla.fill(blanc)

for i in range(4):
    pygame.draw.circle(pantalla, blau, (320, 320), 70*i, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()