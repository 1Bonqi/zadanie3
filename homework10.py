def get_matrix(n, v , value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(v):
            matrix[i].append(value)
    return matrix


print(get_matrix(2,2,10))
print(get_matrix(3,5,42))
print(get_matrix(4, 2,13))
