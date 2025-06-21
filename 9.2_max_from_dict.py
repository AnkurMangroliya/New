# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

# Example:

# my_dict = {'a': 5, 'b': 9, 'c': 2}
# max_value_key(my_dict))
# Output:

# b

def max_value_key(my_dict):
    max= float('-inf')
    key= None
    for k,v in my_dict.items():
        if v>max:
            max = v
            key=k
    return key

def maxi(my_dict):
    return max(my_dict, key=my_dict.get)

my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))
print(maxi(my_dict))

