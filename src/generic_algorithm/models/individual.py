from src.generic_algorithm.models.chromosome import Chromosome


class Individual:
    def __init__(self, start, end, precision):
        self.chromosomes = [Chromosome(start, end, precision) for _ in range(2)]
        self.fitness = self.get_fitness()

    def get_fitness(self):
        x1 = self.chromosomes[0].decode_binary_chain()
        x2 = self.chromosomes[1].decode_binary_chain()
        return self.booth_function(x1, x2)

    def update_fitness(self):
        self.fitness = self.get_fitness()

    def booth_function(self, x1, x2):
        return (x1 + 2 * x2 - 7) ** 2 + (2 * x1 + x2 - 5) ** 2
