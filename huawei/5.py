class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        dp = [[0] * s_len for _ in range(s_len)]
        ans = 1
        max_idx = 0
        for i in range(s_len):
            dp[i][i] = 1
            if i+1 < s_len and s[i] == s[i+1]:
                dp[i][i+1] = 1
                ans = 2
                max_idx = i
        
        for l in range(3, s_len + 1):
            for j in range(0, s_len - l + 1):
                k = j + l - 1
                if s[j] == s[k] and dp[j+1][k-1] == 1:
                    dp[j][k] = 1
                    ans = l
                    max_idx = j
            
        return s[max_idx: max_idx + ans]
