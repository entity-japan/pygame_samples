import pygame
from pygame.locals import Rect

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 640])
pygame.display.set_caption("pygame demo - window title here やで～")

running = True
x1, y1 = 0, 2

# infinite loop top ----
while running:
    # press ctrl-c to stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((220, 190, 75))  # back ground color

    pygame.draw.circle(screen, (0, 255, 255), (500, 400), 200)
    pygame.draw.circle(screen, (192, 192, 192), (500, 400), 125)
    pygame.draw.circle(screen, (0, 255, 0), (500, 400), 50)
    pygame.draw.rect(screen, (255, 255, 0), Rect(150, 150, 20, 300))

    color_on = (0, 255, 255)
    color_off = (255, 255, 255)
    for x0 in range(8):
        for y0 in range(10):
            # pygame.draw.circle(screen, color_off, (24 + x0 * 16, 24 + y0 * 16), 8)
            pygame.draw.rect(screen, color_off, Rect(24 + x0 * 16, 24 + y0 * 16, 12, 12))

    # pygame.draw.circle(screen, color_on, (24 + x1 * 16, 24 + y1 * 16), 8)
    pygame.draw.rect(screen, color_on, Rect(24 + x1 * 16, 24 + y1 * 16, 12, 12))
    x1 += 1
    if x1 > 4:
        x1 = 0

    pygame.display.flip()  # update
    clock.tick(5)  # FPS, Frame Per Second
# infinite loop bottom ----

pygame.quit()
