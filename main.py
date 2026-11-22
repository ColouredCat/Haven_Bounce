
import asyncio
import time
import pygame as pg
from Egg import Egg
from Balloon import Balloon
from Enemy import Enemy
from Background import Background
from Collectible import Collectible
from Overlay import Overlay
from AnimSprite import AnimSprite

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

    def setup(self):
        self.start_time = time.time()
        self.balloon = Balloon(self.screen)
        self.collectibles = [Collectible(self.screen)]
        self.no_collectibles = len(self.collectibles)
        self.bkg = Background(self.screen)
        self.egg = Egg(self.screen)
        self.enemies = []
        self.no_enemies = len(self.enemies)

    async def mainloop(self):
        run = True
        start = False
        score = 0
        dt = 0

        while run:

            if(not start and run):
                pg.mixer.music.load("audio/intro.ogg")
                pg.mixer.music.play(1)
                for i in range(18*60):
                    run = self.check_exit(pg.event.get())
                    self.intro.animate(1)
                    dt = self.clock.tick(self.fps)
                    pg.display.flip()
                    await asyncio.sleep(0)
                    if(not run):
                        break
                start=True
                pg.mixer.music.stop()
                pg.mixer.music.load("audio/music.ogg")
                pg.mixer.music.play(-1)

            time_since_start =(time.time()-self.start_time)
            if(time_since_start//(self.no_enemies*1.5+1)>self.no_enemies
               and time_since_start>4):
                self.enemies.append(Enemy(self.screen))
            self.no_enemies = len(self.enemies)

            self.bkg.scroll()

            events = pg.event.get()

            if(not self.egg.dead):
                self.egg.Update(events, self.balloon.rect, dt)
                self.balloon.update(events, self.egg.rect, dt/(1/60))

            for col in range(self.no_collectibles):
                if(self.egg.rect.colliderect(self.collectibles[col].rect)):
                    del self.collectibles[col]
                    self.collectibles.append(Collectible(self.screen))
                    score += 1
                if (self.collectibles[col].rect.y>720):
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
                pg.mixer.music.stop()
                pg.mixer.music.load("audio/death.ogg")
                pg.mixer.music.play(1, 1.85)
                self.surface.fill((255,0,0,3))
                self.screen.blit(self.surface,(0,0))
                self.GameOver.screen.blit(self.GameOver.sprite, (-60,100))
                pg.display.flip()
                await asyncio.sleep(3)
                score = 0
                self.setup()
                pg.mixer.music.stop()
                pg.mixer.music.load("audio/music.ogg")
                pg.mixer.music.play(-1)

            self.draw_text(str(score), 20, 20)
            self.overlay.screen.blit(self.overlay.sprite, (self.overlay.x+self.overlay.sprite.get_rect().width, 0))

            dt = self.clock.tick(self.fps) / 1000
            pg.display.flip()
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
        self.font = pg.font.Font("fonts/font.ttf", 50)
        self.surface = pg.Surface((self.screen_width,self.screen_height), pg.SRCALPHA)
        pg.mixer.music.set_volume(1)

        self.setup()

        self.GameOver = Overlay(self.screen,-1200,18,"backgrounds/gameOver.png")
        self.overlay = Overlay(self.screen,-500,3.5,"backgrounds/overlay.png")
        self.intro = AnimSprite(self.screen, "sprites/Intro.png", 7, 80, 45, 0, 0, 0.388, 16)
        self.slide_no=1

        asyncio.run(self.mainloop())

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