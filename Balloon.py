
from AnimSprite import AnimSprite
import pygame as pg
from math import sin

class Balloon(AnimSprite):
    speed = 5

    def __init__(self, screen):
        width = pg.display.get_window_size()[0]
        start_x = width / 2
        self.start_y = 620
        self.tick = 0

        self.max_pos = width - (width/8)
        self.min_pos = (width/8)

        super().__init__(screen, "test/egg.png", 8, 16, 16, start_x, self.start_y, fps=8, scale=6)
        self.dx = 0

    def update(self, events):
        self.rect.y = self.start_y - 10 * sin(self.tick * 0.05)
        self.tick += 1

        for e in events:
            if e.type == pg.KEYDOWN:
                self.set_animation("test/egg.png", 8, fps=8)
                if e.key == pg.K_RIGHT:
                    self.dx = self.speed
                    self.xflip = False
                elif e.key == pg.K_LEFT:
                    self.dx = -self.speed
                    self.xflip = True
                    
            elif e.type == pg.KEYUP:
                self.set_animation("test/idle.png", 2, fps=2)
                self.xflip = False

                if e.key == pg.K_LEFT or e.key == pg.K_RIGHT:
                    self.dx = 0

        if self.rect.x <= self.max_pos and self.dx > 0:
            self.rect.x += self.dx
        if self.rect.x >= self.min_pos and self.dx < 0:
            self.rect.x += self.dx

        self.animate()