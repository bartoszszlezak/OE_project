import math
import random
from functools import cmp_to_key

from src.generic_algorithm.base.selection import Selection
from src.generic_algorithm.base.crossover import Crossover
from src.generic_algorithm.base.inversion import Inversion
from src.generic_algorithm.base.mutation import Mutation
from src.configuration import *


class AlgorithmFacade:

    def __init__(self, config: Config):
        self.config = config
        self.selection_helper = Selection(self.ind_comparator)
        self.crossover_helper = Crossover(self.ind_comparator, self.config.alpha, self.config.beta,
                                          self.config.start, self.config.end)
        self.mutation_helper = Mutation()
        self.inversion_helper = Inversion()

    def selection(self, population):

        if self.config.selection_type == SELECTION_BEST:
            return self.selection_helper.selection_best(self.config.selection_percent, population)

        if self.config.selection_type == SELECTION_TOURNAMENT:
            return self.selection_helper.tournament(self.config.selection_no_groups, population)

        if self.config.selection_type == SELECTION_ROULETTE:
            # TODO AM
            return self.selection_helper.roulette(population, self.config.algorithm_goal, self.config.selection_percent)

    def crossover(self, population):
        indexes = [i for i in range(len(population) - 1)]
        index_1 = random.choice(indexes)
        indexes.remove(index_1)
        index_2 = random.choice(indexes)

        if self.config.crossover_type == CROSSOVER_HOMOGENOUS:
            return self.crossover_helper.homogeneous_crossover(population[index_1], population[index_2],
                                                               self.config.crossover_probability)

        if self.config.crossover_type == CROSSOVER_SINGLE_POINT:
            return self.crossover_helper.single_point_crossover(population[index_1], population[index_2])

        if self.config.crossover_type == CROSSOVER_DOUBLE_POINT:
            return self.crossover_helper.double_point_crossover(population[index_1], population[index_2])

        if self.config.crossover_type == ARITHMETIC_CROSSOVER:
            return self.crossover_helper.arithmetic_crossover(population[index_1], population[index_2])

        if self.config.crossover_type == LINEAR_CROSSOVER:
            return self.crossover_helper.linear_crossover(population[index_1], population[index_2])

        if self.config.crossover_type == BLEND_CROSSOVER_ALPHA:
            return self.crossover_helper.blend_crossover_alpha(population[index_1], population[index_2])

        if self.config.crossover_type == BLEND_CROSSOVER_ALPHA_BETA:
            return self.crossover_helper.blend_crossover_alpha_beta(population[index_1], population[index_2])

        if self.config.crossover_type == AVERAGE_CROSSOVER:
            return self.crossover_helper.average_crossover(population[index_1], population[index_2])

    def mutation(self, population, index):

        if self.config.mutation_type == MUTATION_BOUNDARY:
            self.mutation_helper.boundary_mutation(self.config.mutation_probability, population[index])
            return

        if self.config.mutation_type == MUTATION_SINGLE_POINT:
            self.mutation_helper.single_point_mutation(self.config.mutation_probability, population[index])
            return

        if self.config.mutation_type == MUTATION_DOUBLE_POINT:
            self.mutation_helper.double_point_mutation(self.config.mutation_probability, population[index])

        if self.config.mutation_type == UNIFORM_MUTATION:
            return self.mutation_helper.uniform_mutation(population[index], self.config.start,
                                                  self.config.end, self.config.precision)

        if self.config.mutation_type == GAUSSIAN_MUTATION:
            return self.mutation_helper.gaussian_mutation(population[index], self.config.start, self.config.end)

    def invert(self, individual):
        self.inversion_helper.invert(individual, self.config.inversion_probability)

    def elite_strategy(self, population):
        sorted_individuals = sorted(population, key=cmp_to_key(self.ind_comparator))

        break_point = int(len(population) * self.config.elite_percent)

        return sorted_individuals[:break_point], sorted_individuals[break_point:]

    def ind_comparator(self, ind_1, ind_2):

        direction = 0
        if self.config.algorithm_goal == MAXIMUM:
            direction = 1
        elif self.config.algorithm_goal == MINIMUM:
            direction = -1

        try:
            return direction * int(math.fabs(ind_2.fitness) - math.fabs(ind_1.fitness))
        except:
            return None

    def get_sorted_pop(self, pop):
        return sorted(pop, key=cmp_to_key(self.ind_comparator))

    def map_pop_to_fitness(self, pop):
        result = []
        for individual in pop:
            result.append(individual.fitness)

        return result
