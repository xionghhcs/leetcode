class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(len(s)):
            if i == 0:
                dp[i] = 1
            else:
                if s[i] == '0':
                    dp[i] = dp[i-1]
                elif 
        