""" April 5, 2021 """

""" Background objects are like painted scenery. No functional interactions."""

import pygame
from setup.settings import Settings

class Background:
    def __init__(self, win):
        pygame.init()
        self.win = win
        self.set = Settings()

        ## Pager border
        self.border_gap = .03 ## In percent


    def draw(self):
        """ Called from Main """
        self.draw_page_border()

    def draw_page_border(self):
        """ Draw rectangle around the entire page to give it an edge """

        x = self.set.win_w * self.border_gap
        y = self.set.win_h * self.border_gap

        w =  self.set.win_w * (1 - (2 * self.border_gap))
        h = self.set.win_h * (1 - (2 * self.border_gap))

        c = self.set.light_grey
        thick = 3

        pygame.draw.rect(self.win, c, pygame.Rect(x, y, w, h), thick)
