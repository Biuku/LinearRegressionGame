""" APRIL 5, 2021 """

import pygame
from setup.settings import Settings

class PygameBasics:
    def __init__(self):
        pygame.init()
        self.set = Settings()
        self.win = pygame.display.set_mode((self.set.win_w, self.set.win_h))

    """ EVENTS """

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    self.left_click_events()

                if pygame.mouse.get_pressed()[2]:
                    self.right_click_events()

            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_up_events()

            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.keyup_events(event)

            elif event.type == pygame.QUIT:
                pygame.quit(), quit()



    """ Draw background """

    def draw_page_border(self):
        """ Draw rectangle around the entire page to give it an edge """

        x = self.set.win_w * self.set.border_gap
        y = self.set.win_h * self.set.border_gap

        w =  self.set.win_w * (1 - (2 * self.set.border_gap))
        h = self.set.win_h * (1 - (2 * self.set.border_gap))

        c = self.set.light_grey
        thick = 3

        pygame.draw.rect(self.win, c, pygame.Rect(x, y, w, h), thick)
