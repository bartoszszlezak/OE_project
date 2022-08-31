import random


class Inversion:

    def invert(self, individual, probability):
        if not random.random() <= probability:
            return

        for i in range(len(individual.chromosomes)):
            indexes = [i for i in range(len(individual.chromosomes[i].bin_chrom))]
            x1 = random.choice(indexes)
            indexes.remove(x1)
            x2 = random.choice(indexes)

            min_index = min(x1, x2)
            max_index = max(x1, x2)

            sub_array = individual.chromosomes[i].bin_chrom[min_index: max_index]
            sub_array = sub_array[::-1]

            sub_array_1 = individual.chromosomes[i].bin_chrom[:min_index]
            sub_array_2 = individual.chromosomes[i].bin_chrom[max_index:]

            individual.chromosomes[i].bin_chrom = sub_array_1 + sub_array + sub_array_2

        individual.update_fitness()
