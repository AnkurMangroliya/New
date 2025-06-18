import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(len(a))

# time and space complexity of insertion operation is O(mn)

new_col = np.insert(a, 0, [[10,11,12]], axis=1)
new_raw = np.insert(a, 0, [[10,11,12]], axis=0)
# axis=1 means added new column and axis=0 is raw.

print(new_col)
print(new_raw)

# Add new col at the last
new_co = np.append(a, [[105],[115],[155]], axis=1)
print(new_co)

# Accesing element from 2-dimentional array
def accesselement(array, r, c):
    if r >= len(a) and c >= len(a[0]):
        print("Incorrect index")
    else:
        print(a[r][c])

accesselement(a,1,1)

# Traversal of array
print("traveral of array")
def traversal(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traversal(a)

# function which search element in the array
print("search element from the array")
def search(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==target:
                return f"target{target} is located at raw {i} and cloumn {j}"
                # can also return like this
                return 'The value is located at index'+str(i)+" "+str(j)
    return 'The element is not found.'

print(search(a,3))

# deleting an row or column from the array
print("deletion operation...")
print(a)
newarray = np.delete(a, 0, axis=0)
print(newarray)
#  axis=1 would delete the column.



