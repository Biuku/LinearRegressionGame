""" April 11, 2021 """


import pygame
import math as m
import random as r



class Printr:
    def __init__(self, win, set):
        pygame.init()
        self.win = win
        self.set = set


    def print_coord(self, x, y):
        # text = str( (arr[:,0].mean(), arr[:,1].mean()) )
        text = str( (x, y) )
        text = self.set.med_font.render(text, True, self.set.grey)
        x += 15
        y -= 20
        self.win.blit( text, (x, y) )


    def print_instructions(self, angle, rss):
        x = self.set.win_w * 0.85 ## lower number --> leftward
        y = self.set.win_h * 0.07 ## lower number --> upward

        texts = [
            "Angle: " + str(round(angle, 2)) + "°",
            "RSS: " + str(round(rss, 2)),
            'c = snap to centroid',
            'd = Clockwise',
            'a = Counter-clockwise',
            'Right-click = fast clockwise'
            ]

        for text in texts:
            print_instructions = self.set.med_font.render(text, True, self.set.grey)
            self.win.blit( print_instructions, (x, y) )
            y += 20



        """ TRACERS """

    def x_data_label_tracer(self, x, off_y):
        """ TRACER """
        ### Call from draw_axes > draw x_labels with this: self.x_data_label_tracer(x, off_y)
        text = self.set.med_font.render(str(int(x)), True, self.set.blue)
        self.win.blit( text, (x, off_y + 20) )

    def arr_coord_tracer(self, pair, x, y):
        """ TRACER """
        ### Call from draw_array with: self.arr_coord_tracer(pair, x, y)

        ### Draw the array coordinates ###
        text = self.set.small_font.render(str(tuple(pair)), True, self.set.blue)
        self.win.blit( text, (x, y+5) )

        ### Draw the pixel x_coordinate
        text = self.set.small_font.render(str(x) + " pixels", True, self.set.blue)
        self.win.blit( text, (x, y+20) )
