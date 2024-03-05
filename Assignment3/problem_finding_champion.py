def DFS(graph, start_node):
    """
    This function takes in a graph and a start node and returns a list 
    of all the nodes that can be reached from the start node

    Args: 
        graph (dict): A dictionary where the keys are the nodes and the values 
                      are lists of the nodes that the key node is connected to
        start_node (str): The node to start the search from
    
    Returns: True if all nodes can be reached from the start node, False otherwise
    """
    visited = {}
    for node in graph:
        visited[node] = False
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if not visited[current_node]:
            visited[current_node] = True

        neighbors_of_current_node = graph[current_node]

        # For each neighbor that hasn't been visited, add it to the stack
        for neighbor in neighbors_of_current_node:
            if not visited[neighbor]:
                stack.append(neighbor)
    #all(visited.values())
    return visited


def defeat_each_other(graph):
    nodes_visited = []
    for node in graph:
        values = DFS(graph, node)
        nodes_visited.append([node, values])
    result_list = []
    for item in nodes_visited:
        key, value_dict = item
        filtered_keys = [k for k, v in value_dict.items() if v]
        result_list.append([key, filtered_keys])

    merged_lists = {}
    for node, second_list in result_list:
        if node not in merged_lists:
            merged_lists[node] = set()
        for node2, second_list2 in result_list:
            if node in second_list2 and node2 in second_list:
                merged_lists[node].update([node, node2])

    final_result = [list(merged_set) for merged_set in merged_lists.values()]

    final_list = []  
    for list_node in final_result:
        if list_node not in final_list:
            final_list.append(list_node)
    print(final_list)                                                                          

if __name__ == "__main__":
    graph = {
        "A": ["B", "D"],
        "B": ["A", "C"],
        "C": ["E", "F"],
        "D": ["B", "C"],
        "E": ["G"],
        "F": ["E"],
        "G": ["F"]

    }
    defeat_each_other(graph)