from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(path, nums_left, i):
            res.append(path[:])  

            if i >= len(nums_left):
                return 
            
            x = nums_left[i]

            # Include x in the path
            path.append(x)
            dfs(path, nums_left, i + 1)

            # Exclude x from the path (backtrack)
            path.pop()
            dfs(path, nums_left, i + 1)
        
        dfs([], nums, 0)
        return res
