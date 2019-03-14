class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]
        ans = 1
        max_idx = 0
        for i in range(len(s)):
            dp[i][i] = 1
            if i < len(s) - 1 and s[i] == s[i+1]:
                dp[i][i+1] = 1
                ans = 2
                max_idx = i
        
        for l in range(3, len(s)+1):
            for i in range(0, len(s) - l + 1):
                j = i + l - 1
                if s[i] == s[j] and dp[i][j] == 1:
                    dp[i][j] = 1
                    ans = l
                    max_idx = i
        
        return s[max_idx:max_idx + ans]

        