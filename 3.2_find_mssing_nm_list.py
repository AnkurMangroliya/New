a=[]
for i in range(1,101):
    a.append(i)

a.remove(12)
print(a)

def find_missing_value(arr,n):
    sum1 = n*(n+1)/2
    sum2 = sum(arr)
    return (sum1-sum2)

print(find_missing_value(a,100))