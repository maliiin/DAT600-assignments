from itertools import combinations

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, from_node, to_node, weight):
        self.add_node(from_node)
        self.add_node(to_node)
        self.adj_list[from_node].append((to_node, weight))

    def find_all_valid_cuts(self, source, sink):
        valid_cuts = []
        nodes = list(self.adj_list.keys())
        for i in range(1, len(nodes)):
            for subset in combinations(nodes, i):
                if source in subset or sink in subset:
                    continue
                source_side = set(subset)
                sink_side = set(nodes) - source_side
                if source in source_side and sink in sink_side:
                    valid_cuts.append((source_side, sink_side))
        return valid_cuts

# Example usage
g = Graph()
nodes = ['s', 't', 'v1', 'v2', 'v3', 'v4', 'v5']
for node in nodes:
    g.add_node(node)

edges = [
    ('s', 'v1', 14),
    ('s', 'v2', 25),
    ('v1', 'v3', 3),
    ('v3', 'v1', 6),
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

source = 's'
sink = 't'
valid_cuts = g.find_all_valid_cuts(source, sink)
print("All valid cuts:")
for source_side, sink_side in valid_cuts:
    print("Source side:", source_side)
    print("Sink side:", sink_side)
    print()
