import pygame


# заставка, если герой погибает
def death(screen, pos, textt, alpha=0, color=(255, 0, 0), color2='black', size=50):

    font = pygame.font.Font('data/Boncegro FF 4F.otf', size)
    text = font.render(textt, True, color)
    screen.blit(text, pos)

    font = pygame.font.Font('data/Boncegro FF 4F.otf', size)
    text = font.render(textt, True, color2)
    text.set_alpha(alpha)
    screen.blit(text, pos)
