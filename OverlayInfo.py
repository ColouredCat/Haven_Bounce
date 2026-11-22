import pygame as pg

class OverlayInfo:
    def __init__(self, screen):
        self.sprite = pg.Surface.convert_alpha(pg.image.load("backgrounds/overlay.png"))
        self.sprite = pg.transform.scale_by(self.sprite, 4)
        self.x = -620
        self.screen = screen