import pygame
from creature import Creature
from bomb import Bomb
from text import text
from load_image import load_image
from terminate import terminate
import random
from creature import Creature
from  death import  death



def level_with_bombs(screen, num):
    # global start, death, score, screen

    main_sprite = pygame.sprite.Group()
    sprite = Creature(main_sprite, num)

    running_level_with_bombs1 = True
    center = (400, 400)
    all_sprites = pygame.sprite.Group()

    # Border(0, 0, width, 0)
    # Border(0, height, width, height)
    # Border(0, 0, 0, height)
    # Border(width, 0, width, height)

    text(screen, 'score: ' + str(sprite.score), (0, 0))

    corners = (30, 150, 270)
    sprite_bomb1 = Bomb(all_sprites, corners[0], screen, sprite)
    for i in range(2):
        Bomb(all_sprites, corners[i + 1], screen, sprite)

    stop_all = False
    all_sprites.draw(screen)
    fon = pygame.transform.scale(load_image('ship.jpg'), (800, 800))
    screen.blit(fon, (0, 0))
    num_of_death = 0
    alpha = 0
    alpha_up = True
    while running_level_with_bombs1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_level_with_bombs1 = False
                stop_all = True
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start:
            #     start = False
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not start:
            #     start = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q and sprite.death:
                sprite.death = False
                all_sprites = pygame.sprite.Group()
                corners = (30, 150, 270)
                sprite.score = 0
                sprite.rect.x = 400
                sprite.rect.y = 400

                sprite_bomb1 = Bomb(all_sprites, corners[0], screen, sprite)
                for i in range(2):
                    Bomb(all_sprites, corners[i + 1], screen, sprite)
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
                sprite.score += 2

        if not sprite.death:
            # screen.fill('#7986CB')
            screen.blit(fon, (0, 0))
            text(screen, 'score: ' + str(sprite.score), (0, 0))
            if sprite_bomb1.center_x >= 800 + sprite_bomb1.side + 50:
                sprite.score += 3
                text(screen, 'score: ' + str(sprite.score), (0, 0))
                if sprite.score >= 36:
                    return num_of_death
                side = random.randint(75, 320)
                center_x = -side - 40
                v_main = random.randint(5, 15)
                center_y = random.randint(side, 800 - side)
                all_sprites = pygame.sprite.Group()
                sprite_bomb1 = Bomb(all_sprites, corners[0], screen, sprite, (side, center_x, center_y, v_main))
                for i in range(2):
                    Bomb(all_sprites, corners[i + 1], screen, sprite, (side, center_x, center_y, v_main))
            all_sprites.update()
            all_sprites.draw(screen)
            main_sprite.update()
            main_sprite.draw(screen)
            pygame.display.flip()
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