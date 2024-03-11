from itertools import combinations


def transform_to_dag(nodes, edges):
    indexes = list()
    for i in range(len(edges)):
        indexes.append(i)
    combs = generate_combinations(indexes)
    edges_to_remove = set()
    for comb in combs:
        path = list()
        path.append(edges[comb[0]])
        for i in range(1, len(comb)):
            if comb == (2, 6, 14):
                print("hei")
            if len(comb) != 1:
                if edges[comb[i]][0] == path[i-1][1]:
                    if edges[comb[i]][1] == path[0][0]:
                        edges_to_remove.add(comb[i])
                        break
                    else:
                        path.append(edges[comb[i]])
                else:
                    break

                # start_idx = comb[i%len(comb)]
                # end_idx = comb[(i+1)%len(comb)]
                # if edges[comb[i%len(comb)]][1] == edges[comb[(i+1)%len(comb)]][0]:
                #     start = edges[comb[(i+1)%len(comb)]]
                #     end = edges[comb[i%len(comb)]]
                #     if edges[comb[(i+1)%len(comb)]][1] == edges[comb[i%len(comb)]][0]:
                #         edges_to_remove.add((comb[i]%len(comb)))
                    
    dag = [edges[idx] for idx in indexes if idx not in edges_to_remove]
    for edge in edges_to_remove:
        print(edges[edge])
    return dag

    
def generate_combinations(lst):
    all_combinations = []
    n = len(lst)
    for r in range(1, n+1): 
        for comb in combinations(lst, r):
            all_combinations.append(comb)
    return all_combinations


if __name__ == "__main__":
    nodes = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}
    edges = [("A", "B"), ("B", "C"), ("B", "D"), ("C", "E"), 
            ("C", "F"), ("D", "E"), ("D", "F"), ("E", "G"), 
            ("E", "F"), ("F", "G"), ("F", "H"), ("H", "I"), 
            ("F", "J"), ("J", "I"), ("F", "B"), ("I", "C"), ("C", "A")]
    new_edges = transform_to_dag(nodes, edges)
    print(len(edges))
    print(len(new_edges))
    print(edges)
    print(new_edges)
    new_edges2 = transform_to_dag(nodes, new_edges)
    print(len(new_edges2))

