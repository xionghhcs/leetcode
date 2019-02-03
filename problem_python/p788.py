class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def judge(n):
            d = []
            flag = False
            while n > 0:
                r = n % 10
                n = n // 10
                if r in [3, 4, 7]:
                    return False
                if r in [2, 5, 6, 9]:
                    flag = True
            return flag
        
        ans = 0
        for i in range(1, N + 1):
            if judge(i):
                ans += 1
        return ans
    