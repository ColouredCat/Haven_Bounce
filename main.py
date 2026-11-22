
import asyncio
import pygame as pg
from Balloon import Balloon

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
            self.balloon.update(events)
            run = self.check_exit(events)

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
        

        asyncio.run(self.mainloop())

g = Game()