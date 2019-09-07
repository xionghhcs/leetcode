class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        ans = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2 if i-2>=0 else 0] + 2
                elif i - dp[i-1]>0 and s[i - dp[i-1]-1] == '(':
                    tmp = i - dp[i-1] - 2
                    dp[i] = dp[i-1] + dp[tmp if tmp >=0 else 0] + 2
                ans = max(ans, dp[i])
        return ans
