class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_pos = nums[0]
        dp_neg = nums[0]
        dp_max = nums[0]

        for n in nums[1:]:
            temp = max(dp_pos * n, dp_neg * n, n)
            dp_neg = min(dp_pos * n, dp_neg * n, n)
            dp_pos = temp
            dp_max = max(dp_pos, dp_neg, dp_max)

        
        return dp_max


            

        