import pygame
from creature import Creature
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
            text(screen, 'death', (0, 0))
    if stop_all:
        terminate()
