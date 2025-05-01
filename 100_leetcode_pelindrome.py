class Solution:
    def isPalindrome(self, x: int) -> bool:
        new = str(x)
        if new == new[::-1]:
            return True
        else:
            return False
    
s = Solution()
print(s.isPalindrome(23432))

class Ram:
    def ispali(self,x: int) -> bool:
        if x<0 or (x%10==0 and x != 0):
            return False
        reversed_half=0

        while reversed_half < x:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        return x==reversed_half or x == reversed_half // 10

r = Ram()
print(r.ispali(123454321))