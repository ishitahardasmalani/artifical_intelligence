def dfs(graph, start, goal, visited=None, path=None, open_list=None, closed_list=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if open_list is None:
        open_list = []
    if closed_list is None:
        closed_list = []

    visited.add(start)
    open_list.append(start)
    path = path + [start]

    print("Iteration", len(open_list) + len(closed_list))
    print("Current Node:", start)
    print("Open List:", open_list)
    print("Closed List:", closed_list)

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, visited, path, open_list, closed_list)
            if new_path:
                return new_path

    open_list.remove(start)
    closed_list.append(start)

    return None

#FOR GRAPH
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

#FOR TREE
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

print("DFS Path:")
if start_node not in graph or goal_node not in graph:
    print("Start node or goal node not found in the graph.")
else:
    open_list = []
    closed_list = []
    path = dfs(graph, start_node, goal_node, open_list=open_list, closed_list=closed_list)
    if path:
        print("Path from", start_node, "to", goal_node, ":", ' -> '.join(path))
    else:
        print("Path from", start_node, "to", goal_node, "not found.")
    print("Open List after DFS:", open_list)
    print("Closed List after DFS:", closed_list)


'''
This code implements the Depth-First Search (DFS) algorithm to find a path from a start node to a goal node in a graph. Here's a breakdown of how it works:

1. **Function Definition**: 
   - `def dfs(graph, start, goal, visited=None, path=None, open_list=None, closed_list=None):`: This function takes the graph, start node, goal node, visited set, current path, open list, and closed list as inputs.

2. **Initialization**: 
   - `visited = set()`: Initializes an empty set to store visited nodes.
   - `path = []`: Initializes an empty list to store the current path.
   - `open_list = []`: Initializes an empty list to store nodes that are currently being explored.
   - `closed_list = []`: Initializes an empty list to store nodes that have been explored.

3. **Main Algorithm**:
   - Adds the start node to the visited set, open list, and path.
   - Prints the iteration number, current node, open list, and closed list.
   - Checks if the current node is the goal node. If true, returns the path.
   - Iterates over the neighbors of the current node:
     - If a neighbor has not been visited, recursively calls the `dfs` function with the neighbor as the new start node.
       - If the recursive call returns a path, it returns that path.
   - If no path is found from the current node, removes it from the open list and adds it to the closed list.

4. **Example Usage**: 
   - Defines the graph.
   - Takes user input for the start and goal nodes.
   - Calls the `dfs` function with the provided inputs, passing the open list and closed list.
   - Prints the resulting path if found, along with a message indicating whether the goal was found or not, as well as the open and closed lists after DFS execution.

Overall, this code effectively implements the Depth-First Search algorithm and provides visibility into the process through printed messages displaying the current state of the algorithm.'''