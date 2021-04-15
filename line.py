""" April 12, 2021 """


import pygame
import math as m
import random as r
from setup.printr import Printr
from arr import Arr
#from regression import Regression


class FitLine(Arr):
    def __init__(self, win):
        super().__init__()
        pygame.init()
        self.win = win
        self.printr = Printr(self.win, self.set)
        #self.reg = Regression(self.arr)
        self.show_intercepts = False

        ## Agnostic units
        self.degrees = 60
        self.update_opp_angle()

        ## Pixel units
        self.pixel_mid = [200, 600]
        self.pixel_length = 300
        self.update_end_points()

        ## Array units
        self.arr_length = 10 ## TBD
        self.arr_start = (69, 420)
        self.arr_mid = (69, 420)
        self.update_RSS()

        ## Tracer -- delete
        self.tracer_text = ""


    """ Main control """

    def update(self, moving, rotating, arr_units, show_intercepts):
        self.move(moving)
        self.rotate(rotating)
        self.update_end_points()
        self.show_intercepts = show_intercepts

        ## Conversions
        self.arr_start = self.convert_to_arr(self.pixel_start)
        self.arr_mid = self.convert_to_arr(self.pixel_mid)


    def draw(self):
        self.draw_line()
        self.draw_intercepts()
        self.printr.print_instructions(self.degrees, self.opp_angle, self.rss, self.tracer_text)


    """ UPDATES """

    def update_end_points(self):
        """ Update the start and end points if line moves/rotates"""

        midx, midy = self.pixel_mid
        hyp = self.pixel_length
        rads = m.radians(self.degrees)

        ## Do trig
        opp = m.sin(rads) * hyp
        adj = m.cos(rads) * hyp

        ## Apply deltas to mid coord
        start_x = midx + adj
        start_y = midy - opp

        end_x = midx - adj
        end_y = midy + opp

        self.pixel_start = [start_x, start_y]
        self.pixel_end = [end_x, end_y]


    def move(self, moving):
        if moving:
            mx, my = pygame.mouse.get_rel()
            self.pixel_mid[0] += mx
            self.pixel_mid[1] += my

            self.update_RSS()


    def snap_to_centroid(self):
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
            return angle - 360
        if angle < 1:
            return 360
        return angle


    """ Drawing """
    def draw_line(self):
        c = self.set.light_grey_object_538
        #pygame.draw.line(self.win, c, tuple(self.pixel_start), tuple(self.pixel_end), 2)

        ## Draw mid and start circles
        pygame.draw.circle(self.win, self.set.grey, self.pixel_mid, 6, 1)
        #pygame.draw.circle(self.win, c, self.pixel_start, 5, 1)
        #pygame.draw.circle(self.win, self.set.white, self.pixel_mid, 4, 0)
        #pygame.draw.circle(self.win, self.set.white, self.pixel_start, 4, 0)

        ## Draw mid coord
        # Arr units
        arr_x, arr_y = self.arr_mid
        pixel_x, pixel_y = self.pixel_mid
        x, y = self.pixel_mid

        arr_text = str( (round(arr_x, 1), round(arr_y, 1) ) )
        pixel_text = str( (round(pixel_x, 1), round(pixel_y, 1) ) )

        y -= 11
        x += 15
        self.printr.coord_printr(arr_text, x, y, self.set.grey)
        self.printr.coord_printr(pixel_text, x, y+15, self.set.blue)


    """ Utility """

    def get_euclid(self, start, fin):
        x1, y1 = start
        x2, y2 = fin

        for i in [x1, y1, x2, y2]:
            if i == 0:
                i == 0.1

        sol = (x2-x1)**2 + (y2-y1)**2
        """ Tracer """
        self.tracer_text = "x1: " + str(x1) + "  | y1: " + str(y1) + " | x2: " + str(x2) + " | y2: " + str(y2) + " | Euclid: " + str(sol)


        if sol != 0:
            m.sqrt(sol)

        return sol


    """ Regression stuff """
    """ Consider moving to other file """

    def update_RSS(self):
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
