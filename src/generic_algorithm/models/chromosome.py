import math
import random

import numpy as np


class Chromosome:

    def __init__(self, start=-10, end=10, precision=None, representation=None):
        self.start = start
        self.end = end
        self.precision = precision
        self.representation = self.generate_representation() if representation is None else representation


    def generate_representation(self):
        # return random.randint(start, end)
        if self.start is None or self.end is None:
            return random.uniform(-10, 10)
        return random.uniform(self.start, self.end)

