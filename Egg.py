import pygame as pg
from AnimSprite import AnimSprite
from Enemy import Enemy
from Collectible import Collectible

class Egg (AnimSprite):
    vx=0
    vy=0
    ax=0
    ay=0.5

    dead=False

    def __init__(self, screen):
        super().__init__(screen, "test/egg.png", 8, 16, 16, 500, 500, 5, 4)
        return


    def Update(self, ev, balloon_x, size_x):
        self.dead = False

        pg.draw.rect(self.screen,(255,0,0),[balloon_x,600,size_x,100],0)

        vx=0

        self.animate()

        for e in ev:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_d:
                    self.vx=10
                if e.key == pg.K_a:
                    self.vx=-10
            if e.type == pg.KEYUP:
                self.vx=0
            
        self.vx += self.ax
        self.vy += self.ay
        self.rect.x += self.vx
        self.rect.y += self.vy

        if(self.rect.y>600):
            if(self.rect.x<balloon_x+size_x*0.5 and self.rect.x>balloon_x-size_x*0.5):
                self.rect.y=600
                self.vy=-10
            else:
                self.vy=-30
                self.dead = True

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