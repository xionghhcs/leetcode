class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <=1:
            return 0
        min_val = prices[0]
        max_val = 0
        for p in prices[1:]:
            if p > min_val:
                sell_profit = p - min_val
                if sell_profit > max_val:
                    max_val = sell_profit
                
            if p < min_val :
                min_val = p
        return max_val