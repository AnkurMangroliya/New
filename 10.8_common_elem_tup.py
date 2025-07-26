def common_element_tup(tup1, tup2):
    """
    This function takes two tuples as input and returns a tuple containing the common elements.
    """
    common_elements = set(tup1) & set(tup2)
    return tuple(common_elements)

print(common_element_tup((1, 2, 3), (3, 4, 5)))  # Expected output: (3,)