""" April 12, 2021 """

import pygame
import math as m
import random as r


class Printr:
    def __init__(self, win, set):
        pygame.init()
        self.win = win
        self.set = set


    def coord_printr(self, data, x, y, c):
        text = self.set.small_font.render(data, True, c)
        self.win.blit( text, (x, y) )



    def print_instructions(self, b0, b1, SSE, y_int, slope, sse):
        x = self.set.win_w * 0.86 ## lower number --> leftward
        y = self.set.win_h * 0.06 ## lower number --> upward

        texts = [
            'INSTRUCTIONS',
            '  · Click = move',
            '  · d = Clockwise',
            '  · a = Counter-clockwise',
            '  · Right-click = fast clockwise',
            '  · c = Show centroid',
            '  · i = Show intercepts',
            '',
            'BEST FIT LINE',
            '  · Y intercept:  ' + str(round(b0, 4)),
            '  · Slope:  ' + str(round(b1, 4)),
            '  · SSE: ' + str(round(SSE, 4)),
            '',
            'YOUR LINE',
            "  · Y intercept: " + str(round(y_int, 4)),
            "  · Slope: " + str(round(slope, 4)),
            #"  · Angle: " + str(round(angle, 2)) + "°",
            "  · SSE: " + str(round(sse, 4)),
            '',
            ]

        for text in texts:
            print_instructions = self.set.small_font.render(text, True, self.set.grey)
            self.win.blit( print_instructions, (x, y) )
            y += 22



    def format_rss(self, rss):
        if rss:
            return ("{:,}".format(int(rss)))
        return str(0)
