import random

# Create a dictionary to represent the graph where the keys are the vertices and the values are the edges
graph = {1: [2,3, 7], 2: [1,4,5], 3: [1,6], 4: [2], 5: [2], 6: [3, 7], 7: [1, 6]}

# Create a function to perform BFS
def bfs(graph, start_vertex):
    # Create a queue to hold the vertices to visit
    queue = [start_vertex]
    # Create a set to keep track of visited vertices
    visited = set()
    # While there are still vertices to visit
    while queue:
        # Dequeue a vertex from the queue
        current_vertex = queue.pop(0)
        # If the vertex has not been visited
        if current_vertex not in visited:
            # Mark it as visited
            visited.add(current_vertex)
            # Add its edges to the queue
            for neighbor in graph[current_vertex]:
                queue.append(neighbor)
    # Return the set of visited vertices
    return visited

# Select a random start vertex
start_vertex = random.choice(list(graph.keys()))
# Perform BFS
visited = bfs(graph, start_vertex)
print(visited)
