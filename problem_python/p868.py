class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        i = 0
        for j, v in enumerate(bin(N)[2:]):
            if v == '1':
                ans = max(j - i, ans)
                i = j
        return ans