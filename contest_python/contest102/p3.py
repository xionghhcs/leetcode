class Solution:
    def sumSubarrayMins(self, A):
        """
        O(n^2)
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        mod = 1000000000 + 7
        for idx in range(0, len(A)):
            min_v = 30000 + 1
            for j in range(idx, len(A)):
                if min_v > A[j]:
                    ans += A[j]
                    min_v = A[j]
                else:
                    ans += min_v
        return ans % mod


class Solution2:
    def sumSubarrayMins(self, A):
        """
        O(n^2)
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        mod = 1000000000 + 7

        return ans % mod


if __name__ == '__main__':
    pass
