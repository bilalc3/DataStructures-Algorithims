class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the dp table with 'inf' values
        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins) + 1)]

        # Base case: 0 coins are needed to make amount 0
        for i in range(len(coins) + 1):
            dp[i][0] = 0

        # Fill the dp table
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    # Either take the current coin or don't
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
                else:
                    # If the current coin is larger than the amount, skip the coin
                    dp[i][j] = dp[i - 1][j]

        # If dp[-1][-1] is still infinity, return -1, as the amount cannot be made with given coins
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
    


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float(inf)] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for a in range(1, amount + 1):
                if a >= c :
                    dp[a] = min(dp[a - c] + 1, dp[a])
        
        return dp[-1] if dp[-1] != float('inf') else -1
