def diagonal_sum(matrix):
    sum=0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum

print(diagonal_sum([[1,2,3],[4,5,6],[7,8,9]] ))