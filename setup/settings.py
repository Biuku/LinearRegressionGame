""" April 5, 2021 """

import pygame


class Settings:

    def __init__(self):
        self.win_w = 1500
        self.win_h = 800

        self.clock = pygame.time.Clock()
        self.FPS = 60

        ### Colours
        self.white, self.black = (255, 255, 255), (0, 0, 0)
        self.light_grey, self.grey, self.dark_grey = (200, 200, 200), (100,100,100), (45, 45, 45)
        self.blue, self.light_blue = (190, 170, 255), (164, 150, 255),
        self.red, self.light_red = (235, 52, 52), (255, 175, 175)

        ## Colour styles
        self.object1_538 = (217, 240, 222)
        self.object2_538 = (255, 234, 217)
        self.light_grey_object_538 = (221, 221, 221)

        ### Fonts
        self.small_font = pygame.font.SysFont('lucidasans', 10)
        self.med_font = pygame.font.SysFont('lucidasans', 12)

        ### Lookups
