""" April 10, 2021 """

""" Background objects are like painted scenery. No functional interactions."""

"""
April 10 to do:
    - Anchor 0, 0 as the actual min(x), min(y)
        - Remove the 10% buffers on the graph
        - Rather, just move the graph some pixels down and left
"""


import pygame
import numpy as np
from setup.settings import Settings


class Plot:

    def __init__(self, win, arr):
        pygame.init()
        self.set = Settings()
        self.win = win
        self.arr = arr

        self.w = 1300
        self.h = 700
        self.origin = (200, 850) ## Anchor for everything

        self.configure_graph(arr) ### Configure scale of graph


    def configure_graph(self, arr):
        self.x_min, self.x_max = arr[:,0].min(), arr[:,0].max()
        self.y_min, self.y_max = arr[:,1].min(), arr[:,1].max()

        """ Configure x scales """
        x_num_scales = 20
        self.x_scale_gap = self.w / x_num_scales
        self.x_scale_values = np.linspace( (self.x_min), (self.x_max), x_num_scales)

        ### Scale x when drawing it
        data_scale_unit = self.x_scale_values[1] - self.x_scale_values[0]
        self.x_scale_factor = self.x_scale_gap / data_scale_unit ## (delta graph scale) / (delta data scale)

        """ Configure y scales """
        y_num_scales = 15
        self.y_scale_values = np.linspace( (self.y_min), (self.y_max), y_num_scales)
        self.y_scale_gap = self.h / y_num_scales

        ### Scale y when drawing it
        data_scale_unit = self.y_scale_values[1] - self.y_scale_values[0]
        self.y_scale_factor = self.y_scale_gap / data_scale_unit


    """ DRAWING """
    def draw(self, arr):
        self.draw_axes(arr)
        self.draw_array(arr)

    def draw_axes(self, arr):
        """ Draw axes """
        c = self.set.light_grey
        x, y = self.origin
        right, top = x + self.w, y - self.h
        offset = 50
        offset_x, offset_y = x - offset, y + offset

        pygame.draw.line(self.win, c, (offset_x, offset_y), (offset_x, top), 2)
        pygame.draw.line(self.win, c, (offset_x, offset_y), (right, offset_y), 2)

        """ Tracer -- draw big fugly origin """
        pygame.draw.circle(self.win, self.set.red, (x, y), 10, 0)


        """ Draw x data labels """
        c = self.set.grey

        for value in self.x_scale_values:
            value = round(value, 1)
            text = self.set.med_font.render(str(value), True, c)
            self.win.blit( text, (x, offset_y + 5) )

            """ TRACER """
            text = self.set.med_font.render(str(int(x)), True, self.set.blue)
            self.win.blit( text, (x, offset_y + 20) )

            ### Not tracer
            x += self.x_scale_gap

        """ Draw y data labels """
        x, y = self.origin ## Reset x,y
        x -= (offset + 40)

        for value in self.y_scale_values:
            value = round(value, 1)
            text = self.set.med_font.render(str(value), True, c)
            self.win.blit( text, (x, y) )

            y -= self.y_scale_gap


    def draw_array(self, arr):
        c = self.set.light_grey
        left, y = self.origin
        bottom = y

        for pair in arr:
            relative_x = pair[0] - self.x_min
            relative_y = pair[1] - self.y_min

            x = left + int( relative_x * self.x_scale_factor)
            y = bottom - int( relative_y * self.y_scale_factor)

            pygame.draw.circle(self.win, c, (x, y), 4, 0)


            """ TRACER """
            ### Draw the array coordinates ###
            text = self.set.med_font.render(str(pair), True, self.set.blue)
            self.win.blit( text, (x, y+5) )

            ### Draw the pixel x_coordinate
            text = self.set.med_font.render(str(x), True, self.set.blue)
            self.win.blit( text, (x, y+20) )



    """
    The var's I instantiate from init. Took out of init to reduce clutter...
    I didn't actually know you could instantiate without a placeholder in init

    self.x_minmax = None
    self.y_minmax = None

    self.x_scale = None
    self.y_scale = None

    self.x_scale_values = None
    self.x_scale_gap = None
    self.x_scale_factor = None

    self.x_scale_values = None
    self.x_scale_gap = None
    self.x_scale_factor = None

    self.y_scale_values = None
    self.y_scale_gap = None
    self.y_scale_factor = None
    """
