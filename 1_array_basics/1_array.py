import array

a = array.array('i')
print(a)
b = array.array('i',[1,2,3,4])
print(b)


import numpy as np
c = np.array([])
print(c)


d = np.array([1,2,3,4], dtype=int)
print(d)
print(d.dtype)

# For empty array time and space complexity are O(1)


# For non-empty array -> time and space complexity are O(n)
# ✅ Short Answer:
# Time Complexity: O(n) — because each element must be written (initialized).
# Space Complexity: O(n) — because you’re allocating memory for n elements.

