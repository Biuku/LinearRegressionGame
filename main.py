""" APRIL 10, 2021 """

"""
April 10
1. Rename array_config "array".
    - I'm inheriting a shared object into separate objects. It's weird.
    - But ... array is static -- under principles of data science, it could never change.
        - you'd have to conduct more research
    - Drawbacks to placing array on top and saying it "has a" line and a plot:
        - Adds a layer ... messy
        - Unnecessary -- array is static
2. Do in array, draw in pixels
    - Do all math in array units
    - Then, just before drawing, convert to pixels.
    - I can't believe how dumb i've been to do math in pixels where y is reversed... unforced error.
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
        self.plot = Plot(self.win)

        """ LINE STUFF -- IGNORE FOR NOW """
        self.fitline = FitLine(self.win)
        self.line = (500, -1.4) # Tuple for intercept and slope
        self.mxmy = None

        self.moving = False
        self.rotating = False ## Rotate very slow -- 'd'
        # self.counter_rotate = False ## Rotate very slow -- 'a'
        # self.super_rotate = False ## Rotate very fast -- right-click


    """ EVENTS """

    def left_click_events(self):
        pygame.mouse.get_rel()
        self.moving = True

    def right_click_events(self):
        self.rotating = 3 ## Super rotate

    def mouse_button_up_events(self):
        self.moving = False
        self.rotating = False

    def keydown_events(self, event):

        if event.key == pygame.K_d:
            self.rotating = 0.1 ## clockwise

        if event.key == pygame.K_a:
            self.rotating = -0.1 ## Counter clockwise

        if event.key == pygame.K_c:
            self.fitline.snap_to_centroid()

        if event.key == pygame.K_q:
            pygame.quit(), quit()

    def keyup_events(self, event):
        self.rotating = False


    """ UPDATES """

    def updates(self):
        self.fitline.update(self.moving, self.rotating)
        self.draw()

    def draw(self):
        self.win.fill(self.set.white)
        self.plot.draw()
        self.fitline.draw()
        self.update_screen()


    """ MAIN """

    def main(self):
        while True:
            self.win.fill(self.set.white)
            self.set.clock.tick(self.set.FPS)
            self.events()
            self.updates()

if __name__ == "__main__":
    x = Main()
    x.main()
