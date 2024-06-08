import heapq
cost=0
def astar(graph, start, goal, heuristic):
    global cost
    visited = set()
    q = [(heuristic[start], 0, start)]  # Priority queue sorted by f-value (heuristic + cost)
    path_cost = {start: 0}
    path = {start: None}

    while q:
        print("OPEN LIST:", q)
        _, current_cost, current_node = heapq.heappop(q)

        if current_node == goal:
            return construct_path(path, start, goal)

        visited.add(current_node)
        print("CLOSED LIST:",visited)
        for n, edge_cost in graph[current_node].items():
            total_cost = path_cost[current_node] + edge_cost
            cost=total_cost
            if n not in visited or total_cost < path_cost[n]:
                path_cost[n] = total_cost
                heapq.heappush(q, (total_cost + heuristic[n], total_cost, n))
                path[n] = current_node

    return None


def construct_path(path, start, goal):
    current_node = goal
    path_sequence = []
    while current_node:
        path_sequence.insert(0, current_node)
        current_node = path[current_node]
    return path_sequence


# Example usage Graph
# graph = {
#     'A': {'B': 1, 'C': 2},
#     'B': {'D': 3, 'E': 4},
#     'C': {'F': 1},
#     'D': {},
#     'E': {},
#     'F': {}
# }

# graph = {
#     'A': {'B': 1, 'C': 2},
#     'B': {'D': 3, 'E': 4},
#     'C': {'F': 1},
#     'D': {},
#     'E': {},
#     'F': {}
# }

graph = {
    'A': {'B': 2, 'E': 3},
    'B': {'C': 1, 'G': 9},
    'C': {},
    'D': {'G':1},
    'E': {'D':6},
    'G': {}
}

start_node = input("Enter the start node: ").upper()
goal_node = input("Enter the goal node: ").upper()

# heuristic = {
#     'A': 3,
#     'B': 2,
#     'C': 4,
#     'D': 1,
#     'E': 1,
#     'F': 0
# }

heuristic = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0
}

astar_path = astar(graph, start_node, goal_node, heuristic)
print()
if astar_path:
    print('Path:', astar_path)
    print(f"Goal '{goal_node}' found using A*.")
else:
    print(f"Goal '{goal_node}' not found using A*.")

print(cost)


'''
This code implements the A* algorithm with an open list, a closed list, and the calculation of the final cost of the path. Let's walk through the code:

1. **Function Definition**: `def astar(graph, start, goal, heuristic):` This function takes the graph, start node, goal node, and heuristic function as inputs.

2. **Initialization**: 
   - `visited = set()`: Initializes an empty set to store visited nodes.
   - `q = [(heuristic[start], 0, start)]`: Initializes a priority queue with a tuple containing the heuristic value, current cost, and start node. This queue is sorted based on the f-value, which is the sum of the heuristic and current cost.
   - `path_cost = {start: 0}`: Initializes a dictionary to store the cost of the path to each node.
   - `path = {start: None}`: Initializes a dictionary to store the path from the start node to each node.

3. **Main Loop**:
   - `while q:`: Continues until the priority queue is empty.
   - `_, current_cost, current_node = heapq.heappop(q)`: Pops the node with the lowest f-value from the priority queue.
   - `if current_node == goal:`: Checks if the current node is the goal node. If true, it constructs and returns the path from the start node to the goal node.
   - `visited.add(current_node)`: Adds the current node to the visited set.
   - `print("CLOSED LIST:",visited)`: Prints the closed list after each iteration.
   - Iterates over the neighbors of the current node:
     - Calculates the total cost of reaching the neighbor.
     - If the neighbor has not been visited or the new cost is lower than the previously recorded cost, updates the path cost and adds the neighbor to the priority queue.
     - Updates the path dictionary with the new cost and current node as the parent.

4. **Path Construction**: `def construct_path(path, start, goal):` This function constructs the path from the start node to the goal node using the path dictionary.

5. **Example Usage**: 
   - Defines the graph and heuristic function.
   - Takes user input for the start and goal nodes.
   - Calls the `astar` function with the provided inputs.
   - Prints the resulting path if found, along with a message indicating whether the goal was found or not.
   - Prints the final cost of the path.

Overall, this code efficiently implements the A* algorithm, providing insights into the open and closed lists while finding the optimal path from the start to the goal node.'''