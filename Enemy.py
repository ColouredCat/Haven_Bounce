
from AnimSprite import AnimSprite
import pygame as pg
from math import sin, cos
from random import randint
from utill import to_radians

class Enemy(AnimSprite):
    speed = 5

    def __init__(self, screen):
        super().__init__(screen, "test/knife.png", 2, 16, 32, pg.display.get_window_size()[0], 500)
        self.xflip = True
        self.angle = 0
        self.tick = 0
        
        self.a = randint(100, 160)
        self.b = randint(25, 40)

    def update(self):
        
        self.angle = self.a * sin(to_radians(self.tick)/self.b)
        self.tick += 1

        self.rect.x -= cos(self.angle) * speed
        self.rect.y -= sin(self.angle) * speed

        self.animate()
