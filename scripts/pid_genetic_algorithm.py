from random import random

from genome import Genome

print("initializing genetic algorithm")

class GeneticAlgorithm(object):

    def __init__(self, population_cap, generation_size):

        self.population_cap = population_cap
        self.generation_size = generation_size

    def initialize_population(self):

        unevaluated = []

        for i in range(population_cap):

            unevaluated.append(Genome(random(), random(), random()))

        self.unevaluated = unevaluated

    def evaluate_genomes(self, desired_value):

        population = []

        for genome in self.unevaluated:

            # fitness metric evaluated manually
            product = genome.p_gain * genome.i_gain * genome.d_gain

            fitness_metric = desired_value - product

            genome.set_fitness_metric(fitness_metric)

            population.append(genome)

        self.population = population

        # print(self.population)



    def sort_population(self):

        # print(self.population)

        self.population = self.population.sort(key=lambda genome: genome.fitness_metric)

        # print(self.population)

    def cull_population(self):

        return

    def new_generation(self):

        return

    def evaluate_generation(self):

        return

# Simulation targets
p_target = 5
i_target = 8
d_target = 7
metric_target = p_target * i_target * d_target

# Important Algorithm values
population_cap = 16
generation_size = 8

new_algorithm = GeneticAlgorithm(population_cap, generation_size)
new_algorithm.initialize_population()
new_algorithm.evaluate_genomes(1)

print([genome.fitness_metric for genome in new_algorithm.population])

new_algorithm.sort_population()

print([genome.fitness_metric for genome in new_algorithm.population])

new_algorithm.cull_population()