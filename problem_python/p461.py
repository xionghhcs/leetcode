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

class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        for _ in range(32):
            xr = x % 2
            yr = y % 2
            x = x // 2
            y = y // 2
            if xr != yr:
                cnt += 1
        return cnt
