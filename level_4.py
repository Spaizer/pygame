import pygame
import time
from text import text
import random
from load_image import load_image
from terminate import terminate
from cave import Cave
from creature import Creature
from  death import  death
from laminaria import Laminaria



def level_cave(screen, num):
    running_level = True
    # center = (400, 400)
    all_sprites = pygame.sprite.Group()
    borders = pygame.sprite.Group()

    main_sprite = pygame.sprite.Group()
    sprite = Creature(main_sprite, num, 4, True)
    sprite.rect.x = 200
    cave = Cave(all_sprites, 0)

    stop_all = False
    all_sprites.draw(screen)
    time_start = time.time()
    time1 = time.time()
    num1 = random.randint(2, 4)
    center = random.randint(200, 600)
    laminaria1 = Laminaria(borders, 0, center, sprite, screen)
    laminaria2 = Laminaria(borders, 1, center, sprite, screen)
    num_of_death = 0
    alpha = 0
    alpha_up = True
    while running_level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_level = False
                stop_all = True
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start:
            #     start = False
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not start:
            #     start = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q and sprite.death:
                sprite.death = False
                all_sprites = pygame.sprite.Group()
                cave = Cave(all_sprites, 0)

                time_start = time.time()

                sprite.rect.x = 200
                sprite.rect.y = 400
                num_of_death += 1

                borders = pygame.sprite.Group()
                time1 = time.time()
                num1 = random.randint(2, 4)
                center = random.randint(200, 600)
                laminaria1 = Laminaria(borders, 0, center, sprite, screen)
                laminaria2 = Laminaria(borders, 1, center, sprite, screen)

            if event.type == pygame.KEYDOWN and event.key in [pygame.K_DOWN, pygame.K_s] and not sprite.go_down:
                main_sprite.update(event)
            elif event.type == pygame.KEYUP and event.key in [pygame.K_DOWN, pygame.K_s] and sprite.go_down:
                main_sprite.update(event)

            if event.type == pygame.KEYDOWN and event.key in [pygame.K_UP, pygame.K_w] and not sprite.go_up:
                main_sprite.update(event)
            elif event.type == pygame.KEYUP and event.key in [pygame.K_UP, pygame.K_w] and sprite.go_up:
                main_sprite.update(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                time_start -= 2


        if not sprite.death:
            # screen.fill('#7986CB')
            text(screen, 'time: ' + str(int(time.time() - time_start)), (0, 0))
            all_sprites.update()
            all_sprites.draw(screen)

            borders.update()
            borders.draw(screen)

            main_sprite.update()
            main_sprite.draw(screen)
            pygame.display.flip()
            if time.time() - time_start > 40:
                return num_of_death
            if time.time() - time1 > num1:
                time1 = time.time()
                num1 = random.randint(2, 4)
                center = random.randint(200, 600)
                laminaria1 = Laminaria(borders, 0, center, sprite, screen)
                laminaria2 = Laminaria(borders, 1, center, sprite, screen)
        else:
            # alpha_serf = pygame.surface((300, 50))
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


            death(screen, (170,600), '[Q] ДЛЯ ПРОДОЛЖЕНИЯ', alpha)
            pygame.time.delay(2)
    if stop_all:
        terminate()