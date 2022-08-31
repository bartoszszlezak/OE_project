import math
import random

import numpy as np


class Chromosome:

    def __init__(self, start, end, precision):
        self.start = start
        self.end = end
        self.precision = precision
        self.bin_chrom = self.binary_chrom()

    def length_of_binary_chain(self):
        return int(math.ceil(np.log2((self.end - self.start) * 10 ** self.precision) + np.log2(1)))

    def decode_binary_chain(self):
        length = len(self.bin_chrom)
        binary_chain = ''.join(map(str, self.bin_chrom))
        return self.start + int(binary_chain, 2) * (self.end - self.start) / (pow(2, length) - 1)

    def binary_chrom(self):
        return [random.randint(0, 1) for _ in range(0, self.length_of_binary_chain())]
