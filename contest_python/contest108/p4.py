class Solution:

    def beautifulArray(self, N):
        """
        Author: farr3l
        :type N: int
        :rtype: List[int]
        """
        if N == 1:
            return [1]
        l = self.beautifulArray(N // 2)
        r = self.beautifulArray(N - N // 2)
        return [x * 2 for x in l] + [x * 2 - 1 for x in r]


class Solution2:
    def beautifulArray(self, N):
        a = list(range(1, N + 1))
        return self.r_fun(a)
        pass

    def r_fun(self, a):
        if len(a) <= 1:
            return a
        odd = [v for idx, v in enumerate(a) if idx % 2 == 1]
        even = [v for idx, v, in enumerate(a) if idx % 2 == 0]
        odd = self.r_fun(odd)
        even = self.r_fun(even)
        return odd + even
