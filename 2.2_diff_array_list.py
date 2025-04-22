# array and list both are mutable.
# Both can be indexed and iterated through.
# They can be both sliced.

# Array
# Better when one wants to perform similar arithmetic operations.

# example
import numpy as np

myArray = np.array([1,2,3,4,5])
print(myArray/2)
myList = [1,2,3,4,5]
print(myList/2) #This will give error because the list is not suitable for this kind of operations. Better to use array.

# List can store different type of values, whereas array can't.
