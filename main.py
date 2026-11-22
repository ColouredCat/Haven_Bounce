
import asyncio
import time
import pygame as pg
from Egg import Egg
from Balloon import Balloon
from Enemy import Enemy
from Background import Background
from Collectible import Collectible
from GameOver import GameOver

class Game:
    screen_width = 1280
    screen_height = 720
    fps = 60

    def check_exit(self, events):
        for e in events:
            if e.type == pg.QUIT:
                return False
        return True

    def draw_text(self, text, x, y):
        s = self.font.render(text, False, pg.Color(0,0,0))
        self.screen.blit(s, (x, y))

    async def mainloop(self):
        run = True
        start = False
        score = 0
        dt = 0

        while run:

            time_since_start =(time.time()-self.start_time)
            if(time_since_start//(self.no_enemies*1.5+1)>self.no_enemies
               and time_since_start>4):
                self.enemies.append(Enemy(self.screen))
            self.no_enemies = len(self.enemies)

            self.bkg.scroll()

            events = pg.event.get()

            if(not self.egg.dead):
                self.egg.Update(events, self.balloon.rect.x, self.balloon.rect.width, dt)
                self.balloon.update(events, self.egg.rect, dt/(1/60))

            for col in range(self.no_collectibles):
                if(self.egg.rect.colliderect(self.collectibles[col].rect)):
                    del self.collectibles[col]
                    self.collectibles.append(Collectible(self.screen))
                    score += 1
                if (self.collectibles[col].rect.x<0):
                    del self.collectibles[col]
                    self.collectibles.append(Collectible(self.screen))
                self.collectibles[col].update(dt/(1/60))  

            for em in range(self.no_enemies):
                self.egg.EnemyCollision(self.enemies[em],80,100)
                if(self.enemies[em].rect.x<-64 or self.enemies[em].rect.y>720 or self.enemies[em].rect.y<-64):
                    del self.enemies[em]
                    self.enemies.append(Enemy(self.screen))
                self.enemies[em].update(dt/(1/60))

            #print(self.enemies, self.collectibles)


            run = self.check_exit(events)

            if(self.egg.dead):
                self.surface.fill((255,0,0,3))
                self.screen.blit(self.surface,(0,0))
                self.GameOver.screen.blit(self.GameOver.sprite, (self.GameOver.x, 0))
                self.GameOver.screen.blit(self.GameOver.sprite, (self.GameOver.x+self.GameOver.sprite.get_rect().width, 0))

            self.draw_text(str(score), 20, 20)

            dt = self.clock.tick(self.fps) / 1000
            pg.display.flip()
            await asyncio.sleep(0)

        pg.quit()
        pg.display.quit()
        pg.font.quit()
        pg.mixer.quit()

    def __init__(self):
        self.start_time = time.time()
        pg.init()
        pg.display.init()
        pg.font.init()
        pg.mixer.init()

        pg.display.set_mode((self.screen_width, self.screen_height))
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.font = pg.font.Font("fonts/font.ttf", 50)
        self.surface = pg.Surface((self.screen_width,self.screen_height), pg.SRCALPHA)

        self.balloon = Balloon(self.screen)
        self.collectibles = [Collectible(self.screen)]
        self.no_collectibles = len(self.collectibles)
        self.bkg = Background(self.screen)
        self.egg = Egg(self.screen)
        self.enemies = []
        self.no_enemies = len(self.enemies)

        self.GameOver = GameOver(self.screen)

        asyncio.run(self.mainloop())
        #

debug = False

if debug:
    import cProfile
    import pstats

    profiler = cProfile.Profile()
    profiler.enable()

g = Game()

if debug:
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats("cumulative")
    stats.print_stats(20)