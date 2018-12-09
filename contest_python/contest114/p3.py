class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ans = 0
        columns = len(A)
        for c in range(columns):
            flag = []
            for r in range(1, len(A)):
                if A[r-1][c] > A[r][c]:
                    ans += 1
                    break
                elif A[r - 1][c] == A[r][c]:
                    flag.append(r - 1)
                    flag.append(r)
            else:
                if len(flag) > 0:
                    flag = list(set(flag))
                    flag.sort()
                    subset = []
                    for i in flag:
                        subset.append(A[i])
                    A = subset
                else:
                    break

        return ans
