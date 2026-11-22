import pygame as pg

class Overlay:
    def __init__(self, screen,x,size,file):
        self.sprite = pg.Surface.convert_alpha(pg.image.load(file))
        self.sprite = pg.transform.scale_by(self.sprite, size)
        self.x = x
        self.screen = screen