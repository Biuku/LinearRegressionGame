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


class FitLine:
    def __init__(self, win):
        pygame.init()
        self.win = win
        self.set = Settings()

        self.slope = -1.2
        self.start = [180, 200]
        self.end = self.get_end()

    def get_end(self):

        x = 200 + 500
        y = x*(-1 * self.slope)

        return [x, y]

    def draw(self):
        pygame.draw.line(self.win, self.set.red, tuple(self.start), tuple(self.end), 3)

    def move(self, mx, my):
        
        for thing in [self.start, self.end]:
            thing[0] += mx
            thing[1] += my
