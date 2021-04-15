""" April 12, 2021 """


import math as m
import random as r
import numpy as np

class Regression:
    def __init__(self, arr):
        self.arr = arr




    def get_euclid(self, start, fin):
        x1, y1 = start
        x2, y2 = fin

        return m.sqrt( (x2-x1)**2 + (y2-y1)**2)
