import heapq

def gbfs(graph, start, goal, heuristic):
    visited = set()
    open_list = [(heuristic[start], start)]
    path = {start: None}

    while open_list:
        print("OPEN LIST:", open_list)
        print("CLOSED LIST:", visited)
        _, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return construct_path(path, start, goal)

        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))
                path[neighbor] = current_node

    return None

def construct_path(path, start, goal):
    current_node = goal
    path_sequence = []

    while current_node:
        path_sequence.insert(0, current_node)
        current_node = path[current_node]

    return path_sequence if path_sequence[0] == start else None

# Example usage for tree
graph = {
    'A': ['S', 'T', 'Z'],
    'S': ['F', 'O', 'R'],
    'F': ['B'],
    'T': [],
    'Z': [],
    'O': [],
    'R': [],
    'B': []
}

start_node = input("Enter the start node: ").strip().upper()
goal_node = input("Enter the goal node: ").strip().upper()

heuristic = {
    'A': 366,
    'S': 253,
    'F': 176,
    'T': 329,
    'O': 380,
    'Z': 374,
    'R': 193,
    'B': 0
}

gbfs_path = gbfs(graph, start_node, goal_node, heuristic)
if gbfs_path:
    print('Path:', gbfs_path)
    print(f"Goal '{goal_node}' found using GBFS.")
else:
    print(f"Goal '{goal_node}' not found using GBFS.")


'''
This code implements the Greedy Best-First Search (GBFS) algorithm to find the shortest path from a start node to a goal node in a graph. Here's the explanation:

1. **Function Definition**: 
   - `def gbfs(graph, start, goal, heuristic):`: This function takes the graph, start node, goal node, and heuristic function as inputs.

2. **Initialization**: 
   - `visited = set()`: Initializes an empty set to store visited nodes.
   - `open_list = [(heuristic[start], start)]`: Initializes a priority queue with a tuple containing the heuristic value and the start node. This queue is sorted based on the heuristic value.
   - `path = {start: None}`: Initializes a dictionary to store the path from the start node to each node.

3. **Main Loop**:
   - `while open_list:`: Continues until the open list is empty.
   - `print("OPEN LIST:", open_list)`: Prints the open list after each iteration.
   - `print("CLOSED LIST:", visited)`: Prints the closed list (visited nodes) after each iteration.
   - `_, current_node = heapq.heappop(open_list)`: Pops the node with the lowest heuristic value from the priority queue.
   - `if current_node == goal:`: Checks if the current node is the goal node. If true, it constructs and returns the path from the start node to the goal node.
   - `visited.add(current_node)`: Adds the current node to the visited set.
   - Iterates over the neighbors of the current node:
     - If the neighbor has not been visited, adds it to the priority queue and updates the path dictionary with the current node as the parent.

4. **Path Construction**: 
   - `def construct_path(path, start, goal):`: This function constructs the path from the start node to the goal node using the path dictionary.

5. **Example Usage**: 
   - Defines the graph and heuristic function.
   - Takes user input for the start and goal nodes.
   - Calls the `gbfs` function with the provided inputs.
   - Prints the resulting path if found, along with a message indicating whether the goal was found or not.

Overall, this code efficiently implements the Greedy Best-First Search algorithm, providing insights into the open and closed lists while finding the optimal path from the start to the goal node.'''