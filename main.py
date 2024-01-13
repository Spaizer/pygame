import pygame

from text import text
from terminate import terminate
from start_screen import start_screen
from load_image import load_image

from level_1 import level_with_bombs
from level_2 import level_with_little_bad_fish
from level_3 import level_underwater_castle
from level_4 import level_cave
from level_5 import level_piranhas

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('В НЕИЗВЕДАННЫХ ВОДАХ')
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

if __name__ == '__main__':
    results = []
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)

    # выбор персонажа
    screen.fill('#5C6BC0')
    running_start = True
    image1_go_right = pygame.transform.scale(load_image("go_right.jpg", -1), (125, 60))
    image1_go_down = pygame.transform.scale(load_image("go_down.jpg", -1), (54, 60))
    image1_go_up = pygame.transform.scale(load_image("go_up.jpg", -1), (60, 60))
    image1_go_left = pygame.transform.flip(image1_go_right, True, False)

    image2_go_right = pygame.transform.scale(load_image("go_right2.png", -1), (125, 60))
    image2_go_down = pygame.transform.scale(load_image("go_down2.png", -1), (54, 60))
    image2_go_up = pygame.transform.scale(load_image("go_up2.png", -1), (60, 60))
    image2_go_left = pygame.transform.flip(image2_go_right, True, False)

    image3_go_right = pygame.transform.scale(load_image("go_right3.png", -1), (125, 60))
    image3_go_down = pygame.transform.scale(load_image("go_down3.png", -1), (54, 60))
    image3_go_up = pygame.transform.scale(load_image("go_up3.png", -1), (60, 60))
    image3_go_left = pygame.transform.flip(image3_go_right, True, False)

    coralls_background = pygame.transform.scale(load_image("coralls3_smoth.png", -1), (1600, 1005))

    running_hello_level = True
    screen.blit(coralls_background, (-400, 0))
    screen.blit(image1_go_right, (90, 200))
    screen.blit(image2_go_right, (330, 200))
    screen.blit(image3_go_right, (575, 200))
    pygame.draw.rect(screen, (255, 255, 255), (75, 330, 166, 100), width=0)
    pygame.draw.rect(screen, (255, 255, 255), (316, 330, 166, 100), width=0)
    pygame.draw.rect(screen, (255, 255, 255), (557, 330, 166, 100), width=0)
    pygame.draw.rect(screen, (0, 0, 0), (75, 330, 166, 100), width=2)
    pygame.draw.rect(screen, (0, 0, 0), (316, 330, 166, 100), width=2)
    pygame.draw.rect(screen, (0, 0, 0), (557, 330, 166, 100), width=2)
    text(screen, 'Выберите персонажа:', (10, 10))
    text(screen, 'Выбрать', (82, 360), font=45)
    text(screen, 'Выбрать', (327, 360), font=45)
    text(screen, 'Выбрать', (567, 360), font=45)
    stop_all = False
    num = None
    while running_hello_level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_hello_level = False
                stop_all = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if event.pos[1] >= 330 and event.pos[1] <= 430:
                    if event.pos[0] >= 75 and event.pos[0] <= 241:
                        num = 0
                    elif event.pos[0] >= 316 and event.pos[0] <= 482:
                        num = 1
                    elif event.pos[0] >= 557 and event.pos[0] <= 723:
                        num = 2
        if num is not None:
            break

        pygame.display.flip()

    # если не закрыли окно
    if not stop_all:
        # далее идут заставки между уровнями и сами уровни (уровни в отдельных функциях)
        start_screen(screen, ["СПРАВКА", "",
                              "Управление персонажем через стрелки",
                              ""
                              ], 'cave2.jpg', (800, 800), True)

        start_screen(screen, ["ПОДВОДНАЯ ПЕЩЕРА", "",
                              "Пещера не представляет особой опасности.",
                              "Чего тебе и стоит опасаться, так это водорослей,",
                              "растущих в пещере",
                              "Наткнёшься на них - и уже не выпутаешься",
                              "Так что будь осторожен",
                              "Течение в пещере сильное, бороться с ним нет смысла,",
                              "потому двигаться вперёд-назад у тебя не получится."], 'cave2.jpg', (800, 800), True)
        num_of_death = level_cave(screen, num)
        results.append(num_of_death)
        start_screen(screen, ["ПОДВОДНАЯ ПЕЩЕРА", "",
                              "Что ж, пещера пройдена,",
                              "но всё самое интересное только впереди", ''
                                                                        'Количество попыток: ' + str(num_of_death + 1)],
                     'cave2.jpg', (800, 800), True)
        start_screen(screen, ["ПОДВОДНЫЙ ЗАМОК", "",
                              "Никто точно не знает, как замок оказался под водой",
                              "однако уже много лет здесь проживает особая банда рыб.",
                              "Умом они не блещут, как и зрением.",
                              "Чтобы избежать неприятностей, тебе нужно",
                              "не попадаться всего 40 секунд,",
                              "затем путь дальше будет свободен"], 'castle.jpg', (800, 800))

        num_of_death = level_underwater_castle(screen, num)
        results.append(num_of_death)
        start_screen(screen, ["ПОДВОДНЫЙ ЗАМОК", "",
                              "Наконец ты отделался от этой банды",
                              "Правда, впереди тебя ещё ждут подобные встречи...",
                              'Но об этом позже', '',
                              'Количество попыток: ' + str(num_of_death + 1)], 'castle.jpg', (800, 800))

        start_screen(screen, ["ЗАТОНУВШИЙ КОРАБЛЬ", "",
                              "Много лет назад здесь затонул корабль",
                              "Пожалуй, таким тебя не удивить,",
                              "однако этот корабль особый, поскольку он",
                              "перевозил бомбы.",
                              "До сих пор они плавают здесь, а из-за сильного",
                              "течения, от бомб трудно уворачиваться.",
                              "Хорошие новости: бомб всего около 36, так что",
                              'советую повниматильней их считать!',
                              'На тот случай, если с арифметикой у тебя проблемы,',
                              'в левом верхнем углу будет счётчик бомб'], 'ship.jpg', (800, 800))

        num_of_death = level_with_bombs(screen, num)
        results.append(num_of_death)
        start_screen(screen, ["ЗАТОНУВШИЙ КОРАБЛЬ", "",
                              "Надеюсь, ты научился кое-каким приёмам при прохождении",
                              "этого уровня, так как они тебе очень понадобятся для",
                              'следующего уровня, где ты вновь встретишься с бандой рыб,',
                              'которые на самом деле не намного умнее этих бомб.', ''
                              'Количество попыток: ' + str(
                               num_of_death + 1)], 'ship.jpg', (800, 800))

        start_screen(screen, ["СРЕДИЗЕМНОМОРСКИЕ РАЗБОЙНИКИ", "",
                              "Пожалуй, одна из самых надоедливых банд.",
                              "Дело в том, что эти рыбы нападают большим количеством,",
                              "да и двигаются они непредсказуемо.",
                              "К счастью, они не могут противостоять",
                              "течению, потому, их движение подобно движению бомб.",
                              "Остаётся только пожелать тебе удачи,",
                              "поскольку она тебе пригодится)"], 'fon.jpg',
                     (1364, 800))
        num_of_death = level_with_little_bad_fish(screen, num)
        results.append(num_of_death)
        start_screen(screen, ["СРЕДИЗЕМНОМОРСКИЕ РАЗБОЙНИКИ", "",
                              "Удивлён, но ты всё же смог справиться", "с этим уровнем. Поздравляю!",
                              "",
                              'Количество попыток: ' + str(num_of_death + 1)], 'fon.jpg',
                     (1364, 800))

        start_screen(screen, ["БЛИЗКИЙ ПУТЬ К КОНЦУ", "",
                              "Молодец, ты почти прошёл",
                              "Но конечный враг на твоём пути к концу этого тоннеля",
                              "будут одинокие пираньи, которые давно никого не ели",
                              "тебе придётся от них уворачиваться. Плыви!",
                              "Запомни, если они начинают дёргаться, то немедленно плыви!"], 'fon.jpg',
                     (1364, 800))
        num_of_death = level_piranhas(screen, num)
        results.append(num_of_death)
        start_screen(screen, ["БЛИЗКИЙ ПУТЬ К КОНЦУ", "",
                              "Молодец, ты выжил. Теперь ты спокойно можешь ",
                              "плавать и жить как все остальные рыбы",
                              'Количество попыток: ' + str(num_of_death + 1)], 'fon.jpg',
                     (1364, 800))

        with open('results.txt', 'w') as file:
            for i in range(len(results)):
                file.write(str(i + 1) + ' уровень. Количество попыток: ' + str(results[i] + 1) + '\n')
        with open('results.txt', 'r') as file:
            data = file.readlines()
            data = ['РЕЗУЛЬТАТЫ'] + data
            start_screen(screen, data, 'cave2.jpg', (800, 800), True)
