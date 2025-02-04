###############################################################################
#
#   proj04 CSE 231
#       Gene Sequencer Project
#           Takes a target value as an input
#               Checks to make sure the value is valid
#           Generates a random population of 100 with target length
#           Determines the 2 best individuals in random groups of 5
#           Mutates the 2 best individuals
#               Crosses the 2 individuals at a random point
#           Determines their fitness values
#               If fitness = 1 loop stops, else a new generation is created
#               A new population is created using the most fit individuals
#                   Program ends after 200 generations or the target is reached
#
###############################################################################

import random
#DO NOT CHANGE THIS
random.seed(10)

NUM_GENERATIONS = 200
NUM_POPULATION = 100
PROBABILITY_MUTATION = 0.2
PROBABILITY_CROSSOVER = 0.8
TOURNAMENT_SIZE = 5
ALPHABET = 'abcdefghijklmnopqrstuvwxyz '

BANNER = """
**************************************************************
Welcome to GeneticGuess Sentencer! 
This program will attempt to guess a sentence that you input. 
Simply input a sentence and the program will attempt to guess it!
**************************************************************
"""

INPUT = "Would you like to continue? (y/n) "

GUESS_INPUT = "\nPlease input the sentence you would like the program to guess: "
INCORRECT_INPUT = "\nIncorrect input. Please try again.\n"
GUESS_RESULT = "\n\nGeneticGuess results:"
GENERATION = "Generation: "
EARLY = "I found the sentence early!"
BEST = "\nBest Individual: "
THANK_YOU = "\n\nThank you for using GeneticGuess Sentencer!"

# Determines the similarities between the target value and the individual
def fitness(target, individual):
    fitness_count = 0
    for ch in range(len(target)):
        # Determines if each letter in the string is the same as the target
        if target[ch] == individual[ch]:
            fitness_count += 1

    # This value is the overall % likeness value
    total_fitness = fitness_count / len(target)
    return total_fitness
    pass


def five_tournament_selection(population, target):
    # TOURNAMENT SIZE can change to be different depending on the sort
    best_individual_val = -1
    best_individual = ''

    # Selects 5 random individuals in the list
    for i in range(TOURNAMENT_SIZE):
        # Creation of the random individual
        pos = random.randint(0, NUM_POPULATION - 1) * len(target)
        individual = population[pos:(pos + len(target))]
        # Determines the individuals fitness
        individual_fitness = fitness(target, individual)

        # Compares fitness values to determine the most fit
        if individual_fitness > best_individual_val:
            best_individual = individual
            best_individual_val = individual_fitness

    # Returns the most fit individual
    return best_individual
    pass

# Makes a population of 100 individuals with the length of the target
def make_population(target):
    pop_len = target * NUM_POPULATION
    counter = 0
    population = ''
    while counter < len(pop_len):
        # Generates a 'random' letter for each character in the population
        population += random.choice(ALPHABET)
        counter += 1

    return population
    pass

# Mutates an individual so change may occur in the population
def mutation(individual):
    # Empty final string
    new_individual = ''
    for i in range(len(individual)):
        probability = random.random()
        # Random chance to mutate the character
        if probability <= PROBABILITY_MUTATION:
            new_individual += random.choice(ALPHABET)
        else:
            new_individual += individual[i]

    return new_individual
    pass

# Swaps the values between individuals
def single_point_crossover(individual1, individual2):
    probability = random.random()
    #for i in range(len(individual1)):
    #    if probability <= PROBABILITY_CROSSOVER:
    #        # Changes individual letters of each individual
    #        individual1_swap = individual1[i]
    #        individual2_swap = individual2[i]
    #        individual2 = individual2[:i] + individual1_swap + individual2[i+1:]
    #        individual1 = individual1[:i] + individual2_swap + individual1[i+1:]

    if probability <= PROBABILITY_CROSSOVER:
        # Swaps partial strings of the individuals
        cross_str = random.randint(1, len(individual1))
        individual1_front = individual1[:cross_str]
        individual2_front = individual2[:cross_str]
        individual1_back = individual1[cross_str:]
        individual2_back = individual2[cross_str:]
        # Final printing of the individuals
        new_individual1 = individual1_front + individual2_back
        new_individual2 = individual2_front + individual1_back
    else:
        new_individual1 = individual1
        new_individual2 = individual2

    return new_individual1, new_individual2
    pass

# Determines the best individual in the entire population
def find_best_individual(population, target):
    max_fitness = -1
    max_individual = ''
    for i in range(int(len(population)/len(target))):
        individual = population[i * len(target):(i * len(target) + len(target))]
        # Calls the fitness function to determine the likeness value
        fitness_val = fitness(target, individual)

        # Determines if the individual is most fit
        if fitness_val > max_fitness:
            max_fitness = fitness_val
            max_individual = individual
    return max_individual
    pass

# Main File... (Boss Music Incoming...)
def main():
    print(BANNER)
    y_n = input(INPUT)
    best_individual = ''
    # Loops as long as the user will input a value
    while y_n.lower() == 'y':
        target = (input(GUESS_INPUT)).lower()


        # Determines if the target is valid
        confirmation = 1
        while confirmation == 1:
            confirmation = 0
            for ch in range(len(target)):
                if target[ch].isalpha() or target[ch] == ' ':
                    continue
                else:
                    print(INCORRECT_INPUT)
                    target = (input(GUESS_INPUT)).lower()
                    confirmation = 1
                    break

        # Calls the make_population function
        population = make_population(target)
        print(GUESS_RESULT)
        generation = 0
        while generation <= NUM_GENERATIONS - 1:
            fitness_call = ''
            if fitness(target, find_best_individual(population, target)) == 1:
                print(EARLY)
                break

            print(GENERATION, generation)
            generation += 1
            new_population = ''

            # Creating the new populations
            while len(new_population) != (NUM_POPULATION * len(target)):
                individual1 = five_tournament_selection(population, target)
                individual2 = five_tournament_selection(population, target)

                mutated_i1 = mutation(individual1)
                mutated_i2 = mutation(individual2)
                new_individual1, new_individual2 = single_point_crossover(mutated_i1, mutated_i2)

                fitness_val_1 = fitness(target, new_individual1)
                fitness_val_2 = fitness(target, new_individual2)

                if fitness_val_1 > fitness_val_2:
                    new_population += new_individual1
                else:
                    new_population += new_individual2
            population = new_population

        best_individual = find_best_individual(population, target)
        print(BEST, best_individual)
        y_n = input('\n' + INPUT)

    print(THANK_YOU)
    pass

# These two lines allow this program to be imported into other codes
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
# DO NOT CHANGE THESE 2 lines or Do NOT add code to them. Everything
# you add should be in the 'main' function above.
if __name__ == '__main__':
    main()


