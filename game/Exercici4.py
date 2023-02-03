import pygame
pygame.init()
pantalla = pygame.display.set_mode((400, 300))
x = 20
y = 20
x_velocitat = 1
y_velocitat = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += x_velocitat
    y += y_velocitat
    if x > pantalla.get_width() or x < 0:
        x_velocitat = -x_velocitat
    if y > pantalla.get_height() or y < 0:
        y_velocitat = -y_velocitat
    pantalla.fill((255, 255, 255))
    pygame.draw.circle(pantalla, (255, 0, 0), (x, y), 30)
    pygame.display.update()
pygame.quit()