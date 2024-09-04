class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []


        def dfs(sum, comb, i):

            if sum == target:
                res.append(comb[:])
            elif sum > target or  i >= len(candidates):
                return
            else:
                print(comb)
                # add curr and add other 
                comb.append(candidates[i])
                dfs(sum + candidates[i], comb, i)

                comb.pop()
                dfs(sum, comb, i + 1)

                    
                
        dfs(0, [], 0)

        return res
        