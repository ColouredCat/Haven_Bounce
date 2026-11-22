
from AnimSprite import AnimSprite
import pygame as pg
from math import sin

class Balloon(AnimSprite):
    speed = 5

    def __init__(self, screen):
        width = pg.display.get_window_size()[0]
        start_x = width / 2
        self.tick = 0

        super().__init__(screen, "sprites/balloonIdle.png", 6, 16, 16, start_x, 0, fps=8, scale=6)

        self.start_y = pg.display.get_window_size()[1] - 70
        self.rect.y = self.start_y

        self.max_pos = width - self.rect.width
        self.min_pos = 0
        self.dx = 0
        self.squish = False

    def update(self, events, egg_rect):
        if self.rect.colliderect(egg_rect):
            self.squish = True

        self.rect.y = self.start_y - 5 * sin(self.tick * 0.05)
        self.tick += 1

        for e in events:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_RIGHT:
                    self.dx = self.speed
                    self.set_animation("sprites/balloonMoving.png", 1, fps=8)
                    self.xflip = False
                elif e.key == pg.K_LEFT:
                    self.dx = -self.speed
                    self.set_animation("sprites/balloonMoving.png", 1, fps=8)
                    self.xflip = True
                    
            elif e.type == pg.KEYUP:
                if e.key == pg.K_LEFT or e.key == pg.K_RIGHT:
                    self.set_animation("sprites/balloonIdle.png", 6, fps=2)
                    self.xflip = False
                    self.dx = 0

        if self.squish:
            self.set_animation("sprites/balloonSquish.png", 6, fps=2)

        if self.rect.x <= self.max_pos and self.dx > 0:
            self.rect.x += self.dx
        if self.rect.x >= self.min_pos and self.dx < 0:
            self.rect.x += self.dx

        self.animate()