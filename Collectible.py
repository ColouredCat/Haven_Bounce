import pygame as pg
import random
from AnimSprite import AnimSprite

class Collectible(AnimSprite):
    collected = False
    rotate_speed = 2
    speed=3

    def __init__(self, screen):
        super().__init__(screen, "sprites/saltMoving.png", 3, 16, 16, random.uniform(0,1280), 0, 5, 4)
        self.angle = 0

    def update(self, dt):
        self.rect.y+=self.speed
        self.anim_count += dt
        anim_frame = (self.anim_count/60) // (1/self.fps)

        if anim_frame > self.frame_count:
            self.anim_count = 0
            anim_frame = 0

        frame_rect = pg.Rect(anim_frame * self.rect.width, 0, self.rect.width, self.rect.height)
        img = self.sprite.subsurface(frame_rect)
        img = pg.transform.rotate(img, self.angle)
        self.screen.blit(img, self.rect)

        self.angle += self.rotate_speed