import pygame as pg
import random
from AnimSprite import AnimSprite

class Collectible(AnimSprite):
    collected = False
    def __init__(self, screen):
        super().__init__(screen, "test/egg.png", 8, 16, 16, random.uniform(0,1280), random.uniform(0,720), 5, 4)

    def update(self):
        self.animate()