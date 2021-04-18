""" April 18, 2021 """


import pygame
import math as m
import random as r
from setup.printr import Printr
from arr import Arr
from drawline import DrawLine


class FitLine(Arr):
    def __init__(self, win):
        super().__init__()
        pygame.init()
        self.win = win
        self.printr = Printr(self.win, self.set)
        self.drawline = DrawLine(self.win, self.arr)
        self.show_intercepts = False

        ## Agnostic units
        self.degrees = 30
        self.slope = 1

        ## Pixel units
        self.pixel_mid = [800, 400]
        self.pixel_length = self.pixel_w/2 + 10
        self.update_end_points()

        ## Array units
        self.arr_start = (1, 1)
        self.arr_mid = (1, 1)
        self.y_intercept = 1
        self.update_RSS()


    def update(self, moving, rotating, show_intercepts):
        self.move(moving)
        self.rotate(rotating)
        self.show_intercepts = show_intercepts

    def update_coords(self):
        ## If I move or rotate, recalculate everything ##
        self.update_end_points()
        self.convert()
        self.update_coefficients()
        self.update_RSS()


    def draw(self):
        ### Draw line ###
        pixel_points = [self.pixel_start, self.pixel_mid, self.pixel_end]
        arr_points = [self.arr_start, self.arr_mid]
        self.drawline.draw_line(pixel_points, arr_points)

        ### Draw intercepts on the line ###
        intercepts = [self.arr_y_on_line, self.pixel_y_on_line, self.pixels_of_arr]
        self.drawline.draw_intercepts(self.show_intercepts, intercepts, self.error)

        self.printr.print_instructions(self.b0, self.b1, self.SSE, self.y_intercept, self.slope, self.sse)


    """ UPDATES """

    def move(self, moving):
        if moving:
            mx, my = pygame.mouse.get_rel()
            self.pixel_mid[0] += mx
            self.pixel_mid[1] += my

            self.update_coords()



    """ Rotating stuff """
    def rotate(self, rotating):
        def wrap_angle(angle):
            if angle > 360:
                return 1
            if angle < 0:
                return 360
            return angle

        if rotating:
            self.degrees += rotating
            self.degrees = wrap_angle(self.degrees)

            self.update_coords()


    def update_end_points(self):
        """ Update the start and end points if line moves/rotates"""

        midx, midy = self.pixel_mid
        hyp = self.pixel_length
        theta = m.radians(self.degrees)

        ## Do trig
        opp = m.sin(theta) * hyp
        adj = m.cos(theta) * hyp

        ## Get start/end by applying deltas to mid coord
        start_x = int(midx - adj)
        start_y = int(midy + opp)
        end_x = int(midx + adj)
        end_y = int(midy - opp) # account for pygame negative stupidity

        self.pixel_start = [start_x, start_y]
        self.pixel_end = [end_x, end_y]


    def convert(self):
        self.arr_start = self.convert_to_arr(self.pixel_start)
        self.arr_mid = self.convert_to_arr(self.pixel_mid)


    def update_coefficients(self):
        ## Slope
        x1, y1 = self.arr_mid
        x2, y2 = self.arr_start
        if x2-x1 != 0:
            self.slope = (y2 - y1) / (x2-x1)

        ## Y intercept
        self.y_intercept = y2 - self.slope*x2
        b0_mid = y1 - self.slope*x1


    def update_RSS(self):
        self.arr_y_on_line = []
        self.pixel_y_on_line = []
        self.error = []
        self.sse = 0

        for coord in self.arr:
            x, y = coord

            y_on_line = self.y_intercept + x*self.slope ## line equation

            error = (y - y_on_line)**2
            self.sse += error
            self.error.append(error)

            intercept_coord = [x, y_on_line]
            self.arr_y_on_line.append( intercept_coord )
            self.pixel_y_on_line.append(self.convert_to_pixels(intercept_coord))
