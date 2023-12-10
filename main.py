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
    image1_go_right = pygame.transform.scale(load_image("go_right.jpg", -1), (166, 80))
    image1_go_down = pygame.transform.scale(load_image("go_down.jpg", -1), (72, 80))
    image1_go_up = pygame.transform.scale(load_image("go_up.jpg", -1), (80, 80))
    image1_go_left = pygame.transform.flip(image1_go_right, True, False)

    image2_go_right = pygame.transform.scale(load_image("go_right2.png", -1), (166, 80))
    image2_go_down = pygame.transform.scale(load_image("go_down2.png", -1), (72, 80))
    image2_go_up = pygame.transform.scale(load_image("go_up2.png", -1), (80, 80))
    image2_go_left = pygame.transform.flip(image2_go_right, True, False)

    image3_go_right = pygame.transform.scale(load_image("go_right3.png", -1), (166, 80))
    image3_go_down = pygame.transform.scale(load_image("go_down3.png", -1), (72, 80))
    image3_go_up = pygame.transform.scale(load_image("go_up3.png", -1), (80, 80))
    image3_go_left = pygame.transform.flip(image3_go_right, True, False)

    def __init__(self, group, num):
        super().__init__(group)
        self.num = num
        if num == 0:
            self.image = Creature.image1_go_right
        elif num == 1:
            self.image = Creature.image2_go_right
        else:
            self.image = Creature.image3_go_right
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
                if self.num == 0:
                    self.image = Creature.image1_go_down
                elif num == 1:
                    self.image = Creature.image2_go_down
                else:
                    self.image = Creature.image3_go_down
                self.v_y = 50
                self.go_down = True
            elif args[0].type == pygame.KEYUP and args[0].key == pygame.K_DOWN and self.go_down:
                self.v_y = 0
                self.go_down = False

            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_UP and not self.go_up:
                if self.num == 0:
                    self.image = Creature.image1_go_up
                elif num == 1:
                    self.image = Creature.image2_go_up
                else:
                    self.image = Creature.image3_go_up
                self.v_y = -70
                self.go_up = True
            elif args[0].type == pygame.KEYUP and args[0].key == pygame.K_UP and self.go_up:
                self.v_y = 0
                self.go_up = False

            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_LEFT and not self.go_left:
                if self.num == 0:
                    self.image = Creature.image1_go_left
                elif num == 1:
                    self.image = Creature.image2_go_left
                else:
                    self.image = Creature.image3_go_left
                self.v_x = -70
                self.go_left = True
            elif args[0].type == pygame.KEYUP and args[0].key == pygame.K_LEFT and self.go_left:
                self.v_x = 0
                self.go_left = False

            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_RIGHT and not self.go_right:
                if self.num == 0:
                    self.image = Creature.image1_go_right
                elif num == 1:
                    self.image = Creature.image2_go_right
                else:
                    self.image = Creature.image3_go_right
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
        if self.rect.x > 634:
            self.rect.x = 634
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 720:
            self.rect.y = 720


def level_with_bombs():
    global start, death, score, screen
    running_level_with_bombs = True
    center = (400, 400)
    all_sprites = pygame.sprite.Group()

    score_f(screen)

    corners = (30, 150, 270)
    for i in range(3):
        Bomb(all_sprites, corners[i])

    stop_all = False
    all_sprites.draw(screen)
    screen.fill((0, 0, 255))
    start = True
    while running_level_with_bombs:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_level_with_bombs = False
                stop_all = True
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start:
            #     start = False
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not start:
            #     start = True

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
    if stop_all:
        pygame.quit()
        return False
    return True


if __name__ == '__main__':
    score = 0
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)

    # приветствие
    screen.fill('#5C6BC0')
    running_start = True
    image1_go_right = pygame.transform.scale(load_image("go_right.jpg", -1), (166, 80))
    image1_go_down = pygame.transform.scale(load_image("go_down.jpg", -1), (72, 80))
    image1_go_up = pygame.transform.scale(load_image("go_up.jpg", -1), (80, 80))
    image1_go_left = pygame.transform.flip(image1_go_right, True, False)

    image2_go_right = pygame.transform.scale(load_image("go_right2.png", -1), (166, 80))
    image2_go_down = pygame.transform.scale(load_image("go_down2.png", -1), (72, 80))
    image2_go_up = pygame.transform.scale(load_image("go_up2.png", -1), (80, 80))
    image2_go_left = pygame.transform.flip(image2_go_right, True, False)

    image3_go_right = pygame.transform.scale(load_image("go_right3.png", -1), (166, 80))
    image3_go_down = pygame.transform.scale(load_image("go_down3.png", -1), (72, 80))
    image3_go_up = pygame.transform.scale(load_image("go_up3.png", -1), (80, 80))
    image3_go_left = pygame.transform.flip(image3_go_right, True, False)

    running_hello_level = True
    screen.blit(image1_go_right, (75, 125))
    screen.blit(image2_go_right, (316, 125))
    screen.blit(image3_go_right, (557, 125))
    pygame.draw.rect(screen, (255, 255, 255), (75, 330, 166, 100), width=2)
    pygame.draw.rect(screen, (255, 255, 255), (316, 330, 166, 100), width=2)
    pygame.draw.rect(screen, (255, 255, 255), (557, 330, 166, 100), width=2)
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
        main_sprite = pygame.sprite.Group()
        sprite = Creature(main_sprite, num)

        # следующий уровень
        start = False
        death = False
        if level_with_bombs():  # опять проверяем, закрыто ли окно
            # следующий уровень
            pass

