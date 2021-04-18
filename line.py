""" April 12, 2021 """


import pygame
import math as m
import random as r
from setup.printr import Printr
from arr import Arr


class FitLine(Arr):
    def __init__(self, win):
        super().__init__()
        pygame.init()
        self.win = win
        self.printr = Printr(self.win, self.set)
        self.show_intercepts = False

        ## Agnostic units
        self.degrees = 60
        self.update_opp_angle()

        ## Pixel units
        self.pixel_mid = [400, 400]
        self.pixel_length = 300
        self.update_end_points()

        ## Array units
        self.arr_start = (69, 420)
        self.arr_mid = (69, 420)
        self.rss = 1
        self.update_RSS()


    """ Main control """

    def update_motion(self, moving, rotating, centroid):
        self.move(moving)
        self.rotate(rotating)
        self.snap_to_centroid(centroid)

        self.update_end_points()
        self.convert()

    def update_display(self, show_intercepts):
        self.show_intercepts = show_intercepts


    def draw(self):
        self.draw_line()
        self.draw_intercepts()
        self.printr.print_instructions(self.degrees, self.opp_angle, self.rss)


    """ UPDATES """

    def move(self, moving):
        if moving:
            mx, my = pygame.mouse.get_rel()
            self.pixel_mid[0] += mx
            self.pixel_mid[1] += my

            self.update_RSS()

    def snap_to_centroid(self, snapping):
        if snapping:
            self.pixel_mid = self.pixel_centroid


    """ Rotating stuff """
    def rotate(self, rotating):
        if rotating:
            self.degrees += rotating
            self.degrees = self.wrap_angle(self.degrees)

            self.update_opp_angle()
            self.update_RSS()


    def update_opp_angle(self):
        self.opp_angle = self.degrees + 180
        self.opp_angle = self.wrap_angle(self.opp_angle)


    def wrap_angle(self, angle):
        if angle > 360:
            return 0
        if angle < 1:
            return 360
        return angle


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

    """ Drawing """
    def draw_line(self):
        c1 = self.set.light_grey_object_538
        c2 = self.set.object2_538
        pygame.draw.line(self.win, c1, tuple(self.pixel_start), tuple(self.pixel_end), 2)

        ## Draw mid circle
        pygame.draw.circle(self.win, c1, self.pixel_mid, 6, 2)
        pygame.draw.circle(self.win, self.set.white, self.pixel_mid, 4, 0)

        ## Draw start circle
        pygame.draw.circle(self.win, c2, self.pixel_start, 6, 0)

        self.draw_mid_coord()
        self.draw_start_coord()

    def draw_mid_coord(self):
        arr_x, arr_y = self.arr_mid
        pixel_x, pixel_y = self.pixel_mid
        x, y = self.pixel_mid

        arr_text = str( (round(arr_x, 1), round(arr_y, 1) ) )
        pixel_text = str( (x, y) )

        y -= 11
        self.printr.coord_printr(arr_text, x+15, y, self.set.grey)
        self.printr.coord_printr(pixel_text, x+15, y+15, self.set.blue)

    def draw_start_coord(self):
        arr_x, arr_y = self.arr_start
        x, y = self.pixel_start

        arr_text = str( (round(arr_x, 1), round(arr_y, 1) ) )
        pixel_text = str( (x, y) )

        y -= 11
        self.printr.coord_printr(arr_text, x+15, y, self.set.grey)
        self.printr.coord_printr(pixel_text, x+15, y+15, self.set.blue)


    def draw_intercepts(self):
        if self.show_intercepts:
            self.printr.coord_printr("Intercepts Tracer", 1600, 400, self.set.red)
            return ## Temp

            for intercept in self.arr_y_on_line:
                arr_x, arr_y = intercept
                px_x, px_y = self.convert_to_pixels(intercept)
                pygame.draw.circle(self.win, self.set.red, (px_x, px_y), 6, 0)

                ### Tracer
                arr_text = str( (round(arr_x, 1), round(arr_y, 1) ) )
                pixel_text = str( (px_x, px_y) )

                px_y -= 11
                self.printr.coord_printr(arr_text, px_x+15, px_y, self.set.grey)
                self.printr.coord_printr(pixel_text, px_x+15, px_y+15, self.set.blue)


    """ Regression stuff """
    """ Consider moving to other file """

    def update_RSS(self):
        self.arr_y_on_line = []
        rss = 0

        for coord in self.arr:
            x, y = coord

            error = self.error(coord)
            rss += error**2

        self.rss = rss


    def error(self, observation):
        """ Supports update_RSS """

        x1, y1 = self.arr_start
        x2, y2 = observation
        theta = m.radians(self.degrees)

        adj = x2 - x1
        opp = m.tan(theta) * adj

        y_on_line = (x2, y1 + opp)
        self.arr_y_on_line.append( y_on_line )

        ### TRACER ###
        px_x, px_y = self.convert_to_pixels(y_on_line)
        pygame.draw.circle(self.win, self.set.red, (px_x, px_y), 6, 0)


        error = self.get_euclid(observation, y_on_line)

        return error





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
