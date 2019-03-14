class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * m for _ in range(n)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                if i-1>=0 and j-1>=0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i-1>=0:
                    dp[i][j] = dp[i-1][j]
                elif j-1>=0:
                    dp[i][j] = dp[i][j-1]
        
        return dp[n-1][m-1]
