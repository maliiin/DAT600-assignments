from itertools import combinations


def transform_to_dag(edges):
    indexes = list()
    for i in range(len(edges)):
        indexes.append(i)
    combs = generate_combinations(indexes)
    edges_to_remove = set()
    for comb in combs:
        path = list()
        path.append(edges[comb[0]])
        for i in range(1, len(comb)):
            if len(comb) != 1:
                if edges[comb[i]][0] == path[i-1][1]:
                    if edges[comb[i]][1] == path[0][0]:
                        edges_to_remove.add(comb[i])
                        break
                    else:
                        path.append(edges[comb[i]])
                else:
                    break
                    
    dag = [edges[idx] for idx in indexes if idx not in edges_to_remove]
    removed_edges = list()
    for edge in edges_to_remove:
        removed_edges.append(edges[edge])
    return dag, removed_edges

    
def generate_combinations(lst):
    all_combinations = []
    n = len(lst)
    for r in range(1, n+1): 
        for comb in combinations(lst, r):
            all_combinations.append(comb)
    return all_combinations


if __name__ == "__main__":
    # nodes = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}
    edges = [("A", "B"), ("B", "C"), ("B", "D"), ("C", "E"), 
            ("C", "F"), ("D", "E"), ("D", "F"), ("E", "G"), 
            ("E", "F"), ("F", "G"), ("F", "H"), ("H", "I"), 
            ("F", "J"), ("J", "I"), ("F", "B"), ("I", "C"), ("C", "A")]
    dag, removed_edges = transform_to_dag(edges)
    print(f"Edges in dag: {dag}")
    print(f"Edges removed from original graph: {removed_edges}")

