class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ans = 0
        for i in range(len(A[0])):
            j = 0
            while j + 1 < len(A):
                if A[j][i] > A[j + 1][i]:
                    break
                j += 1
            if j + 1 < len(A):
               ans += 1
        return ans