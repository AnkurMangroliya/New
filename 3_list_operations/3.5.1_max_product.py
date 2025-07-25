def max_product(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in arr:
        if num>max1:
            max2=max1
            max1=num
        elif num > max2:
            max2=num
        
        # Update min1 and min2
        if num<min1:
            min2=min1
            min1=num
        elif num<min2:
            min2=num
    print(max1,max2,min1,min2)
    return max(max1*max2,min1*min2)

print(max_product([-1,-2,-4,-5,-8,-2,-3]))
