from collections import deque

def bfs(graph, start, goal):
    open_list = deque([start])
    closed_list = set()
    visited = {start: None}

    while open_list:
        current_node = open_list.popleft()
        print(f"Current Node: {current_node}")
        print(f"Open List: {list(open_list)}")
        print(f"Closed List: {list(closed_list)}")
        print()

        if current_node == goal:
            return construct_path(visited, goal)

        closed_list.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in closed_list and neighbor not in open_list:
                visited[neighbor] = current_node
                open_list.append(neighbor)

    return None

def construct_path(visited, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = visited[goal]
    return list(reversed(path))

graph = {
    'A': ['B', 'C','D'],
    'B': ['E', 'F'],
    'C': ['G','H'],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
    'H':[]
}

start_node = input("Enter the start node: ").strip().upper()
goal_node = input("Enter the goal node: ").strip().upper()

print("BFS Path:")
if start_node not in graph or goal_node not in graph:
    print("Start node or goal node not found in the graph.")
else:
    path = bfs(graph, start_node, goal_node)
    if path:
        print("Path from", start_node, "to", goal_node, ":", ' -> '.join(path))
    else:
        print("Path from", start_node, "to", goal_node, "not found.")


'''
This code implements the Breadth-First Search (BFS) algorithm to find the shortest path from a start node to a goal node in a graph. Here's a breakdown of how it works:

1. **Function Definition**: 
   - `def bfs(graph, start, goal):`: This function takes the graph, start node, and goal node as inputs.

2. **Initialization**: 
   - `open_list = deque([start])`: Initializes a deque (double-ended queue) with the start node. This queue will store the nodes to be explored.
   - `closed_list = set()`: Initializes an empty set to store visited nodes.
   - `visited = {start: None}`: Initializes a dictionary to store the path from the start node to each visited node.

3. **Main Loop**:
   - `while open_list:`: Continues until the open list is empty.
   - `current_node = open_list.popleft()`: Removes and returns the leftmost node from the deque, representing the current node to explore.
   - Prints the current node, open list, and closed list after each iteration.
   - `if current_node == goal:`: Checks if the current node is the goal node. If true, it constructs and returns the path from the start node to the goal node.
   - `closed_list.add(current_node)`: Adds the current node to the closed list to mark it as visited.
   - Iterates over the neighbors of the current node:
     - If a neighbor is not in the closed list or the open list, it adds it to the open list and updates the visited dictionary with the current node as the parent.

4. **Path Construction**: 
   - `def construct_path(visited, goal):`: This function constructs the path from the start node to the goal node using the visited dictionary.

5. **Example Usage**: 
   - Defines the graph.
   - Takes user input for the start and goal nodes.
   - Calls the `bfs` function with the provided inputs.
   - Prints the resulting path if found, along with a message indicating whether the goal was found or not.

Overall, this code efficiently implements the Breadth-First Search algorithm, providing insights into the open and closed lists while finding the optimal path from the start to the goal node.'''