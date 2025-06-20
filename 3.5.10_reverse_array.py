import array
def rev(array):
    for i in range(int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i]=array[other]
        array[other] = temp
    return array

a = array.array('i',[1,2,3,4,5,6,7,8])
print(rev(a))