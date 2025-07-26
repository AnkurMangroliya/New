

def find_diagonal_tup(tup):
    return tuple(tup[i][i] for i in range(len(tup)))

# Example usage
input_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
output_tuple = find_diagonal_tup(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)