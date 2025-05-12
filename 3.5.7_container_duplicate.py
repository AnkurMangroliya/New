# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example :

# Input: nums = [1,2,3,1]
# Output: true
# Hint: Use sets


def contains_duplicate(nums):
    s = set()
    for i in range(len(nums)):    
        if nums[i] in s:
            return True
        s.add(nums[i])
    return False

print(contains_duplicate([1,2,3,1]))