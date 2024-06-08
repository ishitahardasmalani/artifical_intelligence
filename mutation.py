import random

def binaryConversion(chromosome):
    return bin(chromosome)[2:].zfill(5)

def mutation(chromosome):
    mutationPoint = random.randint(0, 4)
    mutatedBit = 1 << mutationPoint
    mutatedChromosome = chromosome ^ mutatedBit

    return mutatedChromosome

def main():
    population = [random.randint(0, 15) for _ in range(6)]
    mutationRate = 0.1

    print("Before Mutation: ")
    for chromosome in population:
        print(f"{chromosome}: {binaryConversion(chromosome)}")

    for i in range(len(population)):
        if random.random() < mutationRate:
            population[i] = mutation(population[i])

    print("After Mutation: ")
    for chromosome in population:
        print(f"{chromosome}: {binaryConversion(chromosome)}")


if __name__ == '__main__':
    main()



'''
Sure, let's go through the code line by line:

1. `import random`: This imports the `random` module, which provides functions for generating random numbers and other random operations.

2. `def binaryConversion(chromosome):`: This defines a function named `binaryConversion` that takes a `chromosome` as input.

3. `return bin(chromosome)[2:].zfill(5)`: This line converts the integer `chromosome` into its binary representation, strips the leading `'0b'` characters, and then left-pads it with zeros to make it 5 digits long. The resulting binary string is returned.

4. `def mutation(chromosome):`: This defines a function named `mutation` that takes a `chromosome` as input.

5. `mutationPoint = random.randint(0, 4)`: This line generates a random integer between 0 and 4 (inclusive) to determine the position of the bit to mutate.

6. `mutatedBit = 1 << mutationPoint`: This line creates a mutated bit by left-shifting the number 1 by `mutationPoint` positions.

7. `mutatedChromosome = chromosome ^ mutatedBit`: This line performs bitwise XOR operation between the `chromosome` and the `mutatedBit` to flip the bit at the randomly chosen position.

8. `return mutatedChromosome`: This returns the mutated chromosome after applying the mutation operation.

9. `def main():`: This defines the main function of the program.

10. `population = [random.randint(0, 15) for _ in range(6)]`: This line creates a list named `population` containing 6 random integers between 0 and 15 (inclusive).

11. `mutationRate = 0.5`: This sets the mutation rate to 0.5, which means there's a 50% chance that each chromosome will undergo mutation.

12. `print("Before Mutation: ")`: This line prints a message indicating that the output will display the population before mutation.

13. `for chromosome in population:`: This initiates a loop over each `chromosome` in the `population`.

14. `print(f"{chromosome}: {binaryConversion(chromosome)}")`: This line prints each `chromosome` along with its binary representation using the `binaryConversion` function.

15. `for i in range(len(population)):`: This initiates a loop over the indices of the `population`.

16. `if random.random() < mutationRate:`: This checks if a randomly generated probability (between 0 and 1) is less than the mutation rate.

17. `population[i] = mutation(population[i])`: If the condition is met, it applies the `mutation` function to the chromosome at index `i` in the population.

18. `print("After Mutation: ")`: This line prints a message indicating that the output will display the population after mutation.

19. `for chromosome in population:`: This initiates a loop over each `chromosome` in the `population`.

20. `print(f"{chromosome}: {binaryConversion(chromosome)}")`: This line prints each `chromosome` along with its binary representation after mutation.

This code demonstrates a simple genetic algorithm for mutating a population of binary-encoded chromosomes.'''