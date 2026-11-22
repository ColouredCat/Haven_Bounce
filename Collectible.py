import pygame as pg
import random
from AnimSprite import AnimSprite

class Collectible(AnimSprite):
    collected = False
    rotate_speed = 2

    def __init__(self, screen):
        super().__init__(screen, "sprites/saltMoving.png", 3, 16, 16, random.uniform(1000,1280), random.uniform(300,600), 5, 4)
        self.angle = 0

    def update(self):
        self.rect.x-=10
        self.anim_count += 1
        anim_frame = (self.anim_count/60) // (1/self.fps)

        if anim_frame > self.frame_count:
            self.anim_count = 0
            anim_frame = 0

        frame_rect = pg.Rect(anim_frame * self.rect.width, 0, self.rect.width, self.rect.height)
        img = pg.transform.flip(self.sprite.subsurface(frame_rect), self.xflip, self.yflip)
        img = pg.transform.rotate(img, self.angle)
        self.screen.blit(img, self.rect)

        self.angle += self.rotate_speed