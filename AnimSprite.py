
import pygame as pg

class AnimSprite:
    def __init__(self, screen, img_source, frame_count, frame_width, frame_height, x, y, fps=5, scale=4):
        self.screen = screen
        self.scale = scale

        self.sprite = pg.Surface.convert_alpha(pg.image.load(img_source))
        self.sprite = pg.transform.scale_by(self.sprite, scale)
        self.rect = pg.Rect(x, y, frame_width*scale, frame_height*scale)

        self.anim_count = 0
        self.fps = fps
        self.frame_count = frame_count-1
        self.xflip = False
        self.yflip = False

    def set_animation(self, img_source, frame_count, fps=5):
        self.sprite = pg.Surface.convert_alpha(pg.image.load(img_source))
        self.sprite = pg.transform.scale_by(self.sprite, self.scale)

        self.anim_count = 0
        self.fps = fps
        self.frame_count = frame_count-1

    def animate(self):
        self.anim_count += 1
        anim_frame = (self.anim_count/60) // (1/self.fps)

        if anim_frame > self.frame_count:
            self.anim_count = 0
            anim_frame = 0

        img = pg.transform.flip(self.sprite, self.xflip, self.yflip)
        frame_rect = pg.Rect(anim_frame * self.rect.width, 0, self.rect.width, self.rect.height)
        self.screen.blit(img, self.rect, area=frame_rect)
