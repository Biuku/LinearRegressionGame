""" April 7, 2021 """


import pygame
import math as m
from setup.settings import Settings

class FitLine:
    def __init__(self, win):
        pygame.init()
        self.win = win
        self.set = Settings()

        self.start = [400, 400]
        #self.end = [600, 200]

        self.length = 300
        #self.mid = [300, 300]
        #self.slope = 1
        self.angle = -45



    def get_end_point(self):

        x, y = self.start

        rads = m.radians(self.angle)

        end_x = x + m.cos(rads) * self.length
        end_y = y + m.sin(rads) * self.length

        return (end_x, end_y)



    def draw(self):
        end = self.get_end_point()

        #pygame.draw.line(self.win, self.set.red, tuple(self.start), tuple(self.end), 3)
        pygame.draw.line(self.win, self.set.red, tuple(self.start), end, 3)


        ## Start a small circle denoting the start
        pygame.draw.circle(self.win, self.set.blue, self.start, 5, 0)

        self.printr()


    def rotate(self, rotating, reverse_rotating):
        """
        Theory -- it's not about trig, but about ...
        """
        if rotating:
            self.angle += 0.4

        if reverse_rotating:
            self.angle -= 0.4


    def printr(self):
        c = self.set.grey
        x = self.set.win_w * 0.85 ## lower number --> leftward
        y = self.set.win_h * 0.07 ## lower number --> upward

        text = str(round(self.angle, 2))
        printr = self.set.med_font.render(text, True, c)

        self.win.blit( printr, (x, y) )


    def move(self, moving):
        if moving:


            mx, my = pygame.mouse.get_rel()

            for point in [self.start, self.end]:
                point[0] += mx
                point[1] += my
