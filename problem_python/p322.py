class Solution:
    """
    方法比较耗时
    """
    def coinChange(self, coins, amount):
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, dp[i-c] + 1)
            dp[i] = cost
        if dp[amount] == float('inf'):
            return - 1
        return dp[amount]