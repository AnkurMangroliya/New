import array
import numpy as np


my_array = array.array('i',[1,2,3,4,5])

my_array.insert(0,3)
print(my_array)

my_array.insert(6,1)
print(my_array)

#  Insert element has space O(1) but time one is O(n).


def traveral(ar):
    for i in ar:
        print(i)

traveral(my_array)

# ✅ Time Complexity: O(n)
# You're iterating through every element in the array ar.

# For each element, you're doing a print(i), which is an O(1) operation.

# Total time = O(n), where n is the number of elements in ar.

# ✅ Space Complexity: O(1)
# You're not creating any new data structures.

# You’re only using a constant amount of space (i in the loop).

# The print function doesn't store anything—it just outputs it.

# ➡️ So: Space = O(1) (constant extra space).


# Accessing element from array

def accesselement(array,index):
    if index > len(array):
        print("Index is out of bound")
    else:
        print(array[index])

# this function has time complexity and space is O(1)

accesselement(my_array,8)
accesselement(my_array,2)


