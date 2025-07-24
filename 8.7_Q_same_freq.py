# Same Frequency
# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

# Example:

# list1 = [1, 2, 3, 2, 1]
# list2 = [3, 1, 2, 1, 3]
# check_same_frequency(list1, list2)
# Output:

# False



def check_same_frequency(list1, list2):
    def counter(lst):
        c={}
        for element in lst:
            c[element] = c.get(element, 0)+1
        # Print key and value pairs
        for key, value in c.items():
            print(f"{key}: {value}")
        return c
    
    
    return counter(list1) == counter(list2)

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]     
print(check_same_frequency(list1, list2))  # Output: True