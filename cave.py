import pygame
from load_image import load_image


class Cave(pygame.sprite.Sprite):
    def __init__(self, group, num):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.group = group
        if num == 0:
            image = pygame.transform.scale(load_image('cave.jpg'), (1603, 800))
        else:
            image = pygame.transform.scale(load_image('cave.jpg'), (1603, 800))
            image = pygame.transform.flip(image, True, False)
        self.image = image
        self.rect = self.image.get_rect()
        self.clock = pygame.time.Clock()
        self.v = 25
        self.rect.x = 0
        self.rect.y = 0
        self.num = num
        self.flag = False

    def update(self):
        # global death
        self.rect.x -= self.v * self.clock.tick() / 100
        if self.rect.x <= -800 and not self.flag:
            cave = Cave(self.group, int((self.num + 1) % 2))
            cave.rect.x = 800
            self.flag = True
