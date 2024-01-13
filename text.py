import pygame


def text(screen, text, pos, font=50):
    font = pygame.font.Font(None, font)
    text = font.render(text, True, (0, 0, 0))
    screen.blit(text, pos)
