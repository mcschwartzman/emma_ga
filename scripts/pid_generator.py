from time import sleep

from genetic_algorithm import GeneticAlgorithm

if __name__ == '__main__':

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

    while(1):

        new_algorithm.evaluate_genomes(1)

        # print([genome.fitness_metric for genome in new_algorithm.population])

        new_algorithm.sort_population()

        print([genome.fitness_metric for genome in new_algorithm.population])

        new_algorithm.cull_population()

        # print([genome.fitness_metric for genome in new_algorithm.population])

        new_algorithm.new_generation()

        # print([genome.fitness_metric for genome in new_algorithm.population])

        sleep(5)