from time import sleep

from genetic_algorithm import GeneticAlgorithm

if __name__ == '__main__':

    # Simulation targets (not in use yet!)
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

        # measure how close each genome's product is to 1
        new_algorithm.evaluate_genomes(1)

        # sort all genomes in the population by their fitness metric
        new_algorithm.sort_population()

        print([genome.fitness_metric for genome in new_algorithm.population])

        # remove the bottom performers (number is the same as generation_size)
        new_algorithm.cull_population()

        # spawn a new generation (first adding to unevaluated)
        new_algorithm.new_generation()

        # uncomment to slow things down a tiny bit
        # sleep(1)    