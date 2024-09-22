class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False 
        
        split = total_sum // 2

        total_set = set()
        total_set.add(split)
        for n in nums:
            temp_set = total_set.copy()
            if n in temp_set:
                return True
            
            # if no match add the new values
            for val in temp_set:
                total_set.add(val - n)
        
        return False
                            
        
        