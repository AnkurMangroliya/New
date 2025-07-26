def tuple_elementwise_sum(t1,t2):
    if len(t1) != len(t2):
        raise ValueError("Tuples must be of the same length")
    
    return tuple(a+b for a,b in zip(t1,t2))

print(tuple_elementwise_sum((1, 2, 3), (4, 5, 6)))  # Output: (5, 7, 9)


# Alteratively, using map function
def tuple_elementwise_sum_map(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Tuples must be of the same length")
    
    return tuple(map(sum, zip(t1, t2)))

print(tuple_elementwise_sum_map((1, 2, 3), (4, 5, 6)))  # Output: (5, 7, 9)