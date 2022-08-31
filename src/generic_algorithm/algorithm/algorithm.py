from src.generic_algorithm.algorithm.algorithm_facade import AlgorithmFacade
from src.generic_algorithm.models.individual import Individual

import numpy as np


def run_algorithm(config):

    population = [Individual(config.start, config.end, config.precision) for _ in range(config.pop_size)]

    facade = AlgorithmFacade(config)

    result_fitness = []
    result_average = []
    result_standard_deviation = []

    for _ in range(config.no_epochs):
        # elita
        elites, population = facade.elite_strategy(population)

        # selekcja
        population = facade.selection(population)

        # krzyżowanie
        children = []
        while len(population) + len(children) + len(elites) <= config.pop_size:

            new_bin1, new_bin2 = facade.crossover(population)

            new_ind_1 = Individual(config.start, config.end, config.precision)
            new_ind_2 = Individual(config.start, config.end, config.precision)

            for index in range(len(new_bin1)):
                new_ind_1.chromosomes[index].bin_chrom = new_bin1[index]
                new_ind_2.chromosomes[index].bin_chrom = new_bin2[index]

            new_ind_1.update_fitness()
            new_ind_2.update_fitness()

            children.append(new_ind_1)
            children.append(new_ind_2)

        population += children

        for index in range(len(population)):
            facade.mutation(population, index)

        for index in range(len(population)):
            facade.invert(population[index])

        population += elites

        # Wyniki
        # Najlepsze osobniki
        sorted_pop = facade.get_sorted_pop(population)
        result_fitness.append((sorted_pop[0].chromosomes[0].decode_binary_chain(),
                               sorted_pop[0].chromosomes[1].decode_binary_chain(), sorted_pop[0].fitness))

        sorted_fitness = facade.map_pop_to_fitness(sorted_pop)

        # Średnia
        result_average.append(np.average(sorted_fitness))

        # Odchylenie standardowe
        result_standard_deviation.append(np.std(sorted_fitness))

    return result_fitness, result_average, result_standard_deviation
