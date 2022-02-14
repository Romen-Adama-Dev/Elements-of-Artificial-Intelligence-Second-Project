# Romen Adama Caetano Ramirez Sun 6 Feb - 2022

"""
Implementing Depth First Search (DFS) algorithm
Consider the graph below and note the expected orders of traversal for this graph using
DFS.
Using recursions we will split the problem into smaller instances, and the same method is called recursively within its body.
If the node has been visited, we have to backtrack.

As explained in the PDF, the order is: A-1, B-2, E-3, I-4, C-5, F-6, J-7, G-8, D-9, H-10
"""

# DFS - non recursive method
"""
DFS - a non-recursive approach
Implement a method in Python that accepts a graph and traverses through it using DFS.
"""
graph_non = {"A": ["D", "C", "B"],
             "B": ["E"],
             "C": ["G", "F"],
             "D": ["H"],
             "E": ["I"],
             "F": ["J"]}


def dfs_non_recursive(graph_non, source_non):
    if source_non is None or source_non not in graph_non:
        return "Invalid input"
    path_non = []
    stack_non = [source_non]
    while (len(stack_non) != 0):
        s = stack_non.pop()
        if s not in path_non:
            path_non.append(s)
        if s not in graph_non:
            # leaf node
            continue
        for neighbor in graph_non[s]:
            stack_non.append(neighbor)
    return " ".join(path_non)

DFS_path_non = dfs_non_recursive(graph_non, "A")
print("This is the non recursive model")
print(DFS_path_non)



# DFS - a recursive method
"""
DFS - a recursive method
Implement the Depth First Search algorithm using a popular problem-solving approach
called recursion.
"""
graph = {"A": ["B", "C", "D"],
         "B": ["E"],
         "C": ["F", "G"],
         "D": ["H"],
         "E": ["I"],
         "F": ["J"]}

def dfs(graph, source, path=[]):
    if source not in path:
        path.append(source)
        if source not in graph:
            # leaf node, backtrack
            return path
        for neighbour in graph[source]:
            path = dfs(graph, neighbour, path)
    return path

path = dfs(graph, "A")
print("This is the recursive model")
print(" ".join(path))

# BFS
"""
***For Bonus points: Implement Breath First Search (BFS) algorithm.
                  a
               /  |  \
              b   c   d
             /   / \   \
            e   f   g   h
           /    |
          i     j     
"""
graph_BFS = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J'],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

visited = []  # List to keep track of visited nodes.
# #Initialize a queue
q = []

def bfs(visited, graph_BFS, node):
    visited.append(node)
    q.append(node)

    print("This is the the Breath First Search algorithm")

    while q:
        s = q.pop(0)
        print(s, end=" ")
        for n in graph_BFS[s]:
            if n not in visited:
                visited.append(n)
                q.append(n)

bfs(visited, graph_BFS, 'A')