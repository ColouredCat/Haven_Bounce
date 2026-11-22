
import pygame as pg

class StartScreen:
    def __init__(self, screen):
        self.sprite = pg.Surface.convert_alpha(pg.image.load("backgrounds/gameOver.png"))
        self.sprite = pg.transform.scale_by(self.sprite, 18)
        self.x = -60
        self.screen = screen
