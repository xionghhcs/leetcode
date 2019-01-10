class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        table = [0] * n
        for i in range(2, n):
            if i * i >=n:
                break
            if table[i] == -1:
                continue

            j = i * i
            while j < n:
                table[j] = -1
                j += i
        cnt = 0
        for i in range(2, n):
            if table[i] == 0:
                cnt += 1
        return cnt