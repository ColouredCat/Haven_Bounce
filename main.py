
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

    def draw_text(self, text, x, y):
        s = self.font.render(text, False, pg.Color(0,0,0))
        self.screen.blit(s, (x, y))

    async def mainloop(self):
        run = True
        score = 0

        while run:

            self.bkg.scroll()

            events = pg.event.get()

            self.egg.Update(events, self.balloon.rect.x, self.balloon.rect.width)
            self.egg.EnemyCollision(self.enemy,16,32)

            self.balloon.update(events, self.egg.rect)

            for col in range(self.no_collectibles):
                if(self.egg.CollectibleCollision(self.collectibles[col],35,35)):
                    del self.collectibles[col]
                    self.collectibles.append(Collectible(self.screen))
                    score += 1
                if (self.collectibles[col].rect.x<0):
                    del self.collectibles[col]
                    self.collectibles.append(Collectible(self.screen))
                self.collectibles[col].update()

            self.enemy.update()
            run = self.check_exit(events)

            if(self.egg.dead):
                print("GAME OVER",len(self.collectibles))
                pg.draw.circle(self.screen,[0,0,255],[50,50],20,0)

            self.draw_text(str(score), 20, 20)

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
        self.font = pg.font.Font("fonts/font.ttf", 50)

        self.balloon = Balloon(self.screen)
        self.no_collectibles = 1
        self.collectibles = [Collectible(self.screen)]
        self.bkg = Background(self.screen)
        self.egg = Egg(self.screen)
        self.enemy = Enemy(self.screen)

        asyncio.run(self.mainloop())

g = Game()