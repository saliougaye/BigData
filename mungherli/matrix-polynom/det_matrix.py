def determinant(matrix):

    ind = list(range(len(matrix)))

    # caso base
    if len(matrix) == 2 and len(matrix[0]) == 2:
        res = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return res

    total = 0
    
    for c in ind:
        # copio la matrice togliendo la prima riga
        copy = matrix[1:]

        h = len(copy)

        for i in range(h):
            copy[i] = copy[i][0:c] + copy[i][c+1:]
        
        s = (-1)**(c%2)

        sub_det = determinant(copy)
        total += s * matrix[0][c] * sub_det
    
    return total


print(determinant(
    [
        [1,0,5],
        [2,-1,0],
        [7,-2,0]
    ]
))