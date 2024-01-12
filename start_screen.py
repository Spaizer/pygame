from terminate import terminate
import pygame
from load_image import load_image
from creature import death
FPS = 50


def start_screen(screen, intro_text, name, scale, flag=False, font_name='data/Boncegro FF 4F.otf'):
    fon = pygame.transform.scale(load_image(name), scale)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(font_name, 30)
    text_coord = 90
    clock = pygame.time.Clock()

    print(intro_text[0], 123)
    string_rendered = pygame.font.Font(font_name, 55).render(intro_text[0], 1, pygame.Color('white' if flag else 'black'))
    screen.blit(string_rendered, (10, 60))
    for line in intro_text[1:]:
        if flag:
            string_rendered = font.render(line, 1, pygame.Color('white'))
        else:
            string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    alpha = 0
    alpha_up = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return  # начинаем игру

        pygame.display.flip()
        if alpha < 240 and alpha_up:
            alpha += 1
        if alpha == 240:
            alpha_up = False
        if not alpha_up:
            if alpha != 0:
                alpha -= 1
            else:
                alpha_up = True

        # screen.blit(pygame.font.Font('data/Boncegro FF 4F.otf', 42).render('[SPACE] ДЛЯ ПРОДОЛЖЕНИЯ', True, (255, 255, 255)), (160, 750))
        death(screen, (170, 750), '[SPACE] ДЛЯ ПРОДОЛЖЕНИЯ', alpha, color='White', color2='black', size=40)
        clock.tick(FPS)
