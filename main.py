
import asyncio
import pygame as pg
from Egg import Egg
from Balloon import Balloon
from Enemy import Enemy
from Background import Background
from Collectible import Collectible

class Game:
    screen_width = 1280
    screen_height = 720
    fps = 60

    def check_exit(self, events):
        for e in events:
            if e.type == pg.QUIT:
                return False
        return True

    async def mainloop(self):
        run = True

        while run:

            self.bkg.scroll()

            events = pg.event.get()

            self.egg.Update(events, self.balloon.rect.x, self.balloon.rect.width)

            self.balloon.update(events, self.egg.rect)

            for col in range(self.no_collectibles):
                if(self.egg.CollectibleCollision(self.collectibles[col],45,45) 
                   or self.collectibles[col].rect.x<0): #change collectible hitbox here
                    del self.collectibles[col]
                    self.collectibles.append(Collectible(self.screen))
                self.collectibles[col].update()

            for em in range(self.no_enemies):
                self.egg.EnemyCollision(self.enemies[em],80,100)
                if(self.enemies[em].rect.x<0 or self.enemies[em].rect.y>720 or self.enemies[em].rect.y<0):
                    del self.enemies[em]
                    self.enemies.append(Enemy(self.screen))
                self.enemies[em].update()


            run = self.check_exit(events)

            if(self.egg.dead):
                print("GAME OVER",len(self.collectibles))
                pg.draw.circle(self.screen,[0,0,255],[50,50],20,0)

            self.clock.tick(self.fps)
            pg.display.update()
            await asyncio.sleep(0)

        pg.quit()
        pg.display.quit()
        pg.font.quit()
        pg.mixer.quit()

    def __init__(self):
        pg.init()
        pg.display.init()
        pg.font.init()
        pg.mixer.init()

        pg.display.set_mode((self.screen_width, self.screen_height))
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()

        self.balloon = Balloon(self.screen)
        self.collectibles = [Collectible(self.screen)]
        self.no_collectibles = len(self.collectibles)
        self.bkg = Background(self.screen)
        self.egg = Egg(self.screen)
        self.enemies = [Enemy(self.screen),Enemy(self.screen),Enemy(self.screen)]
        self.no_enemies = len(self.enemies)

        asyncio.run(self.mainloop())

g = Game()