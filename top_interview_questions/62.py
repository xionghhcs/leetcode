class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            n, m = m, n
        dp = [1 for _ in range(n)]
        for _ in range(m = 1):
            for i in range(1, n):
                dp[i] += dp[i-1]
        return dp[n - 1]

class Solution2:
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                dp[i][j] += dp[i-1][j] if i-1>=0 else 0
                dp[i][j] += dp[i][j-1] if j-1 >=0 else 0
        return dp[-1][-1]