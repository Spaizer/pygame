import pygame
import sys

pygame.init()

# Инициализация окна
def death(screen, pos, textt, alpha=0):
    screen.fill((255, 0, 0))

    font = pygame.font.Font('data/Boncegro FF 4F.otf', 50)
    text = font.render(textt, True, 'black')
    text.set_alpha(alpha)
    screen.blit(text, pos)



width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Плавное изменение прозрачности текста')

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Шрифт и размер текста
font = pygame.font.Font(None, 36)

# Создание текстовой поверхности
text = font.render('Пример текста', True, white)
text_rect = text.get_rect(center=(width // 2, height // 2))

# Начальная прозрачность
alpha = 0
alpha_up = True

# Основной цикл игры
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill(black)

    if alpha < 240 and alpha_up:
        alpha += 1
    if alpha == 240:
        alpha_up = False
    if not alpha_up:
        if alpha != 0:
            alpha -= 1
        else:
            alpha_up = True

    print(alpha, alpha_up)

    death(screen, (0, 0), 'deathhhhh', alpha)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для плавности
    pygame.time.delay(10)

    # Ограничение частоты кадров
    clock.tick(60)