from collections import Counter
from typing import List
class Solution:
    def longestpalindrome(self,words: List[str])->int:
        freq = Counter(words)
        centre = False
        length = 0

        for w in words:
            rev = w[::-1]

            if w == rev:
                length += (freq[w]//2)*4
                if freq[w]%2==1:
                    centre = True

            elif rev in freq:
                pairs = min(freq[w],freq[rev])
                length += pairs * 4
                freq[w] -= 1
                freq[rev] -= 1
        
        if centre:
            length += 2
        
        return length
    
s = Solution()
a = s.longestpalindrome(["ab","ty","yt","lc","cl","ab"])
print(a)