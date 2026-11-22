
import pygame as pg

class Background:
    scroll_speed = 1

    def __init__(self, screen):
        self.sprite = pg.Surface.convert_alpha(pg.image.load("backgrounds/background.png"))
        self.sprite = pg.transform.scale_by(self.sprite, 8)
        self.x = 0
        self.screen = screen
    
    def scroll(self):
        if self.x == -self.sprite.get_rect().width:
            self.x = 0

        self.screen.blit(self.sprite, (self.x, 0))
        self.screen.blit(self.sprite, (self.x+self.sprite.get_rect().width, 0))
        self.x -= 1