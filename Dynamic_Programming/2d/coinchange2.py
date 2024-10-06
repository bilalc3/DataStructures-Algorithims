class Solution:
    def change_n2(self, amount: int, coins: List[int]) -> int:
        c  = len(coins)
        dp = [[0] * (amount + 1) for _ in range(c + 1)]
        
        dp = [0] * (amount + 1 )
        dp[0][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(0, amount + 1):
                dp[i][j] = dp[i -  1][j] # without using current key
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]
        return dp[c][amount]

    def change(self, amount: int, coins: List[int]) -> int:
        c  = len(coins)
       
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for i in range(c, amount + 1):
                # we add the total without coin and with 
                dp[i] += dp[i - c]
        
        return dp[-1]