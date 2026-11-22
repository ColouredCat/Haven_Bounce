
from AnimSprite import AnimSprite
import pygame as pg

class Player(AnimSprite):
    def __init__(self, screen, speed):
        super().__init__(screen, "test/egg.png", 8, 16, 16, 500, 50, fps=8, scale=6)
        self.speed = speed
        self.dx = 0
        self.dy = 0

    def update(self, events):

        for e in events:
            if e.type == pg.KEYDOWN:
                self.set_animation("test/egg.png", 8, fps=8)
                if e.key == pg.K_d:
                    self.dx = self.speed
                    self.xflip = False
                elif e.key == pg.K_a:
                    self.dx = -self.speed
                    self.xflip = True
                    
            elif e.type == pg.KEYUP:
                self.set_animation("test/idle.png", 2, fps=2)
                self.xflip = False

                if e.key == pg.K_d or e.key == pg.K_a:
                    self.dx = 0

        self.rect.x += self.dx
        self.rect.y += self.dy

        self.animate()