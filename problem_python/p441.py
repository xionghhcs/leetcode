class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        row = 0
        pre = 0
        while row + pre <= n:
            row += 1
            pre += row
        return row - 1
