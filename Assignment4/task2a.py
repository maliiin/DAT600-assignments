from collections import deque

# Finds min-cut (bottleneck) by creating the residual graph and augmenting paths
def minimum_cut(graph, source, sink):
    number_of_nodes = len(graph)
    original_graph = [list(row) for row in graph]
    predecessor = [-1] * number_of_nodes
    max_flow = 0
    while bfs(graph, source, sink, predecessor):
        path_flow = float("inf")
        s = sink
        path = []
        while s != source:
            path.append(s)
            s = predecessor[s]
        path.append(source)
        path.reverse()
        for i in range(len(path) - 1):
            path_flow = min(path_flow, graph[path[i]][path[i+1]])
        max_flow += path_flow
        for i in range(len(path) - 1):
            graph[path[i]][path[i+1]] -= path_flow
            graph[path[i+1]][path[i]] += path_flow
    explored = [False] * number_of_nodes
    dfs(graph, source, explored)
    min_cut_edges = [(i, j) for i in range(number_of_nodes) for j in range(number_of_nodes)
                     if graph[i][j] == 0 and original_graph[i][j] > 0 and explored[i] and not explored[j]]
    for i, j in min_cut_edges:
        print(f"Edge: {i}, {j}")
    return min_cut_edges


def bfs(graph, source, target, predecessor):
    explored = [False] * len(graph)
    search_queue = deque([source])
    explored[source] = True
    while search_queue:
        u = search_queue.popleft()
        for v, capacity in enumerate(graph[u]):
            if not explored[v] and capacity > 0:
                search_queue.append(v)
                explored[v] = True
                predecessor[v] = u
    return explored[target]

def dfs(graph, source, explored):
    explored[source] = True
    stack = [source]
    while stack:
        u = stack.pop()
        for v, capacity in enumerate(graph[u]):
            if capacity > 0 and not explored[v]:
                stack.append(v)
                explored[v] = True


# Calculates maximum flow from edges forming the min cut 
def find_max_flow(min_cut_edges, original_graph):
    return sum(original_graph[i][j] for i, j in min_cut_edges)

if __name__ == "__main__":
    # The graph represented as a adjacency matrix
    graph_adjacency_matrix = [
        [0, 14, 25, 0, 0, 0, 0],
        [0, 0, 0, 0, 21, 0, 0],
        [0, 0, 0, 13, 0, 7, 0],
        [0, 6, 0, 0, 0, 15, 0],
        [0, 0, 0, 10, 0, 0, 20],
        [0, 0, 0, 0, 5, 0, 10],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    graph_deepcopy = [list(row) for row in graph_adjacency_matrix]

    min_cut_edges = minimum_cut(graph_adjacency_matrix, source=0, sink=6)
    maximum_flow = find_max_flow(min_cut_edges, graph_deepcopy)
    print(f"Maximum flow: {maximum_flow}")

    # Inspiration from the approach here: https://www.geeksforgeeks.org/minimum-cut-in-a-directed-graph/
