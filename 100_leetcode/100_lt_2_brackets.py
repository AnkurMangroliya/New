# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         bracket = {')':'(','}':'{',']':'['}

#         for char in s:
#             if char in bracket:
#                 top = stack.pop() if stack else '#'
#                 if bracket[char] != top:
#                     return False
#             else:
#                 stack.append(char)
#         return not stack

# sol = Solution()  
# print(sol.isValid('{()}'))



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {')':'(','}':'{',']':'['}

        for char in s:
            if char in bracket:
                top = stack.pop() if stack else '#'
                if bracket[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack

sol = Solution()  
print(sol.isValid('{()}'))