def matrix_chain_multiplication(p):
    n = len(p)- 1
    m = list()
    s = list()
    for i in range(n):
        zeros = [0] * n
        m.append(list(zeros))
        s.append(list(zeros))
    for l in range(2, n+1):
        for i in range (n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j, 1):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if (q < m[i][j]):
                    m[i][j] = q
                    s[i][j] = k + 1
    return m, s


if __name__ == "__main__":
    p_list = [20, 15, 35, 5, 40, 50]
    m_matrix, s_matrix = matrix_chain_multiplication(p_list)
    print(m_matrix)
    print(s_matrix)
    
