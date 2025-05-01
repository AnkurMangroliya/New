def max_product(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in arr:
        if num>max1:
            max2=max1
            max1=num
        elif num > max2:
            max2=num
    return max1*max2

print(max_product([3,5,2,6,8,9]))
