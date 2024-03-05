def find_set(parent, node):
    return parent[node]


def union(parent, a, set_b):
    for element in set_b:
        parent[element] = a


def kruskal_mst(G, e):
    tree = set()
    parent = {}
    total_weight = 0
    # each node is its own parent in the beginning
    for node in G:
        parent[node] = node

    sorted_edges = sorted(e, key=lambda x: x[2])
    for edge in sorted_edges:
        a, b, w = edge

        set_a = find_set(parent, a)
        set_b = find_set(parent, b)

        if b not in set_a:

            total_weight += w
            # add edge to tree
            tree.add(edge)

            # merge set of a and b
            union(parent, set_a, set_b)

        # check if tree is finished
        if len(tree) == len(G) - 1:
            break
    return tree, total_weight


nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
edges = [
    ("A", "B", 5),
    ("A", "D", 1),
    ("B", "D", 4),
    ("B", "H", 8),
    ("C", "D", 2),
    ("C", "G", 6),
    ("D", "E", 2),
    ("D", "F", 4),
    ("E", "H", 8),
    ("F", "G", 9),
    ("F", "H", 7),
]
a, b = kruskal_mst(nodes, edges)
print(a, b)
