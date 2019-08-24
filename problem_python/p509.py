class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N-1) +self.fib(N-2)

class Solution2:
    def fib(self, N: int) -> int:
        if N <=1:
            return N
        f = [0] * (N + 1)
        f[0] = 0
        f[1] = 1
        for i in range(2, N+1):
            f[i] = f[i-1] + f[i-2]
        return f[N]
    