""" April 11, 2021 """


import pygame
import math as m
import random as r
from setup.printr import Printr
from arr import Arr


class FitLine(Arr):
    def __init__(self, win):
        pygame.init()
        self.win = win
        super().__init__()
        self.printr = Printr(self.win, self.set)

        ## Pixel var's
        self.length = 500
        self.for_angle = 25 ## 'angle' for trig; 'slope' for regression
        self.opp_angle = 205
        self.mid = [600, 400]

        ## Array var's
        self.update_end_points()
        self.update_RSS()



    def update(self, moving, rotating):
        self.move(moving)
        self.rotate(rotating)
        self.update_end_points()


    def move(self, moving):
        if moving:
            mx, my = pygame.mouse.get_rel()
            self.mid[0] += mx
            self.mid[1] += my
            self.update_RSS()


    def rotate(self, rotating):
        def wrap_angle(angle):
            if angle > 360:
                return angle - 360
            return angle

        if rotating:
            self.for_angle += rotating
            self.for_angle = wrap_angle(self.for_angle)

            self.opp_angle = self.for_angle + 180
            self.opp_angle = wrap_angle(self.opp_angle)

            self.update_RSS()


    def update_end_points(self):
        """ Update the start and end points if line moves/rotates"""

        x, y = self.mid
        for_rads = m.radians(self.for_angle)
        opp_rads = m.radians(self.opp_angle)

        ## Update start coordinatese
        start_x = x + ( m.cos(opp_rads) * self.length )
        start_y = y + ( m.sin(opp_rads) * self.length )
        self.pixel_start = (start_x, start_y)

        ## Update end coords
        end_x = x + ( m.cos(for_rads) * self.length )
        end_y = y + ( m.sin(for_rads) * self.length )
        self.pixel_end = (end_x, end_y)


    def snap_to_centroid(self):
        self.mid = self.get_centroid()


    def draw(self):

        ### Draw line in two halves
        pygame.draw.line(self.win, self.set.blue, tuple(self.pixel_start), tuple(self.mid), 4)
        pygame.draw.line(self.win, self.set.red, tuple(self.mid), tuple(self.pixel_end), 4)

        #self.draw_intercepts()
        self.printr.print_coord(self.mid[0], self.mid[1])
        self.printr.print_instructions(self.for_angle, self.opp_angle, self.rss)


    def draw_intercepts(self):

        for line in self.vertical_intercepts:
            start, end = line
            start = tuple( self.convert_arr_to_pixels(start) )
            end = tuple( self.convert_arr_to_pixels(end) )
            pygame.draw.line(self.win, self.set.blue, start, end, 1)

            ## Draw vertical lines between the error bars and my line
            #for dot in self.y_on_line:
            #    pygame.draw.circle(self.win, self.set.blue, dot, 1, 0)


    """ Regression stuff"""

    def update_RSS(self):
        error_lines = []
        self.y_on_line = []
        self.vertical_intercepts = []
        rss = 0

        for pair in self.arr:
            x, y = pair

            y_on_line = self.x_intercept(x, y)
            self.y_on_line.append((x, y_on_line))

            intercept = [(x,y), (x, y_on_line)]
            self.vertical_intercepts.append(intercept)

            rss += self.get_euclid(intercept[0], intercept[1])

        self.rss = rss

    def get_euclid(self, start, end):
        x1, y1 = start
        x2, y2 = end
        return m.sqrt( (x2-x1)**2 + (y2-y1)**2)


    def x_intercept(self, x, y):
        """ Supports update_RSS """

        start_x, start_y = self.pixel_start
        rads = m.radians(self.for_angle)

        opposite = x - start_x
        hypot = opposite / m.sin(rads)
        adjacent = m.cos(rads) * hypot

        #So, y on the line should be start_y + adjacent
        y_on_line = round( start_y + adjacent, 2)

        return y_on_line
