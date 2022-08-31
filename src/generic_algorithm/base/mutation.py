import random
import numpy as np

from src.configuration import MUTATION_PROB
from src.generic_algorithm.models.chromosome import Chromosome
from src.generic_algorithm.models.individual import Individual


class Mutation:

    def boundary_mutation(self, p, individual):

        for i in range(len(individual.chromosomes)):
            bound_index = random.randint(-1, 0)
            if random.random() <= p:
                individual.chromosomes[i].bin_chrom[bound_index] = 1 - individual.chromosomes[i].bin_chrom[bound_index]

        individual.update_fitness()

    def single_point_mutation(self, p, individual):
        return self.multi_point_mutation(p, 1, individual)

    def double_point_mutation(self, p, individual):
        return self.multi_point_mutation(p, 2, individual)

    def multi_point_mutation(self, p, point_number, individual):

        indexes = [i for i in range(len(individual.chromosomes[0].bin_chrom))]
        mutation_indexes = []
        for _ in range(point_number):
            mutation_index = random.choice(indexes)
            mutation_indexes.append(mutation_index)
            indexes.remove(mutation_index)

        for j in range(len(individual.chromosomes)):
            for i in mutation_indexes:
                if random.random() <= p:
                    individual.chromosomes[j].bin_chrom[i] = 1 - individual.chromosomes[j].bin_chrom[i]

        individual.update_fitness()

    def uniform_mutation(self, individual, start, end, precision):

        if random.random() > MUTATION_PROB:
            return individual

        return Individual(chromosomes=[individual.chromosomes[random.randint(0, 1)], Chromosome(start, end, precision)])

    def gaussian_mutation(self, individual, start, end):

        if random.random() > MUTATION_PROB:
            return individual

        x = individual.chromosomes[0].representation
        y = individual.chromosomes[1].representation
        sigma = abs(end - start) / 10
        z = np.random.normal(0, sigma)
        new_x = x + z
        if new_x < start:
            new_x = start
        if new_x > end:
            new_x = end
        new_y = y + z
        if new_y < start:
            new_y = start
        if new_y > end:
            new_y = end
        return Individual(chromosomes=[Chromosome(representation=new_x), Chromosome(representation=new_y)])
