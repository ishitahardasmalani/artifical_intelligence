import random

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def binaryConversion(chromosome):
    return bin(chromosome)[2:].zfill(5)

def crossover(population, crossoverRate):
    offspring = []

    for i in range(0, len(population), 2):
        parent1 = population[i]
        parent2 = population[i + 1]

        if random.random() < crossoverRate * 100:
            crossoverPoint = random.randint(1, len(parent1) - 1)
            child1 = parent1[:crossoverPoint] + parent2[crossoverPoint:]
            child2 = parent2[:crossoverPoint] + parent1[crossoverPoint:]

            offspring.extend([child1, child2])                                              # Using list concatenation instead of extend
                                                                                            #      offspring = offspring + [child1, child2]
                                                                                            # else:
                                                                                            #     # Using list concatenation instead of extend
                                                                                            #     offspring = offspring + [parent1, parent2]
        else:
            offspring.extend([parent1, parent2])

    return offspring


pop = ['13', '10', '7', '9', '5','16']
population = [bin(int(decimal))[2:].zfill(4) for decimal in pop]
print(population)

crossoverRate = 0.25

print("Initial Population: ")
for ind, binary in enumerate(population):
    print(f"Binary: {binary}, Decimal: {binary_to_decimal(binary)}")

offspringPopulation = crossover(population, crossoverRate)

print("\nOffspring Population after crossover: ")
for ind, binary in enumerate(offspringPopulation):
    print(f"Binary: {binary}, Decimal: {binary_to_decimal(binary)}")


'''
Sure, let's break down the code line by line:

1. `import random`: This imports the `random` module, which provides functions for generating random numbers and other random operations.

2. `def binary_to_decimal(binary_str):`: This defines a function named `binary_to_decimal` that takes a binary string `binary_str` as input.

3. `return int(binary_str, 2)`: This line converts the binary string `binary_str` to its corresponding decimal integer using the `int()` function with base 2.

4. `def binaryConversion(chromosome):`: This defines a function named `binaryConversion` that converts an integer chromosome to its binary representation.

5. `return bin(chromosome)[2:].zfill(5)`: This line converts the integer `chromosome` into its binary representation, strips the leading `'0b'` characters, and then left-pads it with zeros to make it 5 digits long. The resulting binary string is returned.

6. `def crossover(population, crossoverRate):`: This function performs crossover operation on the given population.

7. `offspring = []`: This initializes an empty list to store the offspring generated through crossover.

8. `for i in range(0, len(population), 2):`: This loop iterates over the population by pairs, considering two parents at a time for crossover.

9. `parent1 = population[i]`: This selects the first parent from the population.

10. `parent2 = population[i + 1]`: This selects the second parent from the population.

11. `if random.random() < crossoverRate * 100:`: This condition checks if a random number between 0 and 1 is less than the crossover rate multiplied by 100 (to convert it to a percentage).

12. `crossoverPoint = random.randint(1, len(parent1) - 1)`: This randomly selects a crossover point between 1 and the length of the parent chromosome minus 1.

13. `child1 = parent1[:crossoverPoint] + parent2[crossoverPoint:]`: This line performs crossover by combining the first part of `parent1` with the second part of `parent2` to create `child1`.

14. `child2 = parent2[:crossoverPoint] + parent1[crossoverPoint:]`: This line performs crossover by combining the first part of `parent2` with the second part of `parent1` to create `child2`.

15. `offspring.extend([child1, child2])`: This appends the offspring `child1` and `child2` to the list `offspring`.

16. `else:`: If the condition in line 11 is not met (i.e., crossover does not occur), the else block executes.

17. `offspring.extend([parent1, parent2])`: In this case, the original parents `parent1` and `parent2` are added to the offspring without crossover.

18. `return offspring`: This returns the list of offspring generated through crossover.

19. `pop = ['13', '10', '7', '9', '5','16']`: This initializes a list `pop` containing string representations of decimal integers.

20. `population = [bin(int(decimal))[2:].zfill(4) for decimal in pop]`: This line converts each decimal integer in the list `pop` to its binary representation and pads it with zeros to make it 4 digits long.

21. `print(population)`: This prints the initial population of binary-encoded chromosomes.

22. `crossoverRate = 0.25`: This sets the crossover rate to 0.25, indicating that there's a 25% chance of crossover occurring between any pair of parents.

23. `print("Initial Population: ")`: This prints a message indicating that the output will display the initial population.

24. `for ind, binary in enumerate(population):`: This loop iterates over each binary chromosome in the population along with its index.

25. `print(f"Binary: {binary}, Decimal: {binary_to_decimal(binary)}")`: This line prints each binary chromosome along with its corresponding decimal representation.

26. `offspringPopulation = crossover(population, crossoverRate)`: This line invokes the `crossover` function to generate offspring from the initial population based on the specified crossover rate.

27. `print("\nOffspring Population after crossover: ")`: This prints a message indicating that the output will display the offspring population after crossover.

28. `for ind, binary in enumerate(offspringPopulation):`: This loop iterates over each binary chromosome in the offspring population along with its index.

29. `print(f"Binary: {binary}, Decimal: {binary_to_decimal(binary)}")`: This line prints each binary chromosome in the offspring population along with its corresponding decimal representation.

This code demonstrates a simple crossover operation in a genetic algorithm applied to a population of binary-encoded chromosomes.'''