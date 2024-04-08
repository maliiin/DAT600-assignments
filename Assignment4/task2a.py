# Finds min-cut (bottleneck) by creating the residual graph and augmenting paths
def minimum_cut(graph, source, sink):
    number_of_nodes = len(graph)
    original_graph = [i[:] for i in graph]
    parent = [-1] * number_of_nodes
    maximum_flow = 0
    while BFS(graph, source, sink, parent):
        s = sink
        path_flow = float("Inf")
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        maximum_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[v][u] += path_flow
            graph[u][v] -= path_flow
            v = parent[v]
    visited = [False] * number_of_nodes
    dfs(graph, source, visited)
    min_cut_edges = list()
    for i in range(number_of_nodes):
        for j in range(number_of_nodes):
            if graph[i][j] == 0 and original_graph[i][j] > 0 and visited[i] and not visited[j]:
                min_cut_edges.append((i, j))
                print(f"Edge: {i}, {j}")
    return min_cut_edges


def dfs(graph, source, visited):
    for i in range(len(graph)):
        if graph[source][i] > 0 and not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)


def BFS(graph, source, target, parent):
    number_of_nodes = len(graph)
    visited = [False] * number_of_nodes
    queue = list()
    queue.append(source)
    visited[source] = True
    while queue:
        u = queue.pop(0)
        for i, cap in enumerate(graph[u]):
            if visited[i] == False and cap > 0:
                queue.append(i)
                visited[i] = True
                parent[i] = u
    if visited[target]:
        return True  
    else: 
        return False


# Calculates maximum flow from edges forming the min cut 
def find_max_flow(min_cut_edges, original_graph):
    flow_sum = 0
    for edges in min_cut_edges:
        flow_sum += original_graph[edges[0]][edges[1]]
    return flow_sum

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

    graph_deepcopy= [i[:] for i in graph_adjacency_matrix]

    min_cut_edges = minimum_cut(graph_adjacency_matrix, source=0, sink=6)
    maximum_flow = find_max_flow(min_cut_edges, graph_deepcopy)
    print(f"Maximum flow: {maximum_flow}")