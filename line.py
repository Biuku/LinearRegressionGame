""" April 11, 2021 """


import pygame
import math as m
import random as r
from array_config import ArrayConfig
from printr import Printr


class FitLine(ArrayConfig):
    def __init__(self, win):
        pygame.init()
        self.win = win
        super().__init__()
        self.printr = Printr(self.win, self.set)

        ## Pixel var's
        self.length = 500
        self.angle = 25 ## 'angle' for trig; 'slope' for regression
        self.mid = [700, 500] ### Line always anchors to mid

        ## Array var's
        self.rss = 0

        self.update_end_points()
        self.get_centroid() ## Centroid in pixels

        ### Tracer
        self.rotating_line_start = (700, 300)
        self.rotating_line_angle = 270


    def update(self, moving, rotating):
        self.move(moving)
        self.rotate(rotating)
        self.update_end_points()
        self.update_RSS()


    def move(self, moving):
        if moving:
            mx, my = pygame.mouse.get_rel()
            self.mid[0] += mx
            self.mid[1] += my


    def rotate(self, rotating):
        if rotating:
            self.angle += rotating


    def update_end_points(self):
        """ Update the start and end points if line moves/rotates"""

        x, y = self.mid
        rads = m.radians(self.angle)
        opposite_angle = self.angle + 180

        if opposite_angle > 360:
            opposite_angle -= 360

        opposite_rads = m.radians(opposite_angle)

        ## Draw mid to end half of line
        end_x = x + ( m.cos(rads) * self.length )
        end_y = y + ( m.sin(rads) * self.length )
        self.end = (end_x, end_y)

        # ## Draw start to mid half of line
        # start_x = x - ( m.cos(rads) * (self.length) )
        # start_y = y - ( m.sin(rads) * (self.length) )
        # self.start = (start_x, start_y)

        ## Draw start to mid half of line
        start_x = x + ( m.cos(opposite_rads) * self.length )
        start_y = y + ( m.sin(opposite_rads) * self.length )

        self.start = (start_x, start_y)


    def draw_rotating_line(self):
        length = 200
        start = self.rotating_line_start
        x, y = start
        self.rotating_line_angle += 1

        ### Draw blue / forward part of line
        angle = self.rotating_line_angle
        rads = m.radians(angle)

        forward_x = x + ( m.cos(rads) * length )
        forward_y = y + ( m.sin(rads) * length )
        end = (forward_x, forward_y)

        pygame.draw.line(self.win, self.set.blue, start, end, 2)

        ### Draw red / opposite part of line
        opposite_angle = angle + 180

        if opposite_angle > 360:
            opposite_angle -= 360

        opposite_rads = m.radians(opposite_angle)

        opposite_x = x + ( m.cos(opposite_rads) * length )
        opposite_y = y + ( m.sin(opposite_rads) * length )
        end = (opposite_x, opposite_y)

        pygame.draw.line(self.win, self.set.red, start, end, 2)




    def draw_theoretical_line(self):
        self.draw_rotating_line()
        return


        """ Tracer -- is everything adding up ???"""
        start_x, start_y = self.start
        rads = m.radians(self.angle)

        delta_x = opposite = m.sin(rads) * (self.length // 2)
        delta_y = adjacent = m.cos(rads) * (self.length // 2)

        end = (start_x + delta_x, start_y + delta_y)
        start = (start_x , start_y )

        pygame.draw.line(self.win, self.set.blue, start, end, 2)


    def update_RSS(self):
        error_lines = []
        self.y_on_line = []
        self.vertical_intercepts = []
        rss = 0

        for pair in self.arr:
            x, y = pair

            y_on_line = self.x_intercept(x, y)
            self.y_on_line.append((x, y_on_line))

            vertical_intercept = [(x,y), (x, y_on_line)]
            self.vertical_intercepts.append(vertical_intercept)

            rss = y_on_line**2

        self.rss = rss




    def x_intercept(self, x, y):
        """ Supports update_RSS """

        start_x, start_y = self.start
        rads = m.radians(self.angle)

        """ TRIG APPROACH """
        opposite = x - start_x
        hypot = opposite / m.sin(rads)
        adjacent = m.cos(rads) * hypot

        #So, y on the line should be start_y + adjacent
        y_on_line = round( start_y + adjacent, 2)

        return y_on_line


    def snap_to_centroid(self):
        self.mid = self.centroid


    def draw(self):
        self.draw_theoretical_line()
        pygame.draw.line(self.win, self.set.grey, tuple(self.start), (self.end), 4)

        ### TRACER LINE

        ## Draw a small circle denoting the mid
        pygame.draw.circle(self.win, self.set.black, self.mid, 6, 0)

        ## Draw vertical lines between the error bars and my line
        for dot in self.y_on_line:
            pygame.draw.circle(self.win, self.set.blue, dot, 1, 0)

        for line in self.vertical_intercepts:
            start, end = line
            pygame.draw.line(self.win, self.set.blue, start, end, 1)

        self.printr.print_coord(self.mid[0], self.mid[1])
        self.printr.print_instructions(self.angle, self.rss)



    """ Init stuff """
    def get_centroid(self):
        x = self.arr[:,0].mean()
        y = self.arr[:,1].mean()

        x, y = self.convert_arr_to_pixels([x, y])

        self.centroid = [x, y]
