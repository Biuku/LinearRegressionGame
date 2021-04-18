""" April 12, 2021 """

import pygame


class Settings:

    def __init__(self):
        self.win_w = 1800
        self.win_h = 1000
        self.border_gap = 0.03 ## In percent

        self.clock = pygame.time.Clock()
        self.FPS = 120

        ### Colours
        self.white, self.black = (255, 255, 255), (0, 0, 0)
        self.light_grey, self.grey, self.dark_grey = (221, 221, 221), (150,150,150), (45, 45, 45)
        self.blue, self.light_blue = (190, 170, 255), (230, 230, 255),
        self.red, self.light_red = (235, 52, 52), (255, 175, 175)

        ## Colour styles
        self.object1_538 = (217, 240, 222)
        self.object2_538 = (255, 234, 217)

        ### Fonts
        self.small_font = pygame.font.SysFont('lucidasans', 11)
        self.med_font = pygame.font.SysFont('lucidasans', 12)
