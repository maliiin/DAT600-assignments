def adjadency_matrix_to_list(adjacency_matrix):
    adjacency_list = dict()
    matrix_size = len(adjacency_matrix[0])
    for node1 in range(1, matrix_size + 1):
        for node2 in range(1, matrix_size + 1):
            if adjacency_matrix[node1-1][node2-1] == 1:
                if node1 not in adjacency_list:
                    adjacency_list[node1] = [node2]
                else:
                    adjacency_list[node1].append(node2)
    return adjacency_list



if __name__ == "__main__":
    adjacency_matrix =   [[0 , 1 , 0 , 0 , 0 , 0] ,
            [0 , 1 , 1 , 1 , 0 , 0] , 
            [1 , 1 , 0 , 0 , 1 , 0] , 
            [0 , 0 , 0 , 0 , 1 , 1] ,
            [0 , 0 , 1 , 1 , 0 , 0] ,
            [0 , 0 , 0 , 1 , 0 , 0]]
    adjacency_list = adjadency_matrix_to_list(adjacency_matrix)
    print(adjacency_list)
    
                    

