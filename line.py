""" April 7, 2021 """


import pygame
import math as m
from setup.settings import Settings

class FitLine:
    def __init__(self, win):
        pygame.init()
        self.win = win
        self.set = Settings()


        self.length = 300
        self.angle = 45 ## 'angle' for trig; 'slope' for regression
        self.mid = [400, 300] ### Line always anchors to mid

        self.start = self.mid
        self.end = self.mid
        self.update_points()

        self.rss = 0


    def rotate(self, rotating, counter_rotating, super_rotating):
        speed = 0.1

        if rotating:
            self.angle += speed

        if counter_rotating:
            self.angle -= speed

        if super_rotating:
            self.angle += 2

        self.update_points()


    def update_points(self):
        """ Update the start and end points if line moves/rotates"""

        x, y = self.mid
        rads = m.radians(self.angle)

        ## Draw mid to end half of line
        end_x = x + m.cos(rads) * self.length
        end_y = y + m.sin(rads) * self.length
        self.end = (end_x, end_y)

        ## Draw start to mid half of line
        start_x = x + m.cos(rads) * (-1 * self.length)
        start_y = y + m.sin(rads) * (-1 * self.length)
        self.start = (start_x, start_y)


    def update_RSS(self, arr):
        """
        1. Iterate over all coordinates in np array
        2. Use slope function to find the y coordinate of the line at that array x coordinate
            2.5 Add two tuples to a list: the arr (x,y) and the (arr x, line y)
                - To do -- iterate through this list to build the vertical intercepts
        3. The difference = the error -- add to a list
        4. Update the RSS as I go (+=)
        5. Print RSS on the right -- minimizing this is good
        """

        error_lines = []
        rss = 0

        for pair in arr:
            x, y = pair
            y_on_line = self.x_intercept(x, y)
            rss = y_on_line**2

        self.rss = rss

    def x_intercept(self, mx, my):
        start_x, start_y = self.start
        angle = m.radians(self.angle)

        """ TRIG APPROACH """
        opposite = mx - start_x
        hypot = opposite / m.sin(angle)
        adjacent = m.cos(angle) * hypot

        #So, y on the line should be start_y + adjacent
        y_on_line = round( start_y + adjacent, 2)

        return y_on_line

        #self.print_coord( (mx, y_on_line) )

    def get_slope(self):
        """ Slope = rise/run """
        x1, y1 = self.start
        x2, y2 = self.end
        return (y2 - y1) // (x2 - x1)

    def move(self, moving):
        if moving:
            mx, my = pygame.mouse.get_rel()

            self.mid[0] += mx
            self.mid[1] += my

    def printr(self):
        c = self.set.grey
        x = self.set.win_w * 0.85 ## lower number --> leftward
        y = self.set.win_h * 0.07 ## lower number --> upward

        texts = [
            "Angle: " + str(round(self.angle, 2)) + "°",
            "RSS: " + str(round(self.rss, 2)),
            'd = Clockwise',
            'a = Counter-clockwise',
            'Right-click = fast clockwise'
            ]
        for text in texts:

            printr = self.set.med_font.render(text, True, c)
            self.win.blit( printr, (x, y) )
            y += 20


    def draw(self):
        pygame.draw.line(self.win, self.set.grey, tuple(self.start), (self.end), 2)

        ## Start a small circle denoting the mid
        pygame.draw.circle(self.win, self.set.black, self.mid, 6, 0)

        ## Start a temporary circle denoting the start
        pygame.draw.circle(self.win, self.set.red, self.start, 6, 0)

        self.print_coord(self.mid)

        self.printr()

    def print_coord(self, coord):
        ### Draw mid coordinates near mid
        c = self.set.grey

        x, y = coord
        x += 15
        y -= 20

        text = str(coord)
        printr = self.set.med_font.render(text, True, c)
        self.win.blit( printr, (x, y) )