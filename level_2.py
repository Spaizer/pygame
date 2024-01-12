import pygame
from creature import Creature, death
from creature import Creature, moving
from littlebadfish import LittleBadFish
from text import text
from load_image import load_image
from terminate import terminate


def level_with_little_bad_fish(screen, num):
    running_level_with_bombs = True
    center = (400, 400)
    all_sprites = pygame.sprite.Group()

    main_sprite = pygame.sprite.Group()
    sprite = Creature(main_sprite, num, 2)

    # Border(0, 0, width, 0)
    # Border(0, height, width, height)
    # Border(0, 0, 0, height)
    # Border(width, 0, width, height)

    text(screen, 'score: ' + str(sprite.score), (0, 0))

    corners = (30, 150, 270)
    for i in range(3):
        LittleBadFish(all_sprites, corners[i], sprite, screen)

    stop_all = False
    all_sprites.draw(screen)
    fon = pygame.transform.scale(load_image('fon.jpg'), (1364, 800))
    screen.blit(fon, (0, 0))
    alpha = 0
    alpha_up = True
    while running_level_with_bombs:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_level_with_bombs = False
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
                for i in range(3):
                    LittleBadFish(all_sprites, corners[i], sprite, screen)
                sprite.rect.x = 400
                sprite.rect.y = 400

            moving(event, main_sprite, sprite)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                sprite.score += 2

        if not sprite.death:
            # screen.fill('#7986CB')
            screen.blit(fon, (0, 0))
            text(screen, 'score: ' + str(sprite.score), (0, 0))
            all_sprites.update()
            all_sprites.draw(screen)
            main_sprite.update()
            main_sprite.draw(screen)
            if sprite.score >= 24:
                return True
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
