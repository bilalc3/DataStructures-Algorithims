class Solution:
    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(l, r):
            while (l >=0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r +=1 
            
            return [l, r]
            
        ansl = 0
        ansr = 0

        for m in range(len(s)):
            # expand from each middle m 
            newl, newr = isPalindrome(m - 1, m + 1)
            if (newr - newl) > (ansr - ansl):
                ansl = newl
                ansr  = newr 

        for m1 in range(len(s) - 1):
            m2 = m1 + 1
            newl, newr = isPalindrome(m1, m2)
            if (newr - newl) > (ansr - ansl):
                ansl = newl
                ansr  = newr  
        
        return s[ansl + 1: ansr]