import random
from copy import deepcopy
from functools import cmp_to_key

from src.configuration import CROSSOVER_PROB
from src.generic_algorithm.models.chromosome import Chromosome
from src.generic_algorithm.models.individual import Individual


class Crossover:

    def __init__(self, ind_comparator, alpha, beta, start, end):
        self.ind_comparator = ind_comparator
        self.alpha = alpha
        self.beta = beta
        self.start = start
        self.end = end

    def arithmetic_crossover(self, ind_1, ind_2):

        if random.random() > CROSSOVER_PROB:
            return [ind_1, ind_2]

        k = random.random()
        k_reverse = 1 - k
        x1 = ind_1.chromosomes[0].representation
        y1 = ind_1.chromosomes[1].representation

        x2 = ind_2.chromosomes[0].representation
        y2 = ind_2.chromosomes[1].representation

        # Witam tutaj moze byc problem
        x1_new = k * x1 + k_reverse * x2
        y1_new = k * y1 + k_reverse * y2

        x2_new = k_reverse * x1 + k * x2
        y2_new = k_reverse * y1 + k * y2


        return [Individual([Chromosome(representation=x1_new), Chromosome(representation=y1_new)])
            , Individual([Chromosome(representation=x2_new), Chromosome(representation=y2_new)])]

    def linear_crossover(self, ind_1, ind_2):

        if random.random() > CROSSOVER_PROB:
            return [ind_1, ind_2]

        x1 = ind_1.chromosomes[0].representation
        y1 = ind_1.chromosomes[1].representation

        x2 = ind_2.chromosomes[0].representation
        y2 = ind_2.chromosomes[1].representation
        z_ind = [(x1 + x2) / 2, (y1 + y2) / 2]
        v_ind = [3 * x1 / 2 - x2 / 2, 3 * y1 / 2 - y2 / 2]
        w_ind = [3 * x2 / 2 - x1 / 2, 3 * y2 / 2 - y1 / 2]

        ind_array = [z_ind, v_ind, w_ind]
        result = []
        for ind in ind_array:
            new_ind = Individual([Chromosome(representation=ind[0]), Chromosome(representation=ind[1])])
            result.append(new_ind)

        sorted_array = sorted(result, key=cmp_to_key(self.ind_comparator))

        return sorted_array[:-1]

    # Sprawdzić bo we wzorze jest max(y1,xy), ale liczone jest potem jak u nas, trzeba sprawdzić

    def blend_crossover_alpha(self, ind_1, ind_2):

        if random.random() > CROSSOVER_PROB:
            return [ind_1,ind_2]

        x1 = ind_1.chromosomes[0].representation
        y1 = ind_1.chromosomes[1].representation

        x2 = ind_2.chromosomes[0].representation
        y2 = ind_2.chromosomes[1].representation

        d1 = abs(x1 - x2)
        d2 = abs(y1 - y2)

        new_ind_array = []
        while len(new_ind_array) < 2:
            u1 = random.uniform(min(x1, x2) - self.alpha * d1, max(x1, x2) + self.alpha * d1)
            u2 = random.uniform(min(y1, y2) - self.alpha * d2, max(y1, y2) + self.alpha * d2)

            if u1 >= self.start and u1 <= self.end and u2 >= self.start and u2 <= self.end:
                new_ind_array.append(Individual([Chromosome(representation=u1), Chromosome(representation=u2)]))

        return new_ind_array

    def blend_crossover_alpha_beta(self, ind_1, ind_2):

        if random.random() > CROSSOVER_PROB:
            return [ind_1, ind_2]

        x1 = ind_1.chromosomes[0].representation
        y1 = ind_1.chromosomes[1].representation

        x2 = ind_2.chromosomes[0].representation
        y2 = ind_2.chromosomes[1].representation

        d1 = abs(x1 - x2)
        d2 = abs(y1 - y2)

        new_ind_array = []
        while len(new_ind_array) < 2:
            u1 = random.uniform(min(x1, x2) - self.alpha * d1, max(x1, x2) + self.beta * d1)
            u2 = random.uniform(min(y1, y2) - self.alpha * d2, max(y1, y2) + self.beta * d2)

            if u1 >= self.start and u1 <= self.end and u2 >= self.start and u2 <= self.end:
                new_ind_array.append(Individual([Chromosome(representation=u1), Chromosome(representation=u2)]))

        return new_ind_array

    def average_crossover(self, ind_1, ind_2):

        if random.random() > CROSSOVER_PROB:
            return [ind_1, ind_2]

        x1 = ind_1.chromosomes[0].representation
        y1 = ind_1.chromosomes[1].representation

        x2 = ind_2.chromosomes[0].representation
        y2 = ind_2.chromosomes[1].representation

        u1 = (x1 + x2) / 2
        u2 = (y1 + y2) / 2

        return Individual([Chromosome(representation=u1), Chromosome(representation=u2)]), Individual([Chromosome(representation=u1), Chromosome(representation=u2)])

    def single_point_crossover(self, ind_1, ind_2):
        return self.multi_point_crossover(1, ind_1, ind_2)

    def double_point_crossover(self, ind_1, ind_2):
        return self.multi_point_crossover(2, ind_1, ind_2)

    def multi_point_crossover(self, point_number, ind_1, ind_2):

        points = [i for i in range(len(ind_1.chromosomes[0].bin_chrom))]
        pivots = []
        for _ in range(point_number):
            random_pivot = random.choice(points)
            pivots.append(random_pivot)
            points.remove(random_pivot)

        pivots.sort()

        pivot_index = 0

        sub_arr_1 = []
        sub_arr_2 = []
        for i in range(len(ind_1.chromosomes)):
            ind_cpy_1 = []
            ind_cpy_2 = []
            for j in range(len(ind_1.chromosomes[i].bin_chrom)):
                if pivot_index < len(pivots) and j == pivots[pivot_index]:
                    pivot_index = pivot_index + 1

                if pivot_index % 2 == 0:
                    ind_cpy_1.append(ind_1.chromosomes[i].bin_chrom[j])
                    ind_cpy_2.append(ind_2.chromosomes[i].bin_chrom[j])
                else:
                    ind_cpy_1.append(ind_2.chromosomes[i].bin_chrom[j])
                    ind_cpy_2.append(ind_1.chromosomes[i].bin_chrom[j])
            sub_arr_1.append(ind_cpy_1)
            sub_arr_2.append(ind_cpy_2)

        return sub_arr_1, sub_arr_2

    def homogeneous_crossover(self, ind_1, ind_2, p):
        if p > 1 or p < 0:
            raise Exception('Wrong probability value.')

        ind_1_cpy = []
        ind_2_cpy = []

        for i in range(len(ind_1.chromosomes)):
            ind_1_cpy.append(list(deepcopy(ind_1.chromosomes[i].bin_chrom)))
            ind_2_cpy.append(list(deepcopy(ind_2.chromosomes[i].bin_chrom)))

        for i in range(0, len(ind_1_cpy)):
            for j in range(1, len(ind_1_cpy[i])):
                if random.random() >= p:
                    ind_1_cpy[i][j], ind_2_cpy[i][j] = ind_2_cpy[i][j], ind_1_cpy[i][j]

        return ind_1_cpy, ind_2_cpy
