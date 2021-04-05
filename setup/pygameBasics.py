""" APRIL 5, 2021 """

import pygame
from setup.settings import Settings
from setup.background import Background

class PygameBasics:
    def __init__(self):
        pygame.init()
        self.set = Settings()
        self.win = pygame.display.set_mode((self.set.win_w, self.set.win_h))
        self.background = Background(self.win)

    """ EVENTS """

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down_events()

            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_up_events()

            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

            elif event.type == pygame.QUIT:
                pygame.quit(), quit()


    """ UPDATES """

    def update_screen(self):
        self.background.draw()
        pygame.display.update()
