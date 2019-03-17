class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = 0
        cnt = 1
        if len(A) <3:
            return 0
        for i in range(1, len(A) - 1):
            if A[i] - A[i-1] == A[i+1] - A[i]:
                ans += cnt
                cnt += 1
            else:
                cnt = 1
        return ans

        