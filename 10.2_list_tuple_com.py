tuple1 = 1,2,3,4,5

tuple1= 2,3,4

print(tuple1)  # Output: (2, 3, 4)

# We can reassign entire tuples but not individual elements

del tuple1  # Deletes the entire tuple

# print(tuple1)  # Raises NameError: name 'tuple1' is not defined

# we can't delete individual elements in a tuple

# list of function that can be used with tuples
# len(), max(), min(), count(), index()
t = (1, 2, 3, 4, 5)
print(len(t))  # Output: 5   //Time complexity: O(1)  
print(max(t))  # Output: 5   //Time complexity: O(n)
print(min(t))  # Output: 1   //Time complexity: O(n)
print(t.count(3))  # Output: 1   //Time complexity: O(n)
print(t.index(3))  # Output: 2   //Time complexity: O(n)

# Methods that can not used with tuples
# append(), extend(), insert(), remove(), pop(), clear(), sort(), reverse()

# I can create tuple in list and list in tuple
t = ([1, 2], (3, 4), "hello")
print(t)  # Output: ([1, 2], (3, 4), 'hello')

l = [(1, 2), (3, 4), (5, 6)]
print(l)  # Output: [(1, 2), (3, 4), (5, 6)]

# We generally use tuples to store heterogeneous data, like a record or a row in a database, and list to store homogeneous data, like a list of numbers or a list of strings.

