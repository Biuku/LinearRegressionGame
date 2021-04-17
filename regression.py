""" April 17, 2021 """


import math as m
import random as r
import numpy as np

class Regression:
    def __init__(self, arr):
        self.arr = arr



    """ Regression stuff """
    """ Consider moving to other file """

    def update_RSS(self):
        rss = 1
        return

        error_lines = []
        self.arr_y_on_line = []
        self.arr_vertical_intercepts = []
        rss = 0

        for coord in self.arr:
            x, y = coord

            y_on_line = self.y_intercept(x, y)
            self.arr_y_on_line.append( y_on_line )

            intercept = [(x,y), y_on_line]
            self.arr_vertical_intercepts.append(intercept)

            rss += self.get_euclid(intercept[0], intercept[1])

        self.rss = rss


    def draw_intercepts(self):
        return
        if self.show_intercepts:

            self.printr.coord_printr("Intercepts Tracer", 1600, 400, self.set.red)

            for intercept in self.arr_y_on_line:
                x, y = self.convert_to_pixels(intercept)
                pygame.draw.circle(self.win, self.set.red, (x, y), 12, 0)

                print( intercept, (x,y) )


    def y_intercept(self, x2, y2):
        """ Supports update_RSS """

        x1, y1 = self.arr_start
        rads = m.radians(self.degrees)

        adj = x2 - x1
        hyp = adj / m.cos(rads)
        opp = m.sin(rads) * hyp

        return [int(x2), int(y1 - opp)]


    """ Utility """

    def get_euclid(self, start, fin):
        x1, y1 = start
        x2, y2 = fin

        for i in [x1, y1, x2, y2]:
            if i == 0:
                i == 0.1

        sol = (x2-x1)**2 + (y2-y1)**2
        if sol != 0:
            m.sqrt(sol)

        return sol
