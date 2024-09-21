class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            curr = nums[i]
            counter = 1
            for j in range(0, i ):
                if curr > nums[j]:
                    counter = max(counter, dp[j] + 1)
            dp[i] = counter
        
        return max(dp)

        
        
        

        