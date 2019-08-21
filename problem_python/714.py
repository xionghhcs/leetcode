class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1:
            return 0
        cost = 0
        hold = - prices[0]
        for i in range(1, len(prices)):
            cost = max(cost, hold + prices[i] - fee)
            hold = max(hold, cost - prices[i])
        return cost
