import os
import sys

import pygame
import random
from math import cos, pi, sin

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def score_f(screen, flag=False):
    if not flag:
        font = pygame.font.Font(None, 50)
        text = font.render('score: ' + str(score), True, (0, 0, 0))
        text_x = 0
        text_y = 0
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
    else:
        font = pygame.font.Font(None, 50)
        text = font.render('death', True, (0, 0, 0))
        text_x = 0
        text_y = 0
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = load_image("boom.png")

    def __init__(self, group, corner):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.corner = corner
        self.center_x = -400
        self.center_y = 400
        self.side = 300
        self.rect.x = self.center_x + int(self.side * cos(self.corner * pi / 180)) - 25
        self.rect.y = self.center_y + int(self.side * sin(self.corner * pi / 180)) - 25
        self.clock1 = pygame.time.Clock()
        self.clock2 = pygame.time.Clock()
        self.v_main = 10
        self.v_x = 15

    def update(self):
        global death, score
        self.image = Bomb.image
        if start:
            self.corner += self.v_main * self.clock1.tick() / 100
            self.corner %= 360
            self.center_x += self.v_x * self.clock2.tick() / 100
            if self.center_x >= 800 + self.side + 50:
                score += 1
                score_f(screen)
                self.side = random.randint(75, 320)
                self.center_x = -self.side - 40
                self.v_main = random.randint(5, 15)
                self.center_y = random.randint(self.side, 800 - self.side)
                self.clock1 = pygame.time.Clock()
                self.clock2 = pygame.time.Clock()
            self.rect.x = self.center_x + int(self.side * cos(self.corner * pi / 180)) - 25
            self.rect.y = self.center_y + int(self.side * sin(self.corner * pi / 180)) - 25
            if self.rect.colliderect(sprite.rect):
                screen.fill((255, 0, 0))
                score_f(screen, True)
                self.image = self.image_boom
                death = True


class Creature(pygame.sprite.Sprite):
    image = load_image("creature.png", -1)

    def __init__(self, group):
        super().__init__(group)
        self.image = Creature.image
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        self.go_up = False
        self.go_down = False
        self.go_left = False
        self.go_right = False
        self.clock_x = pygame.time.Clock()
        self.clock_y = pygame.time.Clock()
        self.v_x = 0
        self.v_y = 0

    def update(self, *args):
        if args:
            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_DOWN and not self.go_down:
                # print('down')
                self.v_y = 50
                self.go_down = True
            elif args[0].type == pygame.KEYUP and args[0].key == pygame.K_DOWN and self.go_down:
                self.v_y = 0
                self.go_down = False

            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_UP and not self.go_up:
                self.v_y = -70
                self.go_up = True
            elif args[0].type == pygame.KEYUP and args[0].key == pygame.K_UP and self.go_up:
                self.v_y = 0
                self.go_up = False

            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_LEFT and not self.go_left:
                self.v_x = -70
                self.go_left = True
            elif args[0].type == pygame.KEYUP and args[0].key == pygame.K_LEFT and self.go_left:
                self.v_x = 0
                self.go_left = False

            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_RIGHT and not self.go_right:
                self.v_x = 50
                self.go_right = True
            elif args[0].type == pygame.KEYUP and args[0].key == pygame.K_RIGHT and self.go_right:
                self.v_x = 0
                self.go_right = False
            self.rect.y += self.v_y * self.clock_y.tick() / 1000
            self.rect.x += self.v_x * self.clock_x.tick() / 1000
            # print('================', self.rect.x, self.rect.y, self.v_x, self.v_y)
        else:
            self.rect.y += self.v_y * self.clock_y.tick() / 100
            self.rect.x += self.v_x * self.clock_x.tick() / 100
            # print(self.rect.x, self.rect.y, self.v_x, self.v_y)
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 720:
            self.rect.x = 720
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 700:
            self.rect.y = 700


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    running = True
    # drawing = False
    center = (400, 400)
    # x = 10
    move = False
    score = 0
    all_sprites = pygame.sprite.Group()
    main_sprite = pygame.sprite.Group()
    sprite = Creature(main_sprite)
    score_f(screen)

    corners = (30, 150, 270)
    for i in range(3):
        Bomb(all_sprites, corners[i])


    start = False
    death = False
    all_sprites.draw(screen)
    screen.fill((0, 0, 255))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start:
                start = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not start:
                start = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q and death:
                death = False
                all_sprites = pygame.sprite.Group()
                corners = (30, 150, 270)
                score = 0
                for i in range(3):
                    Bomb(all_sprites, corners[i])

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

        if not death:
            screen.fill((0, 0, 255))
            score_f(screen)
            all_sprites.update()
            all_sprites.draw(screen)
            main_sprite.update()
            main_sprite.draw(screen)
            pygame.display.flip()
        else:
            score_f(screen, True)
    pygame.quit()
