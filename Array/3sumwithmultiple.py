class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:


        def twosum(temptarg, nums):
            ans = 0
            hashmap = defaultdict(int)
            for n in nums:
                if n in hashmap:
                    ans += hashmap[n]
                
                hashmap[temptarg - n] += 1
            return ans

        res = 0
        for i in range(len(arr)):
            
            temptarg = target - arr[i]
            res += twosum(temptarg, arr[i+1:])
        
        return res % (10 ** 9  + 7)