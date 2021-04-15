""" April 12, 2021 """

import pygame
from arr import Arr
from setup.printr import Printr


class Plot(Arr):

    def __init__(self, win):
        pygame.init()
        super().__init__()
        self.win = win
        self.printr = Printr(self.win, self.set)

    def draw(self):
        self.draw_axes()
        self.draw_x_axes_labels()
        self.draw_y_axes_labels()
        self.draw_origin()
        self.draw_centroid()
        self.draw_array()


    def draw_array(self):
        return ## Temp
        c = self.set.blue

        for coord in self.arr:
            coord = self.convert_to_pixels(coord)
            pygame.draw.circle(self.win, c, coord, 3, 0)


    def draw_origin(self):
        c = self.set.light_grey

        pygame.draw.circle(self.win, c, self.pixel_origin, 5, 0)

        x = self.pixel_origin[0] + 15
        y = self.pixel_origin[1] - 20

        self.printr.coord_printr(str(self.arr_origin), x, y, self.set.black)
        self.printr.coord_printr(str(self.pixel_origin), x, y+15, self.set.blue)


    def draw_centroid(self):
        c = self.set.light_grey_object_538
        x, y = self.arr_centroid
        text = "Centroid: " + str( ( round(x,1), round(y,1) ) )

        x, y = self.pixel_centroid

        pygame.draw.circle(self.win, c, self.pixel_centroid, 4, 0)
        self.printr.coord_printr(text, x+10, y-15, c)


    def draw_axes(self):
        c = self.set.light_grey
        x, y = self.false_axes_origin
        right, top = x + self.w, y - self.h

        pygame.draw.line(self.win, c, (x, y), (x, top), 2)
        pygame.draw.line(self.win, c, (x, y), (right, y), 2)


    def draw_x_axes_labels(self):

        ### Draw x scale
        origin_x = self.pixel_origin[0]
        false_y = self.false_axes_origin[1]

        for i in range(self.x_num_labels):
            pixel_x = self.pixel_x_scale[i]

            ### Draw dot on axis
            self.draw_dot(pixel_x, false_y+1)

            ### Draw labels
            offset_x = pixel_x - 12
            arr_label = str( round(self.x_scale[i], 1) )
            pixel_label = str( int(self.pixel_x_scale[i]) )

            self.printr.coord_printr(arr_label, offset_x, false_y + 10, self.set.black)
            self.printr.coord_printr(pixel_label, offset_x, false_y + 25, self.set.blue)

    def draw_y_axes_labels(self):
            ### Print y scale
            false_x = self.false_axes_origin[0]
            origin_y = self.pixel_origin[1]

            for i in range(self.y_num_labels):
                pixel_y = self.pixel_y_scale[i]

                ### Draw dot on axis
                self.draw_dot(false_x+1, pixel_y)

                ### Draw labels
                offset_y = pixel_y - 15
                arr_label = str( round(self.y_scale[i], 1) )
                pixel_label = str( int(self.pixel_y_scale[i]) )

                self.printr.coord_printr(arr_label, false_x - 40, offset_y, self.set.black)
                self.printr.coord_printr(pixel_label, false_x - 40, offset_y + 15, self.set.blue)


    """ Utility """
    def draw_dot(self, x, y):
        pygame.draw.circle(self.win, self.set.grey, (x, y), 2, 0)
