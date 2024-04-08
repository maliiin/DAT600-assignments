from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, from_node, to_node, weight):
        self.adj_list[from_node].append((to_node, weight))

    def get_neighbors(self, node):
        return self.adj_list.get(node, [])


def bfs(graph, start_node, sink_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        visited.add(current_node)  # Mark the current node as visited
        if current_node == sink_node:
            break  # Stop BFS traversal if we reach the sink node
        for neighbor, _ in graph.get_neighbors(current_node):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)  # Add unvisited neighbors to the queue
    return visited


# Create a graph
g = Graph()

# Add edges
edges = [
    ('s', 'v1', 14),
    ('s', 'v2', 25),
    ('v1', 'v3', 3),
    ('v3', 'v1', 6),
    ('v1', 'v4', 21),  # Added missing edge
    ('v4', 'v3', 10),
    ('v2', 'v3', 13),
    ('v2', 'v5', 7),
    ('v3', 'v5', 15),
    ('v5', 'v4', 5),
    ('v5', 't', 10),
    ('v4', 't', 20)
]

for edge in edges:
    g.add_edge(*edge)

# Find a valid cut
source_side = bfs(g, 's', 't')
sink_side = set(g.adj_list.keys()) - source_side

print("Source side of the cut:", source_side)
print("Sink side of the cut:", sink_side)
