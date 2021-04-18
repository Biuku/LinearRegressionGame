""" April 18, 2021 """

import pygame
import numpy as np
from setup.settings import Settings


class Arr:

    def __init__(self):
        pygame.init()
        self.set = Settings()

        ## Fundamental anchors -- directly equate to the arr min and max
        self.pixel_origin = (200, 850)
        self.pixel_w = 1200
        self.pixel_h = 700

        ## How many labels to divide each axis into
        self.x_num_labels = 17 ## Gives shorter floats
        self.y_num_labels = 15

        ### Pixel units
        self.configure_pixel_scale()

        ### Array units
        self.arr = np.load('data/basic_arr.npy')
        self.configure_arr()
        self.configure_arr_scale()


        ### Agnostic units
        self.configure_conversion_factor()
        self.get_centroid()

        self.buffer = 50
        self.configure_false_axes()

        self.regression()
        self.get_pixels_of_arr()


    """ CONFIGURATION STUFF """

    ### PIXELS
    def configure_pixel_scale(self):

        # Set pixel min/max
        self.pixel_x_min, self.pixel_y_max = self.pixel_origin
        self.pixel_x_max = self.pixel_x_min + self.pixel_w
        self.pixel_y_min = self.pixel_y_max - self.pixel_h

        self.pixel_x_scale = np.linspace( (self.pixel_x_min), (self.pixel_x_max), self.x_num_labels )
        self.pixel_y_scale = np.linspace( (self.pixel_y_max), (self.pixel_y_min), self.y_num_labels )


    ### ARR
    def configure_arr(self):
        # Set arr min/max
        x, y = self.arr[:,0], self.arr[:,1]
        self.arr_x_min, self.arr_x_max = x.min(), x.max()
        self.arr_y_min, self.arr_y_max = y.min(), y.max()

        self.arr_origin = (self.arr_x_min, self.arr_y_min)

    def configure_arr_scale(self):
        self.arr_x_scale = np.linspace( self.arr_x_min, self.arr_x_max, self.x_num_labels )
        self.arr_y_scale = np.linspace( self.arr_y_min, self.arr_y_max, self.y_num_labels )



    """ CONVERSION STUFF """

    def configure_conversion_factor(self):
        ## X
        # Pick the element from the same index location in each scale
        arr_x = self.arr_x_scale[7]
        arr_y = self.arr_y_scale[7]
        pixel_x = self.pixel_x_scale[7]
        pixel_y = self.pixel_y_scale[7]

        # Zero these
        arr_x -= self.arr_x_min
        arr_y -= self.arr_y_min
        pixel_x -= self.pixel_x_min
        pixel_y = self.pixel_y_max - pixel_y

        # Get conversion factor
        self.x_to_arr = arr_x / pixel_x
        self.y_to_arr = arr_y / pixel_y

        # Reverse direction = inverse
        self.x_to_pixels = 1 / self.x_to_arr
        self.y_to_pixels = 1 / self.y_to_arr


    def convert_to_arr(self, pixel_coords):
        x, y = pixel_coords

        ## Zero the passed coord
        x -= self.pixel_x_min
        y = self.pixel_y_max - y

        ### Convert
        x *= self.x_to_arr
        y *= self.y_to_arr

        ### Add back the zero coord in arr units
        x += self.arr_x_min
        y += self.arr_y_min

        return x, y


    def convert_to_pixels(self, arr_coords):
        x, y = arr_coords

        ## Find x, y values relative to arr origin
        x -= self.arr_x_min
        y -= self.arr_y_min

        ## Scale those values to be pixels
        x *= self.x_to_pixels
        y *= self.y_to_pixels

        ## Find x, y values relative to arr origin
        x += self.pixel_x_min
        y = self.pixel_y_max - y

        return int(x), int(y) ## Pixel values should be int


    def get_centroid(self):
        x = self.arr[:,0].mean()
        y = self.arr[:,1].mean()

        self.arr_centroid = [x, y]
        self.pixel_centroid = list( self.convert_to_pixels( (x, y) ) )


    def get_pixels_of_arr(self):
        arr = []
        for coord in self.arr:
            pixels = self.convert_to_pixels(coord)
            arr.append( tuple(pixels) )

        self.pixels_of_arr = tuple(arr)



    """ FIND COEFFICIENTS AND SSE FOR BEST-FIT LINE """
    def regression(self):
        x_mean, y_mean = self.arr_centroid
        x_dev = self.arr[:,0] - x_mean
        y_dev = self.arr[:,1] - y_mean

        numerator = (x_dev * y_dev).sum()
        denom = (x_dev**2).sum()

        self.b1 = numerator/denom
        self.b0 = y_mean - self.b1*x_mean

        pred = self.b0 + (self.b1 * self.arr[:,0])
        error = self.arr[:,1] - pred
        squared_error = error**2
        self.SSE = squared_error.sum()



    """ UTILITY """
    def configure_false_axes(self):

        x, y = self.pixel_origin

        self.false_axes_origin = (x - self.buffer, y + self.buffer)
        self.false_axis_w = self.pixel_w + (2 * self.buffer)
        self.false_axis_h = self.pixel_h + (2 * self.buffer)
