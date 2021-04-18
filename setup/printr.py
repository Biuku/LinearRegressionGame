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



    def print_instructions(self, for_angle, opp_angle, rss):
        # x = self.set.win_w * 0.87 ## lower number --> leftward
        x = self.set.win_w * 0.8 ## lower number --> leftward
        y = self.set.win_h * 0.05 ## lower number --> upward
        rss = self.format_rss(rss)

        texts = [
            "For angle: " + str(round(for_angle, 2)) + "°",
            "Opp angle: " + str(round(opp_angle, 2)) + "°",
            "RSS: " + rss,
            'Click = move',
            'Right-click = fast clockwise',
            'd = Clockwise',
            'a = Counter-clockwise',
            'c = Snap to centroid',
            'i = Toggle show intercepts',
            ' ',
            ]

        for text in texts:
            print_instructions = self.set.med_font.render(text, True, self.set.grey)
            self.win.blit( print_instructions, (x, y) )
            y += 22



    def format_rss(self, rss):
        if rss:
            return ("{:,}".format(int(rss)))
        return str(0)
