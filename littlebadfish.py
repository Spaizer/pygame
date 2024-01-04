import pygame
from load_image import load_image
from math import sin, cos, pi
import random
from text import text


class LittleBadFish(pygame.sprite.Sprite):
    def __init__(self, group, corner, sprite, screen):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        image = pygame.transform.scale(load_image("little_bad_fish.png", -1), (85, 60))
        image = pygame.transform.flip(image, True, False)
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
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

        self.screen = screen
        self.sprite = sprite

    def update(self):
        image = pygame.transform.scale(load_image("little_bad_fish.png", -1), (85, 60))
        image = pygame.transform.flip(image, True, False)
        self.image = image
        self.corner += self.v_main * self.clock1.tick() / 100
        self.corner %= 360
        self.center_x += self.v_x * self.clock2.tick() / 100
        if self.center_x >= 800 + self.side + 50:
            self.sprite.score += 1
            text(self.screen, 'score: ' + str(self.sprite.score), (0, 0))
            self.side = random.randint(75, 320)
            self.center_x = -self.side - 40
            self.v_main = random.randint(5, 15)
            self.center_y = random.randint(self.side, 800 - self.side)
            self.clock1 = pygame.time.Clock()
            self.clock2 = pygame.time.Clock()
        self.rect.x = self.center_x + int(self.side * cos(self.corner * pi / 180)) - 25
        self.rect.y = self.center_y + int(self.side * sin(self.corner * pi / 180)) - 25
        if pygame.sprite.collide_mask(self, self.sprite):
            self.screen.fill((255, 0, 0))
            text(self.screen, 'death', (0, 0))
            # self.image = self.image_boom
            self.sprite.death = True
