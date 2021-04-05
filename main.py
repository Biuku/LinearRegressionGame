""" APRIL 5, 2021 """

import pygame
import numpy as np
from setup.settings import Settings
from setup.background import Background
from setup.background import FitLine

from setup.pygameBasics import PygameBasics

class Main(PygameBasics):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.fitline = FitLine(self.win)

        self.arr = None
        self.line = (500, -1.4) # Tuple for intercept and slope
        self.moving = False

        self.mxmy = None


    """ EVENTS """

    def mouse_button_down_events(self):
        self.moving = True
        pygame.mouse.get_rel()

    def mouse_button_up_events(self):
        self.moving = False

    def keydown_events(self, event):
        if event.key == pygame.K_q:
            pygame.quit(), quit()


    """ UPDATES """

    def updates(self):
        self.draw_plot()
        #self.calculateRSS()
        self.draw_fit_line()
        self.move_line()
        self.update_screen()


    def calculateRSS(self):
        pass

    def draw_fit_line(self):
        self.fitline.draw()

    def move_line(self):
        if self.moving:
            mx, my = pygame.mouse.get_rel()
            self.fitline.move(mx, my)
            

    def draw_plot(self):
        w, h = 1000, 500

        left, top = 200, 100
        right, bottom = left + w, top + h


        zero_zero = (left, bottom)

        pygame.draw.line(self.win, self.set.grey, (left, top), zero_zero, 2)
        pygame.draw.line(self.win, self.set.grey, zero_zero, (right, bottom), 2)

        for pair in self.arr:
            x = pair[0] + left
            y = pair[1] + top

            pygame.draw.circle(self.win, self.set.blue, (x,y), 2, 0)



    """ MAIN """
    def main(self):

        #self.arr = np.load("usa_housing_scaled.npy")
        self.arr = np.load("ecommerce.npy")

        #print(arr[:20])


        while True:
            self.win.fill(self.set.white)
            self.set.clock.tick(self.set.FPS)
            self.events()
            self.updates()

if __name__ == "__main__":
    x = Main()
    x.main()
