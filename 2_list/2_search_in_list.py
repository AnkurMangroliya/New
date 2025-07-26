l1 = [1,2,3,4,5,6,7]

target = int(input("Enter the number:"))
print(type(target))
if target in l1:
    print(f"{target} is present in the list.")
else:
    print("Element not found.")
# This will search in linear fashion that why it has O(n) complexity.


# Linear search
def linear_search(list,target1):
    for i, value in enumerate(list):
        if value == target1:
            return i
    return -1
print(linear_search(l1,5))
# Enumerate function keeps track of current items that's why time complexity is O(n). space is O(1).

# List operations:
a=[0,1,2]
b=[4,5,6]
c=a+b
print(c)
# This will concatenate two list and give output -> [0, 1, 2, 4, 5, 6]

# * and give result : [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
a = a * 4
print(a)

# there are methods which helpful to find max(a), min(a),sum(a), for average -> sum(a)/len(a).

# find the average of input numbers from user until enters done.

# Solution 1
total=0
a=[]
while(True):
    number = input("Enter a number:")
    if number == 'done':
        break
    else:
        a.append(int(number))
print(sum(a)/len(a))

# Solution 2:
total=0
count=0
while(True):
    number = input("Enter a number:")
    if number == 'done':
        break
    else:
        value=float(number)
        total = total + value
        count = count + 1
        average = total / count

print("Average", average)

