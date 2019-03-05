class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        ans = 0
        while 5 ** i < n:
            i += 1
        
        for j in range(1, i  + 1):
            ans += int(n // (5 ** j))
        
        return ans
