""" April 7, 2021 """

""" Background objects are like painted scenery. No functional interactions."""

import pygame
from setup.settings import Settings


class Plot:

    def __init__(self, win):
        pygame.init()
        self.win = win
        self.set = Settings()

    def draw(self, arr):

        ### Draw axes

        w, h = 1000, 500

        left, top = 200, 100
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