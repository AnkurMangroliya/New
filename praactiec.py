class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {')':'(','}':'{',']':'['}

        for i in s:
            if i in bracket:
                top = stack.pop() if stack else '#'
                if bracket[i] != top:
                    return False
            else:
                stack.append(i)
        return not stack


b = Solution()
print(b.isValid("())"))