import pygame as pg
from AnimSprite import AnimSprite
class Egg (AnimSprite):
    vx=0
    vy=0
    ax=0
    ay=0

    def __init__(self, screen):  #deal with this Robert
        self.rect.x = 0
        self.rect.y = 0
        super().__init__(screen, "test/egg.png", 8, 16, 16, 500, 500)
        return


    def Update(self):
        self.vx += self.ax
        self.vy += self.ay
        self.rect.x += self.vx
        self.rect.y += self.vy

        #add death and bounce logic here

        return
    
    def Render(self,screen):
        pg.draw.circle(screen,(255,0,0),[self.rect.x,self.rect.y],50,0)
        return