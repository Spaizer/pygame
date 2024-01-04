import pygame
from load_image import load_image
from math import sin, cos, pi
from text import text


class Bomb(pygame.sprite.Sprite):
    def __init__(self, group, corner, screen, sprite, args=(300, -400, 400, 15)):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        image = load_image("bomb.png")
        image_boom = load_image("boom.png")
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.corner = corner
        self.side, self.center_x, self.center_y, self.v_main = args
        self.rect.x = self.center_x + int(self.side * cos(self.corner * pi / 180)) - 25
        self.rect.y = self.center_y + int(self.side * sin(self.corner * pi / 180)) - 25
        self.clock1 = pygame.time.Clock()
        self.clock2 = pygame.time.Clock()
        self.v_x = 25
        self.screen = screen
        self.sprite = sprite

    def update(self):
        # global death
        image = load_image("bomb.png")
        image_boom = load_image("boom.png")
        self.corner += self.v_main * self.clock1.tick() / 100
        self.corner %= 360
        self.center_x += self.v_x * self.clock2.tick() / 100
        self.rect.x = self.center_x + int(self.side * cos(self.corner * pi / 180)) - 25
        self.rect.y = self.center_y + int(self.side * sin(self.corner * pi / 180)) - 25
        if pygame.sprite.collide_mask(self, self.sprite):
            self.screen.fill((255, 0, 0))
            text(self.screen, 'death', (0, 0))
            self.image = image_boom
            self.sprite.death = True
