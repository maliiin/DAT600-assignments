def graph_to_adjacent_list(nodes, edges):
    adjacent_list = dict()
    for node in nodes:
         adjacent_list[node] = list()
    for edge in edges:
            adjacent_list[edge[0]].append(edge[1])
    return adjacent_list


if __name__ == "__main__":
    nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    edges = [("A", "B"), ("B", "C"), ("B", "D"), ("C", "E"), 
            ("C", "F"), ("D", "E"), ("D", "F"), ("E", "G"), 
            ("E", "F"), ("F", "G"), ("F", "H"), ("H", "I"), 
            ("F", "J"), ("J", "I"), ("F", "B")]
    adjacent_list = graph_to_adjacent_list(nodes, edges)
    for node, adjacent_nodes in adjacent_list.items():
        print(f"Node: {node}, Adjacent nodes: {adjacent_nodes}")