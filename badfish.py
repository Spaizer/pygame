import pygame
from load_image import load_image
from text import text


class BadFish(pygame.sprite.Sprite):
    def __init__(self, group, pos, vx, vy, screen, sprite):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        image_right = pygame.transform.scale(load_image("bad_fish.png", -1), (151, 80))
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

        self.sprite = sprite
        self.screen = screen

    def update(self):
        self.rect.x += self.vx * self.clock1.tick() / 100
        self.rect.y += self.vy * self.clock2.tick() / 100
        if self.rect.x < 0 and self.vx < 0:
            self.vx = -self.vx
            self.image = pygame.transform.flip(self.image, True, False)
        if self.rect.x > 649 and self.vx > 0:
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
