class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i], prices[i - 1])
        return ans

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1 :
            return 0
        
        dp = [[0] * len(prices) for _ in range(len(prices))]
        
        dp[0][0] = 0
        dp[0][1] = - prices[0]
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[len(prices)-1][0]
