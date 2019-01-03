class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        table = dict()
        for c in candies:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1
        
        return min(len(candies) // 2, len(table))