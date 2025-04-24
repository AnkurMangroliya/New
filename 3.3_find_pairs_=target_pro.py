
def findPairs(nums,target):
    for i in range(len(nums)):
        for j in range(i+1):
            if nums[i] == nums[j]:
                continue
            elif (nums[i]+nums[j])==target:
                print(i,j)

myList=[1,2,3,2,3,4,5,6]
findPairs(myList,6)

# time complexity is O(n)2

# Another solution

def two_sum(nums,target):
    seen={}

    for i, num in enumerate(nums):
        compliment = target - num

        if compliment in seen:
            print(compliment)
            return [seen[compliment],i]

        seen[num] = i

print(two_sum(myList,6))