import random

import pygame
from load_image import load_image
from text import text


class Laminaria(pygame.sprite.Sprite):
    def __init__(self, group, num, center, sprite, screen):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.group = group
        if num == 0:
            image = pygame.transform.scale(load_image('laminaria.png', -1), (200, 640))
        else:
            image = pygame.transform.scale(load_image('laminaria.png', -1), (200, 640))
            image = pygame.transform.flip(image, False, True)
        self.image = image
        self.rect = self.image.get_rect()
        self.clock = pygame.time.Clock()
        self.v = 20
        self.rect.x = 800
        if num == 0:
            self.rect.y = center + 50
        else:
            self.rect.y = center - 50 - 640
        self.mask = pygame.mask.from_surface(self.image)
        self.sprite = sprite
        self.screen = screen

    def update(self):
        # global death
        if self.rect.x < -900:
            self.v = 0
        else:
            self.rect.x -= self.v * self.clock.tick() / 100
            if pygame.sprite.collide_mask(self, self.sprite):
                self.screen.fill((255, 0, 0))
                text(self.screen, 'death', (0, 0))
                self.sprite.death = True

