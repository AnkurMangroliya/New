class Solution:
    def isPalindrome(self, x: int) -> bool:
        new = str(x)
        if new == new[::-1]:
            return True
        else:
            return False
    
s = Solution()
print(s.isPalindrome(23432))