""" April 7, 2021 """

""" Background objects are like painted scenery. No functional interactions."""

import pygame
from setup.settings import Settings


class Plot:

    def __init__(self, win):
        pygame.init()
        self.win = win
        self.set = Settings()
        self.w = 1500
        self.h = 750

    def draw(self, arr):

        ### Draw axes


        w, h = self.w, self.h

        left, top = 120, 100
        right, bottom = left + w, top + h

        zero_zero = (left, bottom)

        pygame.draw.line(self.win, self.set.light_grey, (left, top), zero_zero, 2)
        pygame.draw.line(self.win, self.set.light_grey, zero_zero, (right, bottom), 2)


        ### Draw array dots
        c = self.set.light_grey

        for pair in arr:
            x = pair[0] + left
            y = pair[1] + top

            pygame.draw.circle(self.win, c, (x, y), 1, 0)

    def configure_data(self, arr):

        arr = -1*arr
        return arr
        
        x = arr[:,0]
        x_factor = self.w / x.max()
        arr[:,0] = arr[:,0] * x_factor

        arr = arr.astype(int)

        return arr
