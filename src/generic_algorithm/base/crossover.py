import random
from copy import deepcopy


class Crossover:

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
