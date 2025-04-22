# Convert string to list.
a = 'ram'
list1=list(a)
print(list1)

#  Convert multiple words to list
b = " ankur ram chaman"
list2 = b.split()
print(list2)

# Convert the string using delimeter. Moreover, one can convert any delimeter as parameter.
c = "a-s-sfsd-sdffs-sfs"
delimeter='-'
list3=c.split(delimeter)
print(list3)

# Join function use to join back after spliting string into list.
print(list3)
print(delimeter.join(list3))

# sort function will remove original list so you can use sorted(list3)
sorted(list3)
print(list3)


# The below is the example to reference only 1 list even if there are 2.
li1= [1,2,3,4,5]
li2 = li1   #This is point to one if I change something will also change in li1.

li3 = li1[:]  #THis code will create a new array.

