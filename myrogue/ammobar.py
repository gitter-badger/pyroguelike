import math
import pygame


class AmmoBar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.offset = (10, 10)
        self.pos = (10, 10)
        self.max_width = 200
        self.size = (self.max_width, 20)
        self.max_ammo = 10
        self.ammo = self.max_ammo
        self.bg_color = (0, 40, 0)
        self.bar_color = (0, 10, 240)
        self.background = pygame.Surface(self.size)
        self.background.fill(self.bg_color)
        self.bg_rect = self.background.get_rect()
        self.bg_rect.move_ip(self.pos)
        self.bar = pygame.Surface(self.size)
        self.bar.fill(self.bar_color)
        self.bar_rect = self.bar.get_rect()
        self.bar_rect.move_ip(self.pos)

        self.image = self.bar
        self.rect = self.bar_rect

    def inc_ammo(self, plus):
        self.ammo += plus

    def dec_ammo(self, minus):
        self.ammo -= minus

    def update(self, dt):
        self.bar_rect.right = self.pos[0] - self.offset[0]
        self.bar_rect.top = self.pos[1] + self.offset[1]
        new_bar_rect = self.bar_rect.copy()
        new_bar_rect.width = math.floor((self.ammo / self.max_ammo) * self.max_width)
        new_bar_rect = pygame.Rect((0, 0), self.size)
        new_bar_rect.width = math.floor((self.ammo / self.max_ammo) * self.max_width)

        self.bar.fill(self.bg_color)
        self.bar.fill(self.bar_color, rect=new_bar_rect)
