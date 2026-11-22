import pygame as pg
from AnimSprite import AnimSprite
class Egg (AnimSprite):
    vx=0
    vy=0
    ax=0
    ay=0.5

    def __init__(self, screen):
        super().__init__(screen, "test/egg.png", 8, 16, 16, 500, 500, 5, 4)
        return


    def Update(self, ev):

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
            self.rect.y=600
            self.vy=-10

        #add death and bounce logic here

        return
    
    def Render(self,screen):
        pg.draw.circle(screen,(255,0,0),[self.rect.x,self.rect.y],50,0)
        return