class Solution:
    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            curr = nums[i]
            counter = 1
            for j in range(0, i ):
                if curr > nums[j]:
                    counter = max(counter, dp[j] + 1)
            dp[i] = counter
        
        return max(dp)

    
    def lengthOfLIS(self, nums: List[int]) -> int:
        # binary serach approach 
        def binary_search(tails, target):
            low, high = 0, len(tails) - 1
            while low <= high:
                mid = (low + high) // 2
                if tails[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low


        lis = []
        for n in nums:
            # place in proper area 
            index = binary_search(lis, n)
            if index >= len(lis):
                # need top append 
                lis.append(n)
            else:
                # need to replace ith char with smth smaller 
                lis[index] = n
        
        return len(lis)

      
        
        

        