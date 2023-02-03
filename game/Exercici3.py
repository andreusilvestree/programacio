import pygame
pygame.init()
tamany = (640, 640)
blanc = (255,255,255)
negre = 0,0,0
blau = (0, 0, 255)
colore = [(0,0,0), (255, 215, 0), (255,0,0), blau, negre]
pantalla = pygame.display.set_mode(tamany)
pygame.display.set_caption("Exercici 1")
pantalla.fill(blanc)
a = 0
for i in range(11):
    color = negre
    if i <= 4:
        pygame.draw.circle(pantalla, colore[i], (320, 320), 20*(i+a), 40)
    if i == 7:
        color = blanc
    a = a+1
    pygame.draw.circle(pantalla, color, (320, 320), 20*i, 2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()