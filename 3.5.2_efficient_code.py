def max_pro(arr):
    arr.sort()
    return(max(arr[0]*arr[1],arr[-1]*arr[-2]))

print(max_pro([2,5,4,9,3,1,-10,-12]))