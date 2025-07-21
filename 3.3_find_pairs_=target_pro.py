
# def findPairs(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1):
#             if nums[i] == nums[j]:
#                 continue
#             elif (nums[i]+nums[j])==target:
#                 print(i,j)

# myList=[1,2,3,2,3,4,5,6]
# findPairs(myList,6)

# # time complexity is O(n)2

# # Another solution

# def two_sum(nums,target):
#     seen={}

#     for i, num in enumerate(nums):
#         compliment = target - num

#         if compliment in seen:
#             print(compliment)
#             return [seen[compliment],i]

#         seen[num] = i

# print(two_sum(myList,6))


def two_sum(nums, target):
    seen = {}
    
    for i,num in enumerate(nums):
        compliment = target - num

        if compliment in seen:
            return [seen[compliment],i]
        seen[num]=i
        print(seen)
 
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")