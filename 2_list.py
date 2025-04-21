a = [1,2,3,4,5]
print(a)
print( 1 in a)

# a[-1] will return last value, however begins with 0

empty = []
for i in empty:
    print("Nothing will be printed because it's empty error.")

# Update value to the list - time complexity O(1) and space O(1)
a[2]=33
print(a)

# Insertion element. There are 3 methods insert() append() and extend()
a.insert(0,11)
print(a)
#  For insertion, it has O(n) complexity because it requires to move each element backwards so.. ans space one is O(1)

a.append(12)
print(a)
# time complexity O(1) and space also same

new = [23,24]
a.extend(new)
print(a)
#  time and space O(n)

# slicing 
arr1 = ['a','b','c']
arr1[:1] = ['x','y']
print(arr1)

# For deletion, there are 3 methods pop(), delete() and remove()
print(arr1.pop(1))
print(arr1)
# If not provided index, it will delete the last element from the array snf it also print that element.

del arr1[0]
print(arr1)
# use slicing to delete more elements

arr1.remove('c')
print(arr1)
# Useful when you know the value and wants to delete.








