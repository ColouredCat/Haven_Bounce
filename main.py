
import asyncio
import pygame as pg
from Egg import Egg
from Balloon import Balloon
from Enemy import Enemy

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

            self.screen.fill("purple")

            events = pg.event.get()

            self.egg.Update(events, self.balloon.rect.x, self.balloon.rect.width)
            self.egg.EnemyCollision(self.enemy,16,32)

            self.balloon.update(events)

            self.enemy.update()
            run = self.check_exit(events)

            if(self.egg.dead):
                print("GAME OVER")
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
        self.egg = Egg(self.screen)
        self.balloon = Balloon(self.screen)
        self.enemy = Enemy(self.screen)

        asyncio.run(self.mainloop())

g = Game()