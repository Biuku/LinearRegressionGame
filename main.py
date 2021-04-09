""" APRIL 7, 2021 """

"""
Today, I spent a lot of time learning trigonometry.
To refresh, check out my Jupyter notebook.
Changes made:
    - The line is defined by its mid point and compass angle
        - Math angles start at "East", 90 degrees = "South", etc.
    - Added rotation capability

"""



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
        self.rotating = False ## Rotate very slow -- 'd'
        self.counter_rotating = False ## Rotate very slow -- 'a'
        self.super_rotating = False ## Rotate very fast -- right-click


    """ EVENTS """

    def left_click_events(self):
        pygame.mouse.get_rel()
        self.moving = True

    def right_click_events(self):
        self.super_rotating = True

    def mouse_button_up_events(self):
        self.moving = False
        self.super_rotating = False

    def keydown_events(self, event):
        if event.key == pygame.K_a:
            self.counter_rotating = True

        if event.key == pygame.K_d:
            self.rotating = True

        if event.key == pygame.K_q:
            pygame.quit(), quit()


    def keyup_events(self, event):
        self.counter_rotating = False
        self.rotating = False


    """ UPDATES """

    def updates(self):
        #self.fitline.x_intercept()
        self.fitline.move(self.moving)
        self.fitline.rotate(self.rotating, self.counter_rotating, self.super_rotating)
        self.fitline.update_RSS(self.arr)
        self.draw()


    def draw(self):
        self.win.fill(self.set.white)
        self.plot.draw(self.arr)
        self.fitline.draw()
        self.update_screen()


    """ MAIN """
    def main(self):

        self.arr = np.load('data/ecommerce2.npy')
        #self.arr = self.plot.configure_data(self.arr)

        while True:
            self.win.fill(self.set.white)
            self.set.clock.tick(self.set.FPS)
            self.events()
            self.updates()

if __name__ == "__main__":
    x = Main()
    x.main()
