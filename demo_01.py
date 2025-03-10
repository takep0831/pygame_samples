import pygame
from pygame.locals import Rect

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([700, 500])
pygame.display.set_caption("pygame demo - Hello!")

running = True
x1, y1 = 0, 2

# infinite loop top ----
while running:
    # press ctrl-c to stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 0))  # back ground color

    pygame.draw.circle(screen, (100, 100, 200), (500, 300), 150)
    pygame.draw.circle(screen, (255, 0, 0), (300, 100), 30)
    pygame.draw.circle(screen, (255, 0, 255), (300, 150), 30)
    pygame.draw.rect(screen, (0, 128, 0), Rect(100, 300, 100, 200))

    color_on = (248, 180, 120)
    color_off = (105, 105, 105)
    for x0 in range(7):
        for y0 in range(9):
            # pygame.draw.circle(screen, color_off, (24 + x0 * 16, 24 + y0 * 16), 8)
            pygame.draw.rect(screen, color_off, Rect(24 + x0 * 16, 24 + y0 * 16, 12, 12))

    # pygame.draw.circle(screen, color_on, (24 + x1 * 16, 24 + y1 * 16), 8)
    pygame.draw.rect(screen, color_on, Rect(24 + x1 * 16, 24 + y1 * 16, 12, 12))
    x1 += 1
    if x1 > 6:
        x1 = 0
        y1 += 1

    if y1 > 8:
        y1 = 0

    pygame.display.flip()  # update
    clock.tick(5)  # FPS, Frame Per Second
# infinite loop bottom ----

pygame.quit()
