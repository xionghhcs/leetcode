class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        def count1(a):
            num = 0
            while a != 0:
                num += a & 1
                a >>= 1
            return num
        ans = x ^ y
        return count1(ans)