import array

a = array.array('i',[1,2,3,4,5])

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

print(linear_search(a,1))

# If I want to remove element from the array

a.remove(1)
print(a)

# append an elment at the end of array

a.append(6)
print(a)

a.insert(1,3)
print(a)

# step:5  extend the array
b = array.array('i',[1,2,3,4,5])
a.extend(b)
print(a)

# step: 6 adding values to array using fromlist() method
print("step 6")
c =[20,34,22]
b.fromlist(c)
print(b)


# remove method removes element from any where, whereas pop method will remove from the last 
a.pop()
print(a)

#  .index(11) provides the index location in the array where 11 is present.
# step 9
print(a.index(1))

#  step 11 Get array buffer information through buffer_info method
print("step 11")
print(a.buffer_info())
# this will print where array values are stored. like this (1615008735344, 10)

# step 12 count method which count the element from the array
print("step 12")
print(a.count(2))


# step 13 Convert an array to a python list with same elements using tolist()

print('step 13')
print(a.tolist())

