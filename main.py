""" APRIL 5, 2021 """

import pygame
import numpy as np
from setup.settings import Settings
from setup.background import Background
from plot import Plot
from line import FitLine

from setup.pygameBasics import PygameBasics

class Main(PygameBasics):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.fitline = FitLine(self.win)
        self.plot = Plot(self.win)

        self.arr = None
        self.line = (500, -1.4) # Tuple for intercept and slope
        self.mxmy = None

        self.moving = False
        self.rotating = False
        self.reverse_rotating = False


    """ EVENTS """

    def left_click_events(self):
        #pygame.mouse.get_rel()
        #self.moving = True

        self.reverse_rotating = True


    def right_click_events(self):
        #pygame.mouse.get_rel()
        self.rotating = True

    def mouse_button_up_events(self):
        self.moving = False
        self.rotating = False
        self.reverse_rotating = False

    def keydown_events(self, event):
        if event.key == pygame.K_q:
            pygame.quit(), quit()


    """ UPDATES """

    def updates(self):
        self.fitline.move(self.moving)
        self.fitline.rotate(self.rotating, self.reverse_rotating)
        self.draw()


    def draw(self):
        #self.plot.draw(self.arr) ## Turn off for trig stuff
        self.fitline.draw()
        self.update_screen()


    """ MAIN """
    def main(self):

        # self.arr = np.load('data/ecommerce.npy')
        #
        # MIT = pygame.image.load('mit.jpg')
        # degrees = 0

        while True:
            self.win.fill(self.set.white)

            # degrees += -1
            # rotated = pygame.transform.rotate(MIT, degrees)
            # self.win.blit(rotated, (800, 200))
            # pygame.display.flip()

            self.set.clock.tick(self.set.FPS)
            self.events()
            self.updates()

if __name__ == "__main__":
    x = Main()
    x.main()
