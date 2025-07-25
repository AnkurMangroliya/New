# Tuples are immutable sequences in Python.
# Tuples are also comparable and hashable.

newTuples = ('a',)
# THis is a tuple with one element.

t = tuple("abcd")
print(t)  # Output: ('a', 'b', 'c', 'd')

print("a" in t)  # Output: True   //Time complexity: O(n)

print(t.index("b"))  # Output: 1   //Time complexity: O(n

def searchTuple(t, element):
    for i in range(len(t)):
        if t[i] == element:
            return(f"Element {element} found at index {i}")
    return(f"Element {element} not found in tuple")
            

print(searchTuple(t, "c"))  # Output: 2

print(t.count("a"))  # Output: 1   //Time complexity: O(n)

print(t.max())  # Output: 'd'   //Time complexity: O(n)
print(t.min())  # Output: 'a'   //Time complexity: O(n)

# COnverting a list to a tuple
l = [1, 2, 3, 4]
t = tuple(l)
print(t)  # Output: (1, 2, 3, 4)


