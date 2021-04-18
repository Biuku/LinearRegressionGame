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
        self.show_centroid = False
        self.c1 = self.set.light_grey ## Arr coord's
        self.c2 = self.set.light_blue ## Pixel coords


    def update(self, show_centroid):
        self.show_centroid = show_centroid


    def draw(self):
        self.draw_axes()
        self.draw_x_axes_labels()
        self.draw_y_axes_labels()
        self.draw_centroid()
        self.draw_array()


    def draw_array(self):

        for arr_coord in self.arr:
            px_coord = self.convert_to_pixels(arr_coord)
            pygame.draw.circle(self.win, self.set.blue, px_coord, 4, 0)
            self.draw_arr_coord(arr_coord, px_coord)


    def draw_arr_coord(self, arr, px):
        x, y = px
        arr_text = str( (round(arr[0], 1), round(arr[1], 1) ) )
        pixel_text = str( (x, y) )

        self.printr.coord_printr(arr_text, x-45, y, self.c1)


    def draw_centroid(self):

        if self.show_centroid:
            c = self.set.object2_538

            x, y = self.arr_centroid
            text = "Centroid: " + str( ( round(x,1), round(y,1) ) )

            x, y = self.pixel_centroid

            ### Draw horizontal line, vertical lines
            pygame.draw.line(self.win, c, (self.pixel_x_min, y), (self.pixel_x_max, y), 1)
            pygame.draw.line(self.win, c, (x, self.pixel_y_max), (x, self.pixel_y_min), 1)

            ### Draw centroid circle and coordinates
            pygame.draw.circle(self.win, c, self.pixel_centroid, 5, 0)
            self.printr.coord_printr(text, x+10, y-18, self.c1)


    def draw_axes(self):
        c = self.set.light_grey
        x, y = self.false_axes_origin
        right = x + self.false_axis_w
        top = y - self.false_axis_h

        pygame.draw.line(self.win, self.c1, (x, y), (x, top), 2)
        pygame.draw.line(self.win, self.c1, (x, y), (right, y), 2)


    def draw_x_axes_labels(self):

        ### Draw x scale
        y = self.false_axes_origin[1]
        origin_x = self.pixel_origin[0]

        for i in range(self.x_num_labels):
            pixel_x = self.pixel_x_scale[i]

            ### Draw dot on axis
            pygame.draw.circle(self.win, self.set.grey, (pixel_x, y+1), 2, 0)

            ### Draw labels
            offset_x = pixel_x - 12
            arr_label = str( round(self.arr_x_scale[i], 1) )
            pixel_label = str( int(self.pixel_x_scale[i]) )

            self.printr.coord_printr(arr_label, offset_x, y + 10, self.set.light_grey)
            self.printr.coord_printr(pixel_label, offset_x, y + 25, self.set.blue)


    def draw_y_axes_labels(self):
            ### Print y scale
            x = self.false_axes_origin[0]
            origin_y = self.pixel_origin[1]

            for i in range(self.y_num_labels):
                pixel_y = self.pixel_y_scale[i]

                ### Draw dot on axis
                pygame.draw.circle(self.win, self.set.grey, (x+1, pixel_y), 2, 0)

                ### Draw labels
                offset_y = pixel_y - 15
                arr_label = str( round(self.arr_y_scale[i], 1) )
                pixel_label = str( int(self.pixel_y_scale[i]) )

                self.printr.coord_printr(arr_label, x - 40, offset_y, self.set.light_grey)
                self.printr.coord_printr(pixel_label, x - 40, offset_y + 15, self.set.blue)
