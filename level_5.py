import pygame
import time
from text import text
import random
from load_image import load_image
from terminate import terminate
from creature import Creature
from clever_badfish import Clever_BadFish


def level_piranhas(screen, num):
    running_level = True
    # center = (400, 400)
    all_sprites = pygame.sprite.Group()

    main_sprite = pygame.sprite.Group()
    sprite = Creature(main_sprite, num, 3)

    text(screen, 'score: ' + str(sprite.score), (0, 0))

    data = ((50, 20), (50, 700), (600, 50), (600, 700))
    speed = (1, 2, 3, 5)
    for i in range(4):
        if data[i][0] < 400:
            vx = random.randint(15, 20)
        else:
            vx = random.randint(-20, -15)
        vy = random.randint(-20, 20)
        Clever_BadFish(all_sprites, data[i], vx, vy, screen, sprite, speed[i])
    stop_all = False
    all_sprites.draw(screen)
    fon = pygame.transform.scale(load_image('tunnel.jpg'), (800, 800))
    screen.blit(fon, (0, 0))
    time1 = time.time()
    num_of_death = 0
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
                sprite.rect.x = 400
                sprite.rect.y = 400
                num_of_death += 1

            #if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and not sprite.go_down:
                #main_sprite.update(event)
            #elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN and sprite.go_down:
               # main_sprite.update(event)

            #if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and not sprite.go_up:
              #  main_sprite.update(event)
            #elif event.type == pygame.KEYUP and event.key == pygame.K_UP and sprite.go_up:
               # main_sprite.update(event)

           # if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and not sprite.go_left:
              #  main_sprite.update(event)
          #  elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT and sprite.go_left:
           #     main_sprite.update(event)

          #  if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and not sprite.go_right:
            #    main_sprite.update(event)
          #  elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT and sprite.go_right:
            main_sprite.update(event)

        if not sprite.death:
            # screen.fill('#7986CB')
            screen.blit(fon, (0, 0))
            text(screen, 'time: ' + str(int(time.time() - time1)), (0, 0))
            all_sprites.update()
            all_sprites.draw(screen)
            main_sprite.update()
            main_sprite.draw(screen)
            pygame.display.flip()
            if time.time() - time1 > 8:
                return num_of_death
        else:
            text(screen, 'death', (0, 0))
    if stop_all:
        terminate()
