# Selection types
SELECTION_BEST = "SELECTION_BEST"
SELECTION_TOURNAMENT = "SELECTION_TOURNAMENT"
SELECTION_ROULETTE = "SELECTION_ROULETTE"

# Crossover types
CROSSOVER_HOMOGENOUS = "CROSSOVER_HOMOGENOUS"
CROSSOVER_SINGLE_POINT = "CROSSOVER_SINGLE_POINT"
CROSSOVER_DOUBLE_POINT = "CROSSOVER_DOUBLE_POINT"
ARITHMETIC_CROSSOVER = "ARITHMETIC_CROSSOVER"
LINEAR_CROSSOVER = "LINEAR_CROSSOVER"
BLEND_CROSSOVER_ALPHA = "BLEND_CROSSOVER_ALPHA"
BLEND_CROSSOVER_ALPHA_BETA = "BLEND_CROSSOVER_ALPHA_BETA"
AVERAGE_CROSSOVER = "AVERAGE_CROSSOVER"

# Mutation types
MUTATION_BOUNDARY = "MUTATION_BOUNDARY"
MUTATION_SINGLE_POINT = "MUTATION_SINGLE_POINT"
MUTATION_DOUBLE_POINT = "MUTATION_DOUBLE_POINT"
UNIFORM_MUTATION = "UNIFORM_MUTATION"
GAUSSIAN_MUTATION = "GAUSSIAN_MUTATION"

# Algorithm goal
MAXIMUM = "MAXIMUM"
MINIMUM = "MINIMUM"

START = -10
END = 10
PRECISION = 5
POPULATION_SIZE = 100
NUMBER_OF_EPOCHS = 200
SELECTION_PERCENT = 0.3
SELECTION_NO_GROUPS = 50
CROSSOVER_PROB = 0.8
MUTATION_PROB = 0.01
INVERSION_PROB = 0.3
ELITE_PERCENT = 0.2
ALPHA = 0.25
BETA = 0.7


class Config:
    def __init__(self):
        self.start = None
        self.end = None
        self.precision = None
        self.pop_size = None
        self.no_epochs = None
        self.selection_type = None
        self.selection_percent = None
        self.selection_no_groups = None
        self.crossover_type = None
        self.crossover_probability = None
        self.mutation_type = None
        self.mutation_probability = None
        self.inversion_probability = None
        self.elite_percent = None
        self.algorithm_goal = None
        self.alpha = None
        self.beta = None
