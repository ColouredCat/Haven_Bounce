import pygame as pg
from AnimSprite import AnimSprite
from Enemy import Enemy
from Collectible import Collectible

class Egg (AnimSprite):
    vx=0
    vy=0
    ax=0
    ay=0.5
    speed = 6

    double_jump=True
    dead = False

    def __init__(self, screen):
        super().__init__(screen, "sprites/egg.png", 8, 16, 16, pg.display.get_window_size()[0]/2, 500)


    def Update(self, ev, balloon_rect, dt):

        #pg.draw.rect(self.screen,(255,0,0),[balloon_x,600,size_x,100],0)

        vx=0

        self.animate(dt)

        for e in ev:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_w and self.double_jump:
                    self.vy=-10
                    self.double_jump=False

                if e.key == pg.K_s:
                    self.vy=20
            if e.type == pg.KEYUP:
                self.vx=0

        keys = pg.key.get_pressed()
        if(keys[pg.K_d]):
            self.vx=self.speed
        if(keys[pg.K_a]):
            self.vx=-self.speed
            
        self.vx += self.ax
        self.vy += self.ay
        self.rect.x += self.vx
        self.rect.y += self.vy

        if(self.rect.y>600):
            if(self.rect.colliderect(balloon_rect)):
                self.rect.y=600
                self.vy=-20
                self.double_jump=True
            elif(self.rect.y>700):
                self.rect.y=650
                self.dead = True

        return self.dead

    def EnemyCollision(self, e: Enemy, hitbox_x, hitbox_y):
        if(self.rect.x < e.rect.x + hitbox_x*0.5 
           and self.rect.x > e.rect.x - hitbox_x*0.5 
           and self.rect.y < e.rect.y + hitbox_y*0.5 
           and self.rect.y > e.rect.y - hitbox_y*0.5):
            self.dead=True
        return

    def CollectibleCollision(self, col: Collectible, hitbox_x, hitbox_y):
        if(self.rect.x < col.rect.x + hitbox_x*0.5 
                   and self.rect.x > col.rect.x - hitbox_x*0.5 
                   and self.rect.y < col.rect.y + hitbox_y*0.5 
                   and self.rect.y > col.rect.y - hitbox_y*0.5):
            return True
        return False