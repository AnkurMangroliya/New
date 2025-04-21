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

