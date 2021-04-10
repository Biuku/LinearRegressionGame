""" April 10, 2021 """

""" Background objects are like painted scenery. No functional interactions."""

import pygame
import numpy as np
from setup.settings import Settings


class ArrayConfig:

    def __init__(self):
        pygame.init()
        self.set = Settings()
        self.arr = np.load('data/basic_arr.npy')
        #self.arr = np.load('data/ecommerce2.npy')

        self.w, self.h = 1300, 700
        self.origin = (200, 850) ## Anchor for everything

        self.configure_graph(self.arr)



    def configure_graph(self, arr):
        self.x_min, self.x_max = arr[:,0].min(), arr[:,0].max()
        self.y_min, self.y_max = arr[:,1].min(), arr[:,1].max()

        """ Configure x scale """
        ### Set up axis labels
        x_num_labels = 20
        self.x_scale_gap = self.w / x_num_labels
        self.x_scale = np.linspace( (self.x_min), (self.x_max), x_num_labels )

        ### Get factor to convert array x units to pygame pixels
        data_scale_unit = self.x_scale[1] - self.x_scale[0]
        self.x_scale_factor = self.x_scale_gap / data_scale_unit ## (delta graph scale) / (delta data scale)


        """ Configure y scale """
        y_num_labels = 15
        self.y_scale = np.linspace( (self.y_min), (self.y_max), y_num_labels)
        self.y_scale_gap = self.h / y_num_labels

        ### Get factor to convert array y units to pygame pixels
        ## Note, additional step needed for y to reverse direction... not handled here
        data_scale_unit = self.y_scale[1] - self.y_scale[0]
        self.y_scale_factor = self.y_scale_gap / data_scale_unit


    def convert_arr_to_pixels(self, pair):
        left, bottom = self.origin

        relative_x = pair[0] - self.x_min
        relative_y = pair[1] - self.y_min

        x = left + int( relative_x * self.x_scale_factor)
        y = bottom - int( relative_y * self.y_scale_factor)

        return x, y


        """
        The var's I instantiate in configure_graph

        self.x_min, self.x_max
        self.y_min, self.y_max

        self.x_scale
        self.y_scale

        self.x_scale
        self.x_scale_gap
        self.x_scale_factor

        self.y_scale
        self.y_scale_gap
        self.y_scale_factor

        """
