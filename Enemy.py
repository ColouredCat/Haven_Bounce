
from AnimSprite import AnimSprite
import pygame as pg

class Enemy(AnimSprite):
    speed = 5

    def __init__(self, screen):
        super().__init__(screen, "test/knife.png", 2, 16, 32, pg.display.get_window_size()[0], 500)
        self.xflip = True

    def update(self):
        self.rect.x -= self.speed
        self.animate()