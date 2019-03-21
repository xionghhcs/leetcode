class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * col for _ in range(row)]
        ans = 0
        for i in range(row):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                ans = 1
        for j in range(col):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                ans = 1
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    if dp[i][j] > ans:
                        ans = dp[i][j]
                else:
                    dp[i][j] = 0
        return ans ** 2
