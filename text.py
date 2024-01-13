import pygame


# добавление текста
def text(screen, text, pos, font=50):
    font = pygame.font.Font('data/Boncegro FF 4F.otf', font)
    text = font.render(text, True, (0, 0, 0))
    screen.blit(text, pos)
