class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n > 0:
            if n % 2 == 1:
                ans += 1
            n = n // 2
        return ans


class Solution2:
    def hammingWeight(self, n):
        return bin(n).count(1)


class Solution3:
    def hammingWeight(self, n):
        ans = 0
        while n > 0:
            ans += n & 1
            n = n >> 1
        return ans