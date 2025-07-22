# Dictionary is a collection which is ordered, changeable and indexed.

# Dict is build using hash table

my_dict = dict(one="one",two='two')
print(my_dict)
my_dict2={'one':'1','two':'2'}
print(my_dict2)

# Time and Space complexity is O(n)

# ANother way to create dict

l = [('1','2'),('2','3')]
new = dict(l)
print(new)

# At the backend, hash function is used to store values.

#  if i give "1":"2".
# First it will hash "1" and then store that values in memory using index which provided by hash.

# Key and Value pair should be stored.

# After some key value. if same hash generate so it can pair values as linked list.

# See the next image where I have mentioned how same hash element is stored.