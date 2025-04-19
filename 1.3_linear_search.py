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

