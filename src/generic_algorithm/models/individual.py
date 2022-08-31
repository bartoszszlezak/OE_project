from src.generic_algorithm.models.chromosome import Chromosome


class Individual:
    def __init__(self, start = None, end = None, precision = None, chromosomes = None):
        self.chromosomes = [Chromosome(start, end, precision) for _ in range(2)] if chromosomes is None else chromosomes
        self.fitness = self.get_fitness()

    def get_fitness(self):
        x1 = self.chromosomes[0].representation
        x2 = self.chromosomes[1].representation
        return self.booth_function(x1, x2)

    def update_fitness(self):
        self.fitness = self.get_fitness()

    def booth_function(self, x1, x2):
        return (x1 + 2 * x2 - 7) ** 2 + (2 * x1 + x2 - 5) ** 2
