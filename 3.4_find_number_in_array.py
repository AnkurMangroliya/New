import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9])
target=4
for i in range(len(a)):
    if a[i]==target:
        print(f'{target} is found')
