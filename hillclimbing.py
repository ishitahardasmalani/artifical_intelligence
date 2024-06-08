#f(x) = -x**2
import random

# Define the objective function
def objective_function(x):
    return -x ** 2

# Generate initial solution
def generate_initial_solution():
    return random.randint(-100, 100)

# Generate neighbour solutions
def generate_neighbours(solution):
    neighbours = []
    for delta in [-1, 1]:
        neighbours.append(solution + delta)
    return neighbours

# Find the best neighbour
def get_best_neighbour(neighbours):
    best_neighbour = neighbours[0]
    best_quality = objective_function(best_neighbour)
    for neighbour in neighbours[1:]:
        neighbour_quality = objective_function(neighbour)
        if neighbour_quality > best_quality:
            best_quality = neighbour_quality
            best_neighbour = neighbour
    return best_neighbour

# Hill climbing algorithm
def hill_climbing():
    current_solution = generate_initial_solution()
    while True:
        neighbours = generate_neighbours(current_solution)
        best_neighbour = get_best_neighbour(neighbours)
        if objective_function(best_neighbour) <= objective_function(current_solution):
            return current_solution
        current_solution = best_neighbour

# Main function
def main():
    best_solution = hill_climbing()
    print("Best solution found:", best_solution)
    print("Objective function value:", objective_function(best_solution))

# Run the main function
if __name__ == "__main__":
    main()

'''
This code implements the Hill Climbing algorithm to find the maximum value of the objective function \( f(x) = -x^2 \).

Let's go through the code line by line:

1. `def objective_function(x):`: Defines the objective function \( f(x) = -x^2 \). It takes a value `x` as input and returns the negative square of `x`.

2. `def generate_initial_solution():`: Generates an initial solution by selecting a random integer between -100 and 100.

3. `def generate_neighbours(solution):`: Generates neighboring solutions of a given solution. It returns a list containing the solution itself and its immediate neighbors obtained by adding and subtracting 1.

4. `def get_best_neighbour(neighbours):`: Finds the best neighbor among a list of neighbors based on their objective function values. It returns the neighbor with the highest objective function value.

5. `def hill_climbing():`: Implements the Hill Climbing algorithm. It starts from an initial solution, iteratively generates neighboring solutions, selects the best neighbor, and moves to that neighbor if it has a higher objective function value than the current solution. It continues this process until it reaches a peak where no neighbor has a higher objective function value.

6. `def main():`: Defines the main function. It runs the Hill Climbing algorithm and prints the best solution found along with its objective function value.

7. `if __name__ == "__main__":`: This block ensures that the `main()` function is executed only if the script is run directly, not if it's imported as a module into another script.

8. `main()`: Calls the `main()` function to start the execution of the program.

The Hill Climbing algorithm implemented in this code aims to find the maximum value of the given objective function \( f(x) = -x^2 \) by iteratively moving towards higher values of \( x \). 
'''

# f(x) = sinx
# import random
# import math

# # Define the objective function
# def objective_function(x):
#     return math.sin(x)

# # Generate initial solution
# def generate_initial_solution():
#     return random.uniform(-math.pi, math.pi)

# # Generate neighbour solutions
# def generate_neighbours(solution):
#     neighbours = []
#     for delta in [-0.1, 0.1]:
#         neighbours.append(solution + delta)
#     return neighbours

# # Find the best neighbour
# def get_best_neighbour(neighbours):
#     best_neighbour = neighbours[0]
#     best_quality = objective_function(best_neighbour)
#     for neighbour in neighbours[1:]:
#         neighbour_quality = objective_function(neighbour)
#         if neighbour_quality > best_quality:
#             best_quality = neighbour_quality
#             best_neighbour = neighbour
#     return best_neighbour

# # Hill climbing algorithm
# def hill_climbing():
#     current_solution = generate_initial_solution()
#     while True:
#         neighbours = generate_neighbours(current_solution)
#         best_neighbour = get_best_neighbour(neighbours)
#         if objective_function(best_neighbour) <= objective_function(current_solution):
#             return current_solution
#         current_solution = best_neighbour

# # Main function
# def main():
#     best_solution = hill_climbing()
#     print("Best solution found:", best_solution)
#     print("Objective function value:", objective_function(best_solution))

# # Run the main function
# if __name__ == "__main__":
#     main()


# f(x) = -5x2+3x+6
# import random

# # Define the objective function
# def objective_function(x):
#     return -(5 * x ** 2 + 3 * x + 6)

# # Generate initial solution
# def generate_initial_solution():
#     return random.uniform(-100, 100)

# # Generate neighbour solutions
# def generate_neighbours(solution):
#     neighbours = []
#     for delta in [-0.1, 0.1]:
#         neighbours.append(solution + delta)
#     return neighbours

# # Find the best neighbour
# def get_best_neighbour(neighbours):
#     best_neighbour = neighbours[0]
#     best_quality = objective_function(best_neighbour)
#     for neighbour in neighbours[1:]:
#         neighbour_quality = objective_function(neighbour)
#         if neighbour_quality > best_quality:
#             best_quality = neighbour_quality
#             best_neighbour = neighbour
#     return best_neighbour

# # Hill climbing algorithm
# def hill_climbing():
#     current_solution = generate_initial_solution()
#     while True:
#         neighbours = generate_neighbours(current_solution)
#         best_neighbour = get_best_neighbour(neighbours)
#         if objective_function(best_neighbour) <= objective_function(current_solution):
#             return current_solution
#         current_solution = best_neighbour

# # Main function
# def main():
#     best_solution = hill_climbing()
#     print("Best solution found:", best_solution)
#     print("Objective function value:", objective_function(best_solution))

# # Run the main function
# if __name__ == "__main__":
#     main()
