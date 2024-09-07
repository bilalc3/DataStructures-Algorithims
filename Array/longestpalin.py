class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        hashMap = defaultdict(int)
        res = 0

        for word in words:
            reverse = word[::-1]
            if word in hashMap and hashMap[word] > 0:
                res += 4
                hashMap[word] -= 1
                hashMap[word] = max(hashMap[word], 0)
            else:
                hashMap[reverse] += 1

        # enumerating for double evens 
        for k, v in hashMap.items():
            if k[0] == k[1] and v > 0: # doubles
                res += 2
                break
        
        return res




        