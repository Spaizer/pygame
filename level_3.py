import pygame
import time
from text import text
import random
from load_image import load_image
from terminate import terminate
from creature import Creature
from badfish import BadFish
from  death import  death



def level_underwater_castle(screen, num):
    running_level = True
    # center = (400, 400)
    all_sprites = pygame.sprite.Group()

    main_sprite = pygame.sprite.Group()
    sprite = Creature(main_sprite, num, 3)

    text(screen, 'score: ' + str(sprite.score), (0, 0))

    data = ((50, 20), (50, 700), (600, 50), (600, 700))
    for i in range(4):
        if data[i][0] < 400:
            vx = random.randint(15, 20)
        else:
            vx = random.randint(-20, -15)
        vy = random.randint(-20, 20)
        BadFish(all_sprites, data[i], vx, vy, screen, sprite)

    stop_all = False
    all_sprites.draw(screen)
    fon = pygame.transform.scale(load_image('castle.jpg'), (800, 800))
    screen.blit(fon, (0, 0))
    time1 = time.time()
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
                data = ((50, 20), (50, 700), (600, 50), (600, 700))
                sprite.score = 0
                time1 = time.time()
                for i in range(4):
                    if data[i][0] < 400:
                        vx = random.randint(15, 25)
                    else:
                        vx = random.randint(-25, -15)
                    vy = random.randint(-25, 25)
                    BadFish(all_sprites, data[i], vx, vy, screen, sprite)
                sprite.rect.x = 400
                sprite.rect.y = 400
                num_of_death += 1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and not sprite.go_down:
                main_sprite.update(event)
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN and sprite.go_down:
                main_sprite.update(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and not sprite.go_up:
                main_sprite.update(event)
            elif event.type == pygame.KEYUP and event.key == pygame.K_UP and sprite.go_up:
                main_sprite.update(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not sprite.go_left:
                main_sprite.update(event)
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT and sprite.go_left:
                main_sprite.update(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and not sprite.go_right:
                main_sprite.update(event)
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT and sprite.go_right:
                main_sprite.update(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                time1 -= 2

        if not sprite.death:
            # screen.fill('#7986CB')
            screen.blit(fon, (0, 0))
            text(screen, 'time: ' + str(int(time.time() - time1)), (0, 0))
            all_sprites.update()
            all_sprites.draw(screen)
            main_sprite.update()
            main_sprite.draw(screen)
            pygame.display.flip()
            if time.time() - time1 > 40:
                return num_of_death
        else:
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

            death(screen, (170, 600), '[Q] ДЛЯ ПРОДОЛЖЕНИЯ', alpha)
            pygame.time.delay(2)
    if stop_all:
        terminate()