import pygame

from load_image import load_image
from text import text

# класс противника для последнего уровня
class Clever_BadFish(pygame.sprite.Sprite):
    def __init__(self, group, pos, vx, vy, screen, sprite, speed):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        image_right = pygame.transform.scale(load_image("clever_bad_fish.png", -1), (151, 80))
        image_left = pygame.transform.flip(image_right, True, False)
        if pos[0] < 400:
            self.image = image_right
        else:
            self.image = image_left
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vx = vx
        self.vy = vy
        self.clock1 = pygame.time.Clock()
        self.clock2 = pygame.time.Clock()
        self.speed = speed

        self.sprite = sprite
        self.screen = screen

        self.spritex = sprite.rect.x
        self.spritey = sprite.rect.y


    def update(self):
        if self.rect.x < self.spritex:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.rect.y < self.spritey:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed
        self.clock1.tick(60)
        if self.rect.x == self.spritex:
            self.flag = False
        if self.rect.x < self.spritex + 5 and self.vx < 0:
            self.vx = -self.vx
            self.image = pygame.transform.flip(self.image, True, False)
        if self.rect.x > self.spritex + 5 and self.vx > 0:
            self.vx = -self.vx
            self.image = pygame.transform.flip(self.image, True, False)
        if self.rect.y < 0 and self.vy < 0:
            self.vy = -self.vy
        if self.rect.y > 720 and self.vy > 0:
            self.vy = -self.vy
        if pygame.sprite.collide_mask(self, self.sprite):
            self.screen.fill((255, 0, 0))
            text(self.screen, 'death', (0, 0))
            # self.image = self.image_boom
            self.sprite.death = True
        self.spritex = self.sprite.rect.x
        self.spritey = self.sprite.rect.y