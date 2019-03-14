class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * len(triangle)

        for idx, row in enumerate(triangle):
            if idx == 0:
                dp[0] = row[0]
            else:
                tmp = [0] * len(triangle)
                for j in range(len(row)):
                    if j == 0:
                        tmp[j] = dp[j] + row[j]
                    elif j == len(row) -1 :
                        tmp[j] = dp[j - 1] + row[j]
                    else:
                        tmp[j] = min(dp[j-1], dp[j]) + row[j]
                dp = tmp
        return min(dp)

