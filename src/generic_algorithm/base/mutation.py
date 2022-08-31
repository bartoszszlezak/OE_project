import random


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
