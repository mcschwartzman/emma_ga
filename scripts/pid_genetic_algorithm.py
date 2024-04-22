from random import random

from genome import Genome

print("initializing genetic algorithm")

# Simulation targets
p_target = 5
i_target = 8
d_target = 7
metric_target = p_target * i_target * d_target

# Important Algorithm values
population_cap = 16
generation_size = 8

def initialize_population():

    population = []

    for i in range(population_cap):

        population.append(Genome(random(), random(), random()))

    return population

print(initialize_population())