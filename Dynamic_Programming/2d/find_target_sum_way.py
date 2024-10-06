class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # setting up
        big_dp = defaultdict(int)
        big_dp[nums[0]] += 1
        big_dp[-nums[0]] += 1

        # iterating over
        for n in nums[1::]:
            temp_dp = defaultdict(int)
            for k, v in big_dp.items():
                temp_dp[k - n] += v
                temp_dp[k + n] += v
            
            big_dp = temp_dp
        
        return big_dp[target]