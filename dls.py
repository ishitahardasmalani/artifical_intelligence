def dls(graph, start, goal, max_depth, depth=0, visited=None, path=None, open_list=None, closed_list=None):
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

    print("Iteration", depth)
    print("Current Node:", start)
    print("Open List:", open_list)
    print("Closed List:", closed_list)
    print()

    if start == goal:
        return path

    if depth >= max_depth:
        open_list.remove(start)
        closed_list.append(start)
        return None

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dls(graph, neighbor, goal, max_depth, depth + 1, visited, path, open_list, closed_list)
            if new_path:
                return new_path

    open_list.remove(start)
    closed_list.append(start)

    return None

# Example graph represented as an adjacency list
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
max_depth = int(input("Enter the maximum depth: ").strip())

print("DLS Path:")
if start_node not in graph or goal_node not in graph:
    print("Start node or goal node not found in the graph.")
else:
    open_list = []
    closed_list = []
    path = dls(graph, start_node, goal_node, max_depth, open_list=open_list, closed_list=closed_list)
    if path:
        print("Path from", start_node, "to", goal_node, ":", ' -> '.join(path))
    else:
        print("Path from", start_node, "to", goal_node, "not found within the maximum depth.")
    print("Open List after DLS:", open_list)
    print("Closed List after DLS:", closed_list)


'''
Certainly! Let's break down the code step by step:

1. **Function Definition**: 
    ```python
    def dls(graph, start, goal, max_depth, depth=0, visited=None, path=None, open_list=None, closed_list=None):
    ```

    - This defines a function named `dls` which stands for Depth-Limited Search.
    - It takes several parameters:
        - `graph`: The graph or tree on which the search is performed.
        - `start`: The starting node of the search.
        - `goal`: The goal node that the search aims to reach.
        - `max_depth`: The maximum depth until which the search is allowed to explore.
        - `depth`: (Optional) The current depth of the search (default is 0).
        - `visited`: (Optional) A set to track visited nodes (default is an empty set).
        - `path`: (Optional) A list representing the current path being explored (default is an empty list).
        - `open_list`: (Optional) A list to track nodes that are currently open for exploration (default is an empty list).
        - `closed_list`: (Optional) A list to track nodes that have been explored and closed (default is an empty list).

2. **Initialization**: 
    ```python
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if open_list is None:
        open_list = []
    if closed_list is None:
        closed_list = []
    ```
   
    - These lines initialize the optional parameters if they are not provided when calling the function. 
    - `visited` is initialized as an empty set, `path` as an empty list, and both `open_list` and `closed_list` as empty lists.

3. **Node Handling**:
    ```python
    visited.add(start)
    open_list.append(start)
    path = path + [start]
    ```
   
    - The function starts by adding the `start` node to the `visited` set, `open_list`, and `path`. 
    - This node is marked as visited, added to the open list, and appended to the current path being explored.

4. **Printing Current State**:
    ```python
    print("Iteration", depth)
    print("Current Node:", start)
    print("Open List:", open_list)
    print("Closed List:", closed_list)
    print()
    ```

    - This section prints the current iteration number, the current node being explored, the open list, and the closed list. 
    - It provides a visual representation of the search process.

5. **Goal Check**:
    ```python
    if start == goal:
        return path
    ```

    - If the current node being explored is the goal node, the function returns the path that led to reaching the goal.

6. **Depth Check**:
    ```python
    if depth >= max_depth:
        open_list.remove(start)
        closed_list.append(start)
        return None
    ```

    - If the maximum depth has been reached without finding the goal node, the function removes the current node from the open list, adds it to the closed list, and returns `None`.

7. **Recursive Exploration**:
    ```python
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dls(graph, neighbor, goal, max_depth, depth + 1, visited, path, open_list, closed_list)
            if new_path:
                return new_path
    ```

    - This loop iterates over the neighbors of the current node.
    - If a neighbor has not been visited, the function is called recursively with the neighbor node.
    - The depth is incremented, and the visited, path, open list, and closed list are updated accordingly.
    - If a path to the goal is found through this neighbor, it is returned.
  
8. **Final Steps**:
    ```python
    open_list.remove(start)
    closed_list.append(start)
    return None
    ```

    - After exploring all neighbors, if the function reaches this point, it removes the current node from the open list, adds it to the closed list, and returns `None`, indicating that no path to the goal was found from this node.

This function conducts a Depth-Limited Search (DLS) on a graph or tree, keeping track of visited nodes, the current path, and the open and closed lists for each iteration. It explores nodes up to a specified maximum depth.'''