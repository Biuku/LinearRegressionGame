""" April 12, 2021 """

import pygame
import numpy as np
from setup.settings import Settings


class Arr:

    def __init__(self):
        pygame.init()
        self.set = Settings()

        ## Graph data = "False" data
        """
        The axes lines are drawn down-left from the actual origin of the data.
        Because this is a scatterplot it doesn't matter, so long as the labels are correct
        """
        self.w, self.h = 1400, 750
        self.pixel_origin = (200, 850)

        self.false_axes_origin = self.get_false_axes_origin() ## Shift the drawn axes lines down_left

        ### Pixel units
        self.configure_pixel_scale()

        ### Array units
        self.arr = np.load('data/basic_arr.npy')
        self.configure_arr()
        self.configure_arr_scale()

        ### Agnostic units
        self.get_centroid()


    """ CONFIGURATION STUFF """

    def configure_pixel_scale(self):
        self.pixel_x_min, self.pixel_y_max = self.pixel_origin

        ## Configure pixel lengths
        self.pixel_x_len = self.w - 100
        self.pixel_y_len = self.h - 75

        self.pixel_x_max = self.pixel_x_min + self.pixel_x_len
        self.pixel_y_min = self.pixel_y_max - self.pixel_y_len

        self.x_num_labels = 20
        self.y_num_labels = 15

        self.pixel_x_scale = np.linspace( (self.pixel_x_min), (self.pixel_x_max), self.x_num_labels )
        self.pixel_y_scale = np.linspace( (self.pixel_y_max), (self.pixel_y_min), self.y_num_labels )

        self.pixel_x_scale_unit = self.pixel_x_len / self.x_num_labels
        self.pixel_y_scale_unit = self.pixel_y_len / self.y_num_labels


    def configure_arr(self):

        self.x_min = self.arr[:,0].min()
        self.y_min = self.arr[:,1].min()
        self.arr_origin = (self.x_min, self.y_min)

        self.x_max = self.arr[:,0].max()
        self.y_max = self.arr[:,1].max()

        ## Configure arr lengths
        self.x_len = self.x_max - self.x_min
        self.y_len = self.y_max - self.y_min


    def configure_arr_scale(self):
        self.x_scale = np.linspace( (self.x_min), (self.x_max), self.x_num_labels )
        self.y_scale = np.linspace( (self.y_min), (self.y_max), self.y_num_labels )

        self.x_scale_unit = self.x_scale[1] - self.x_scale[0]
        self.y_scale_unit = self.y_scale[1] - self.y_scale[0]


    """ CONVERSION STUFF """

    def convert_to_arr(self, pixel_coords):
        x, y = pixel_coords

        ## Find x, y values relative to pixel origin
        x = x - self.pixel_x_min
        y = self.pixel_y_max - y

        ## Scale those values to be array units
        x, y = self.to_arr(x, y)

        ## Shift the values relative to arr origin
        x += self.x_min
        y += self.y_min

        return x, y


    def convert_to_pixels(self, arr_coords):
        x, y = arr_coords

        ## Find x, y values relative to arr origin
        x -= self.x_min
        y -= self.y_min

        ## Scale those values to be pixels
        x, y = self.to_pixels(x, y)

        ## Shift the values relative to pixel origin
        x = x + self.pixel_x_min
        y = self.pixel_y_max - y

        return int(x), int(y)


    def to_pixels(self, x, y):
        x *= (self.pixel_x_scale_unit / self.x_scale_unit) ## (delta pixel scale) / (delta arr scale)
        y *= (self.pixel_y_scale_unit / self.y_scale_unit)

        return x, y


    def to_arr(self, x, y):
        x *= (self.x_scale_unit / self.pixel_x_scale_unit)
        y *= (self.y_scale_unit / self.pixel_y_scale_unit)

        return x, y


    def get_centroid(self):
        x = self.arr[:,0].mean()
        y = self.arr[:,1].mean()

        self.arr_centroid = [x, y]
        self.pixel_centroid = list( self.convert_to_pixels( (x, y) ) )


    """ UTILITY """

    def get_false_axes_origin(self):
        # self.x_false_gap_pixels = self.set.win_w * (self.set.border_gap + 0.05)
        # self.y_false_gap_pixels = self.set.win_h * (self.set.border_gap + 0.07)
        x, y = self.pixel_origin

        # return (self.x_false_gap_pixels, self.set.win_h - self.y_false_gap_pixels)
        return (x-50, y + 50)
