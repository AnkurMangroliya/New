pre_list = [1,2,3,4,5]
new_list = [i*2 for i in pre_list]
print(new_list)


# Conditional List Comprehension
new_l = [number for number in pre_list if number>3]
print(new_l)


# also mentino condition ahead of for loop
n = [number if number>0 else 0 for number in pre_list]
print(n)