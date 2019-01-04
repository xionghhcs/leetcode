class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = n
        while tmp >= 10:
            ans = []
            while tmp >0:
                r = tmp % 10
                tmp = tmp // 10
                ans.append(r ** 2)
            tmp = sum(ans)
            if tmp == 1:
                return True
        return True if tmp in (1,7) else False