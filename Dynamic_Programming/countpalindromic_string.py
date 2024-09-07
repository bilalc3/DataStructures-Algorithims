class Solution:
    def countSubstrings(self, s: str) -> int:


        def getNumberPalindromes(l, r):
            accum = 0
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
                accum += 1

            return accum        

        total_sum = 0
        for i in range(len(s)):
            total_sum += getNumberPalindromes(i - 1, i + 1) 
            total_sum += 1 # to account for char itsefl
        
        for i in range(len(s) - 1):
            j = i + 1
            total_sum += getNumberPalindromes(i, j)
        
        return total_sum
            


        