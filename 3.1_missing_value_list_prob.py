# array has missing value from 1 to 6. if 5 is missing find that.

def missing(arr,n):
    total = n*(n+1)/2
    s = sum(arr)

    return (total-s)

print(missing([1,2,3,4,6],6))