import pygame
from load_image import load_image


class Creature(pygame.sprite.Sprite):
    def __init__(self, group, num, level, slow=False):
        image1_go_right = pygame.transform.scale(load_image("go_right.jpg", -1), (125, 60))

        image2_go_right = pygame.transform.scale(load_image("go_right2.png", -1), (125, 60))

        image3_go_right = pygame.transform.scale(load_image("go_right3.png", -1), (125, 60))

        super().__init__(group)
        self.num = num
        if num == 0:
            self.image = image1_go_right
        elif num == 1:
            self.image = image2_go_right
        else:
            self.image = image3_go_right
        self.mask = pygame.mask.from_surface(self.image)
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
        self.death = False
        self.score = 0
        self.level = level

        self.slow = slow

    def update(self, *args):
        if args:
            image1_go_right = pygame.transform.scale(load_image("go_right.jpg", -1), (125, 60))
            image1_go_down = pygame.transform.scale(load_image("go_down.jpg", -1), (54, 60))
            image1_go_up = pygame.transform.scale(load_image("go_up.jpg", -1), (60, 60))
            image1_go_left = pygame.transform.flip(image1_go_right, True, False)

            image2_go_right = pygame.transform.scale(load_image("go_right2.png", -1), (125, 60))
            image2_go_down = pygame.transform.scale(load_image("go_down2.png", -1), (54, 60))
            image2_go_up = pygame.transform.scale(load_image("go_up2.png", -1), (60, 80))
            image2_go_left = pygame.transform.flip(image2_go_right, True, False)

            image3_go_right = pygame.transform.scale(load_image("go_right3.png", -1), (125, 60))
            image3_go_down = pygame.transform.scale(load_image("go_down3.png", -1), (54, 60))
            image3_go_up = pygame.transform.scale(load_image("go_up3.png", -1), (60, 80))
            image3_go_left = pygame.transform.flip(image3_go_right, True, False)
            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_DOWN and not self.go_down:
                # print('down')
                if self.level != 4:
                    if self.num == 0:
                        self.image = image1_go_down
                    elif self.num == 1:
                        self.image = image2_go_down
                    else:
                        self.image = image3_go_down
                if self.slow:
                    self.v_y = 25
                else:
                    self.v_y = 60
                self.go_down = True
            elif args[0].type == pygame.KEYUP and args[0].key == pygame.K_DOWN and self.go_down:
                self.v_y = 0
                self.go_down = False

            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_UP and not self.go_up:
                if self.level != 4:
                    if self.num == 0:
                        self.image = image1_go_up
                    elif self.num == 1:
                        self.image = image2_go_up
                    else:
                        self.image = image3_go_up
                if self.slow:
                    self.v_y = -25
                else:
                    self.v_y = -60
                self.go_up = True
            elif args[0].type == pygame.KEYUP and args[0].key == pygame.K_UP and self.go_up:
                self.v_y = 0
                self.go_up = False

            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_LEFT and not self.go_left:
                if self.num == 0:
                    self.image = image1_go_left
                elif self.num == 1:
                    self.image = image2_go_left
                else:
                    self.image = image3_go_left
                if self.slow:
                    self.v_x = -25
                else:
                    self.v_x = -60
                self.go_left = True
            elif args[0].type == pygame.KEYUP and args[0].key == pygame.K_LEFT and self.go_left:
                self.v_x = 0
                self.go_left = False

            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_RIGHT and not self.go_right:
                if self.num == 0:
                    self.image = image1_go_right
                elif self.num == 1:
                    self.image = image2_go_right
                else:
                    self.image = image3_go_right
                if self.slow:
                    self.v_x = 25
                else:
                    self.v_x = 60
                self.go_right = True
            elif args[0].type == pygame.KEYUP and args[0].key == pygame.K_RIGHT and self.go_right:
                self.v_x = 0
                self.go_right = False
            self.rect.y += self.v_y * self.clock_y.tick() / 100
            self.rect.x += self.v_x * self.clock_x.tick() / 100
            self.mask = pygame.mask.from_surface(self.image)
            # print('================', self.rect.x, self.rect.y, self.v_x, self.v_y)
        else:
            self.rect.y += self.v_y * self.clock_y.tick() / 100
            self.rect.x += self.v_x * self.clock_x.tick() / 100
            # print(self.rect.x, self.rect.y, self.v_x, self.v_y)
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 675:
            self.rect.x = 675
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 740:
            self.rect.y = 740
