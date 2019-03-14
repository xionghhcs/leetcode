class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        if grid is None:
            return None
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i-1>=0 and j-1>=0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                elif i-1>=0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif j-1>=0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
        return dp[n-1][m-1]

                