import math
import random

from functools import cmp_to_key

from src.configuration import MINIMUM


class Selection:

    def __init__(self, ind_comparator):
        self.ind_comparator = ind_comparator

    def selection_best(self, percent, individuals):
        result = sorted(individuals, key=cmp_to_key(self.ind_comparator))
        number_of_best = math.ceil(len(individuals) * percent)
        return result[:number_of_best]

    def tournament(self, no_groups, individuals):

        no_individuals = int(len(individuals) / no_groups)
        rest = len(individuals) % no_groups
        res = []
        for i in range(0, no_groups):
            x = 0
            if rest > 0:
                x = x + 1
                rest = rest - 1
            res.append(no_individuals + x)

        buff = []
        for n in res:
            sub_pop = []
            for i in range(0, n):
                rand_n = random.randint(0, len(individuals) - 1)
                sub_pop.append(individuals[rand_n])
                individuals.pop(rand_n)

            buff.append(sorted(sub_pop, key=cmp_to_key(self.ind_comparator))[0])
        return buff

    # TODO AM
    def roulette(self, individuals, goal, percent):

        results = []
        if goal == MINIMUM:
             for i in range (0,int(len(individuals)) - 1):
                results.append([individuals[i], 1/individuals[i].fitness])
        else:
             for i in range (0,int(len(individuals)) - 1):
                 results.append([individuals[i], individuals[i].fitness])

        total = 0
        for i in range(0,len(results)-1):
            total = total + results[i][1]

        for i in range(len(results)):
            if (i == 0):
                results[i][1] = results[i][1] / total
            else:
                results[i][1] = results[i][1] / total + results[i - 1][1]

        def select(results, value):
            min = 1
            clotest_value_index = 0
            for i in range(len(results)):
                diff = abs(results[i][1] - value)
                if (diff < min):
                    min = diff
                    clotest_value_index = i
            if (value > results[clotest_value_index][1]):
                clotest_value_index = clotest_value_index + 1
            return results[clotest_value_index]

        selection_list = []
        number_of_best = math.ceil(len(results) * percent)

        for i in range(number_of_best):
            random_number = random.uniform(0, 1)
            selected = select(results, random_number)
            selected_obj = selected[0]
            selection_list.append(selected_obj)
            results.remove(selected)

        return selection_list

