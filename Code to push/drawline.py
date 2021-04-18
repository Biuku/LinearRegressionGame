""" April 18, 2021 """


import pygame
from setup.printr import Printr
from setup.settings import Settings
import math as m

class DrawLine:

    def __init__(self, win, arr):
        pygame.init()
        self.win = win
        self.set = Settings()
        self.arr = arr
        self.printr = Printr(self.win, self.set)
        self.c1 = self.set.light_grey
        self.c2 = self.set.light_blue

    def draw_line(self, pixel_points, arr_points):
        self.pixel_start, self.pixel_mid, self.pixel_end = pixel_points
        self.arr_start, self.arr_mid = arr_points

        pygame.draw.line(self.win, self.c1, tuple(self.pixel_start), tuple(self.pixel_end), 2)

        ## Draw mid circle
        pygame.draw.circle(self.win, self.c1, self.pixel_mid, 6, 2)
        pygame.draw.circle(self.win, self.set.white, self.pixel_mid, 4, 0)

        ## Draw start circle
        pygame.draw.circle(self.win, self.set.object2_538, self.pixel_start, 6, 0)

        self.draw_mid_coord()


    def draw_mid_coord(self):
        arr_x, arr_y = self.arr_mid
        pixel_x, pixel_y = self.pixel_mid
        x, y = self.pixel_mid

        arr_text = str( (round(arr_x, 1), round(arr_y, 1) ) )
        pixel_text = str( (x, y) )

        y -= 11
        self.printr.coord_printr(arr_text, x+15, y, self.c1)
        #self.printr.coord_printr(pixel_text, x+15, y+15, self.c2)



    def draw_intercepts(self, show_intercepts, intercepts, error):
        if show_intercepts:

            arr_intercepts, pixel_intercepts, pixels_of_array = intercepts

            for i in range(len(pixel_intercepts)):
                x, y1 = pixels_of_array[i]
                x, y2 = pixel_intercepts[i]

                pygame.draw.circle(self.win, self.set.red, (x, y2), 3, 0)
                pygame.draw.line(self.win, self.set.red, (x, y1), (x, y2), 1)

                y = int( (y2-y1)/2 + y1)
                error_text = m.sqrt(error[i])
                error_text = "error: " + str(round(error_text, 2))
                self.printr.coord_printr(error_text, x+15, y, self.set.red)
