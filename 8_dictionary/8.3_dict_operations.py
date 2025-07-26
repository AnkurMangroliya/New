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

# to remove last element, I have to use .popitem() method

# my_dict.clear()
# Used to delete all elements and {} should be stayed.   Time complexity is O(n)


new_dict = myDict.copy()  # it creates shallow copy. means different dict that existing one.
print(new_dict)


# Another way to create dictniories.
newDict = {}.fromkeys([1,2,3],0)   #helpful to create new dict with same values.
print(newDict)
#  If you don't provide values it will take None.

print(newDict.get(1,10))   # This will return values if existing otherwise return 10 which is set at the last.

print(newDict.keys())

# Another method

newD = {"ankur":"Mangroliya"}

newDict.update(newD)
print(newDict)

newDict.update({1:0})
print(newDict)

# If values are present it did not changed anythings.

print(1 in newDict)  # by default it's keys take
print("Mangroliya" in newDict.values())

print(len(newDict))
print(all(newDict))  # This will give true if all keys are positive like not 0 as keys stored. otherwise give False
print(any(new_dict))  # only false if all keys are false, otherwise true

print(newDict)
print(sorted(newD))

