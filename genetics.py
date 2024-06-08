import random

def genetic_algorithm(population_size, mutation_rate, crossover_rate, num_variables):
    # Generate initial population
    initial_population = [[random.randint(0, 10) for _ in range(num_variables)] for _ in range(population_size)]
    print("Initial Population:")
    for chromosome in initial_population:
        print(chromosome)

    # Loop until optimal solution found (fitness of 0)
    population = initial_population
    while True:
        fitness_values = [fitness(chromosome) for chromosome in population]
        best_chromosome = population[fitness_values.index(min(fitness_values))]
        if min(fitness_values) == 0:
            print("\nFinal Population:")
            for chromosome in population:
                print(chromosome)
            return best_chromosome

        # Selection (replace with a simpler method if needed)
        selected_population = random.choices(population, fitness_values, k=population_size)

        # Crossover (replace with a basic mechanism if needed)
        next_generation = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.sample(selected_population, 2)
            child1, child2 = crossover(parent1, parent2, crossover_rate)
            next_generation.extend([child1, child2])

        # Mutation
        for individual in next_generation:
            mutation(individual, mutation_rate)

        population = next_generation

def fitness(variables):
    a, b, c, d = variables
    return abs((a + 2 * b + 3 * c + 4 * d) - 30)

# Simplified crossover (can be replaced with random selection)
def crossover(parent1, parent2, crossover_rate):
    if random.random() < crossover_rate:
        crossover_point = random.randint(1, len(parent1) - 1)
        return parent1[:crossover_point] + parent2[crossover_point:], parent2[:crossover_point] + parent1[crossover_point:]
    return parent1, parent2

# Simplified mutation (can be replaced with random value assignment)
def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.randint(0, 10)

def main():
    population_size = 6
    mutation_rate = 0.1
    crossover_rate = 0.7
    num_variables = 4
    best_chromosome = genetic_algorithm(population_size, mutation_rate, crossover_rate, num_variables)
    print("\nBest solution:", best_chromosome)

main()


'''
Sure, let's go through the code line by line:

1. `import random`: This imports the `random` module, which is used for generating random numbers and making random choices.

2. `def genetic_algorithm(population_size, mutation_rate, crossover_rate, num_variables):`: This defines the `genetic_algorithm` function, which takes four parameters: `population_size`, `mutation_rate`, `crossover_rate`, and `num_variables`. This function implements a genetic algorithm to find the optimal solution to a problem.

3. `initial_population = [[random.randint(0, 10) for _ in range(num_variables)] for _ in range(population_size)]`: This line generates the initial population of chromosomes. It creates a list of lists, where each inner list represents a chromosome, and each element within the inner list represents a gene. The value of each gene is a random integer between 0 and 10. This process is repeated `population_size` times.

4. `print("Initial Population:")`: This line prints a message indicating that the following output will display the initial population.

5. `for chromosome in initial_population:`: This loop iterates over each chromosome in the initial population.

6. `print(chromosome)`: This line prints each chromosome.

7. `population = initial_population`: This line initializes the current population to be the initial population.

8. `while True:`: This starts an infinite loop that will continue until a stopping condition is met (in this case, when the optimal solution is found).

9. `fitness_values = [fitness(chromosome) for chromosome in population]`: This line calculates the fitness value for each chromosome in the population using the `fitness` function.

10. `best_chromosome = population[fitness_values.index(min(fitness_values))]`: This line finds the chromosome with the minimum fitness value, which represents the best solution found so far.

11. `if min(fitness_values) == 0:`: This condition checks if the minimum fitness value is 0, indicating that an optimal solution has been found.

12. `print("\nFinal Population:")`: This line prints a message indicating that the following output will display the final population.

13. `for chromosome in population:`: This loop iterates over each chromosome in the population.

14. `print(chromosome)`: This line prints each chromosome in the final population.

15. `return best_chromosome`: This line returns the best chromosome found, which represents the optimal solution to the problem.

16. `selected_population = random.choices(population, fitness_values, k=population_size)`: This line selects a new population by randomly choosing chromosomes from the current population, with the probability of selection proportional to their fitness values.

17. `next_generation = []`: This line initializes an empty list to store the offspring generated by crossover.

18. `for _ in range(population_size // 2):`: This loop iterates over half of the population size, as two parents are required to produce two offspring.

19. `parent1, parent2 = random.sample(selected_population, 2)`: This line randomly selects two parents from the selected population without replacement.

20. `child1, child2 = crossover(parent1, parent2, crossover_rate)`: This line performs crossover between the two parents to produce two offspring.

21. `next_generation.extend([child1, child2])`: This line adds the two offspring to the next generation.

22. `for individual in next_generation:`: This loop iterates over each individual in the next generation.

23. `mutation(individual, mutation_rate)`: This line applies mutation to each individual in the next generation with a certain probability defined by the mutation rate.

24. `population = next_generation`: This line updates the current population to be the next generation.

25. `def main():`: This defines the `main` function, which serves as the entry point of the program.

26. `population_size = 6`, `mutation_rate = 0.1`, `crossover_rate = 0.7`, `num_variables = 4`: These lines define the parameters for the genetic algorithm, including the population size, mutation rate, crossover rate, and number of variables.

27. `best_chromosome = genetic_algorithm(population_size, mutation_rate, crossover_rate, num_variables)`: This line calls the `genetic_algorithm` function with the specified parameters to find the best solution.

28. `print("\nBest solution:", best_chromosome)`: This line prints the best solution found by the genetic algorithm.

29. `main()`: This line calls the `main` function to start the program.'''