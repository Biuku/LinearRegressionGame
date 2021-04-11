""" April 10, 2021 """

import pygame
import numpy as np
from array_config import ArrayConfig
from printr import Printr

class Plot(ArrayConfig):

    def __init__(self, win):
        pygame.init()
        super().__init__()
        self.win = win
        self.printr = Printr(self.win, self.set)


    """ DRAWING """

    def draw(self):
        self.draw_axes()
        self.draw_array()


    def draw_array(self):
        c = self.set.light_grey

        for pair in self.arr:
            x, y = self.convert_arr_to_pixels(pair)

            pygame.draw.circle(self.win, c, (x, y), 4, 0)

            ### Tracer """
            self.printr.arr_coord_tracer(pair, x, y)


    def draw_axes(self):
        c = self.set.light_grey

        x, y = self.origin
        right, top = x + self.w, y - self.h

        offset = 50
        off_x, off_y = x-offset,  y+offset

        pygame.draw.line(self.win, c, (off_x, off_y), (off_x, y - self.h), 2)
        pygame.draw.line(self.win, c, (off_x, off_y), (x + self.w, off_y), 2)

        self.draw_axes_labels(off_x, off_y)


    def draw_axes_labels(self, off_x, off_y):
        x, y = self.origin
        master_y = y

        def label_printr(i, x, y):
            text = self.set.med_font.render(i, True, self.set.grey)
            self.win.blit( text, (x, y) )

        for i in self.x_scale:
            label_printr(str(round(i, 1)), x, off_y+5)
            self.printr.x_data_label_tracer(x, off_y) ### Tracer
            x += self.x_scale_gap

        y = master_y

        for i in self.y_scale:
            label_printr(str(round(i, 1)), off_x-40, y)
            y -= self.y_scale_gap





    """ TEMP DELETE """

    def draw_rotating_line(self):
        # self.rotating_line_start = (700, 300)
        # self.rotating_line_angle = 270


        length = 200
        start = self.rotating_line_start
        x, y = start
        self.rotating_line_angle += 1

        ### Draw blue / forward part of line
        angle = self.rotating_line_angle
        rads = m.radians(angle)

        forward_x = x + ( m.cos(rads) * length )
        forward_y = y + ( m.sin(rads) * length )
        end = (forward_x, forward_y)

        pygame.draw.line(self.win, self.set.blue, start, end, 2)

        ### Draw red / opposite part of line
        opposite_angle = angle + 180

        if opposite_angle > 360:
            opposite_angle -= 360

        opposite_rads = m.radians(opposite_angle)

        opposite_x = x + ( m.cos(opposite_rads) * length )
        opposite_y = y + ( m.sin(opposite_rads) * length )
        end = (opposite_x, opposite_y)

        pygame.draw.line(self.win, self.set.red, start, end, 2)
