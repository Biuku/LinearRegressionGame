""" April 7, 2021 """

""" Background objects are like painted scenery. No functional interactions."""

import pygame
import numpy as np
from setup.settings import Settings


class Plot:

    def __init__(self, win, arr):
        pygame.init()
        self.win = win
        self.set = Settings()
        self.w = 1400
        self.h = 750
        self.zero = (120, 850)

        ### Configure scale of graph
        self.arr = arr
        self.x_bounds = None
        self.y_bounds = None

        self.x_scale = None
        self.y_scale = None

        self.x_scale_values = None
        self.x_scale_gap = None
        self.x_scale_factor = None

        self.configure_graph(arr)


    def configure_graph(self, arr):
        x_min, x_max = arr[:,0].min(), arr[:,0].max()
        y_min, y_max = arr[:,1].min(), arr[:,1].max()

        self.x_bounds = ( int(x_min), int(x_max) )
        self.y_bounds = ( int(y_min), int(y_max) )

        ### Configure x scales
        num_scales = 20

        self.x_scale_values = np.linspace( (self.x_bounds[0]*0.9), (self.x_bounds[1]*1.1), num_scales).round(1)
        self.x_scale_gap = self.w // num_scales

        ### Scale x when drawing it
        """
        15.2174 comes from my calulator:  (190-120) / (35.2-30.6)
        """
        self.x_scale_factor =  15.2174 #self.w / (x_max - x_min) #15.2


    def draw(self, arr):

        ### Draw axes
        w, h = self.w, self.h

        left, top = self.zero[0], self.zero[1] - h
        right, bottom = left + w, top + h

        zero_zero = (left, bottom)

        pygame.draw.line(self.win, self.set.light_grey, (left, top), zero_zero, 2)
        pygame.draw.line(self.win, self.set.light_grey, zero_zero, (right, bottom), 2)



        """ DRAW ARRAY DOTS """
        c = self.set.light_grey

        for pair in arr:
            x_min = self.x_bounds[0]
            relative_x = pair[0] - (x_min *0.9)

            x = left + int( relative_x * self.x_scale_factor)
            y = pair[1] + top

            pygame.draw.circle(self.win, c, (x, y), 4, 0)


            """ TRACER """
            ### Draw the array coordinates ###
            text = self.set.med_font.render(str(pair), True, self.set.blue)
            self.win.blit( text, (x, y+5) )

            ### Draw the pixel x_coordinate
            text = self.set.med_font.render(str(x), True, self.set.blue)
            self.win.blit( text, (x, y+20) )


        self.draw_scale(arr)


    def draw_scale(self, arr):
        c = self.set.grey
        x, y = self.zero
        y += 10

        for value in self.x_scale_values:
            text = self.set.med_font.render(str(value), True, c)
            self.win.blit( text, (x, y) )

            """ TRACER """
            text = self.set.med_font.render(str(x), True, self.set.blue)
            self.win.blit( text, (x+5, y+20) )

            ### Not tracer
            x += self.x_scale_gap
