""" APRIL 12, 2021 """


import pygame
import numpy as np
from setup.settings import Settings
from setup.pygameBasics import PygameBasics
from plot import Plot
from line import FitLine


class Main(PygameBasics):
    def __init__(self):
        pygame.init()
        super().__init__()

        self.fitline = FitLine(self.win)
        self.plot = Plot(self.win)

        ## Flags
        self.moving = False
        self.rotating = False
        self.arr_units_flag = False
        self.show_intercepts_flag = False


    """ EVENTS """

    def left_click_events(self):
        pygame.mouse.get_rel()
        self.moving = True


    def right_click_events(self):
        self.rotating = -3 ## trig degrees are counter-clockwise. negative = clockwise

    def mouse_button_up_events(self):
        self.moving = False
        self.rotating = False

    def keydown_events(self, event):
        if event.key == pygame.K_a:
            self.rotating = 0.1 ## trig degrees are counter-clockwise. positive = counter clockwise

        if event.key == pygame.K_d:
            self.rotating = -0.1 ## trig degrees are counter-clockwise. negative = clockwise

        if event.key == pygame.K_c:
            self.fitline.snap_to_centroid()

        if event.key == pygame.K_t:
            self.arr_units_flag = not self.arr_units_flag

        if event.key == pygame.K_i:
            self.show_intercepts_flag = not self.show_intercepts_flag

        if event.key == pygame.K_q:
            pygame.quit(), quit()


    def keyup_events(self, event):
        self.rotating = False


    """ UPDATES """

    def updates(self):
        self.fitline.update(self.moving, self.rotating, self.arr_units_flag, self.show_intercepts_flag)
        self.draw()


    def draw(self):
        self.win.fill(self.set.white)
        self.draw_page_border()
        self.plot.draw()
        self.fitline.draw()

        pygame.display.update()


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
