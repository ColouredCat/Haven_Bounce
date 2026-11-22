
from AnimSprite import AnimSprite
import pygame as pg
from math import sin, cos, radians
from random import randint

class Enemy(AnimSprite):
    speed = 10

    def __init__(self, screen):
        height = pg.display.get_window_size()[1]
        self.start_y = randint(height // 4, (height//4)*3)
        
        super().__init__(screen, "sprites/birdMoving.png", 8, 16, 16, pg.display.get_window_size()[0], self.start_y)
        self.angle = 0
        self.tick = 0
        
        self.a = randint(-200, 200)
        self.b = randint(300, 500)

    def update(self, dt):
        
        self.angle = self.a * sin(radians(self.tick)/self.b)
        self.tick += 1

        self.rect.x -= cos(self.angle) * self.speed
        self.rect.y -= sin(self.angle) * self.speed

        self.animate(dt)
