class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        limit = amount + 1
        dp = [0] * limit
        for a in range(limit):
            dp[a] = limit
        dp[0] = 0
        for a in range(1, limit):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)
        if dp[amount] == limit:
            return -1
        return dp[amount]