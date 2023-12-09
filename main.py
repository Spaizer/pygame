import pygame
from math import cos, sin, pi

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    screen2 = pygame.Surface(screen.get_size())
    running = True
    # drawing = False
    center = (400, 400)
    # x = 10
    move = False
    a = 70
    pygame.draw.circle(screen, (255, 255, 255), center, 10, width=0)
    pygame.draw.polygon(screen, (255, 255, 255),
                        (center, (400 + int(a * cos(15 * pi / 180)), 400 + int(a * sin(15 * pi / 180))),
                         (400 + int(a * cos(45 * pi / 180)), 400 + int(a * sin(45 * pi / 180)))),
                        width=0)
    pygame.draw.polygon(screen, (255, 255, 255),
                        (center, (400 + int(a * cos(255 * pi / 180)), 400 + int(a * sin(255 * pi / 180))),
                         (400 + int(a * cos(285 * pi / 180)), 400 + int(a * sin(285 * pi / 180)))),
                        width=0)
    pygame.draw.polygon(screen, (255, 255, 255),
                        (center, (400 + int(a * cos(135 * pi / 180)), 400 + int(a * sin(135 * pi / 180))),
                         (400 + int(a * cos(165 * pi / 180)), 400 + int(a * sin(165 * pi / 180)))),
                        width=0)
    corner1 = 15
    corner2 = 45
    corner3 = 255
    corner4 = 285
    corner5 = 135
    corner6 = 165
    start = False
    v = 50
    clock1 = pygame.time.Clock()
    clock2 = pygame.time.Clock()
    clock3 = pygame.time.Clock()
    clock4 = pygame.time.Clock()
    clock5 = pygame.time.Clock()
    clock6 = pygame.time.Clock()
    data = []
    drawing = False  # режим рисования выключен
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start = True
                v += 50
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                start = True
                v -= 50
        if start:
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (255, 255, 255), center, 10, width=0)
            corner1 += v * clock1.tick() / 100
            corner2 += v * clock2.tick() / 100
            corner3 += v * clock3.tick() / 100
            corner4 += v * clock4.tick() / 100
            corner5 += v * clock5.tick() / 100
            corner6 += v * clock6.tick() / 100
            corner1 = corner1 % 360
            corner2 = corner2 % 360
            corner3 = corner3 % 360
            corner4 = corner4 % 360
            corner5 = corner5 % 360
            corner6 = corner6 % 360
            pygame.draw.polygon(screen, (255, 255, 255),
                                (center, (400 + int(a * cos(corner1 * pi / 180)), 400 + int(a * sin(corner1 * pi / 180))),
                                 (400 + int(a * cos(corner2 * pi / 180)), 400 + int(a * sin(corner2 * pi / 180)))),
                                width=0)
            pygame.draw.polygon(screen, (255, 255, 255),
                                (center, (400 + int(a * cos(corner3 * pi / 180)), 400 + int(a * sin(corner3 * pi / 180))),
                                 (400 + int(a * cos(corner4 * pi / 180)), 400 + int(a * sin(corner4 * pi / 180)))),
                                width=0)
            pygame.draw.polygon(screen, (255, 255, 255),
                                (center, (400 + int(a * cos(corner5 * pi / 180)), 400 + int(a * sin(corner5 * pi / 180))),
                                 (400 + int(a * cos(corner6 * pi / 180)), 400 + int(a * sin(corner6 * pi / 180)))),
                                width=0)
            # рисуем на экране сохранённое на втором холсте

        pygame.display.flip()
    pygame.quit()
