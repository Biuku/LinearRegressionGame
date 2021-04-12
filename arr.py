""" April 10, 2021 """

import pygame
import numpy as np
from setup.settings import Settings


class Arr:

    def __init__(self):
        pygame.init()
        self.set = Settings()
        self.arr = np.load('data/basic_arr.npy')

        ### Pixel data
        self.w, self.h = 1200, 700
        self.pixel_origin = (200, 850) ## Anchor for everything

        ### Array data
        self.configure_graph(self.arr)
        self.get_centroid()
        self.origin = (self.x_min, self.y_min)


    def get_centroid(self):
        x = self.arr[:,0].mean()
        y = self.arr[:,1].mean()

        """ Delete line below to make this array data """
        x, y = self.convert_arr_to_pixels([x, y])

        return [x, y]


    def configure_graph(self, arr):
        """All array data"""

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
        data_scale_unit = self.y_scale[1] - self.y_scale[0]
        self.y_scale_factor = self.y_scale_gap / data_scale_unit



    def convert_pixels_to_arr(self, coords):
        """
        1. Find how far the array points are from the array origin

        """

        left, bottom = self.pixel_origin

        x = left + int( relative_x * self.x_scale_factor)
        y = bottom - int( relative_y * self.y_scale_factor)

        relative_x = coords[0] - self.x_min
        relative_y = coords[1] - self.y_min


        return x, y


    def convert_arr_to_pixels(self, coords):
        left, bottom = self.pixel_origin

        relative_x = coords[0] - self.x_min
        relative_y = coords[1] - self.y_min

        x = left + int( relative_x * self.x_scale_factor)
        y = bottom - int( relative_y * self.y_scale_factor)

        return x, y
