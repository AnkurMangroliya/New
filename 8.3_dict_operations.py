# FOr this time complexity is O(1) and space amortized O(1).
# For editing values space is O(n)
myDict = {"Name":"Ankur","age":27}
myDict["body"]="yes"
print(myDict)


def Searchdict(dict, value):
    for key in dict:
        if dict[key]==value:
            return key, value
    return "Not found"

print(Searchdict(myDict,27))

del myDict['age']     #SPace and time O(1)
print(myDict)

# .pop()  method also used to deleting element my_dict.pop("age"), it laso return value

