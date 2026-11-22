
import asyncio
import pygame as pg
<<<<<<< HEAD
from Player import Player
from Egg import Egg
=======
from Balloon import Balloon
>>>>>>> 46b2a45f5b54caae65e9e50f2e3a1a398c6fe65a

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
<<<<<<< HEAD

            self.player.update(events)
            self.egg.Update(events,self.egg.rect.x,20) # change this for actual balloon data

=======
            self.balloon.update(events)
>>>>>>> 46b2a45f5b54caae65e9e50f2e3a1a398c6fe65a
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

<<<<<<< HEAD
        self.player = Player(self.screen, 5)
        self.egg = Egg(self.screen)
=======
        self.balloon = Balloon(self.screen)
>>>>>>> 46b2a45f5b54caae65e9e50f2e3a1a398c6fe65a

        asyncio.run(self.mainloop())

g = Game()