class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        中心扩展，需要考虑奇数和偶数，每次从中心一个字符或者两个字符向两边扩展。
        """
        def get_count(s, i, j):
            cnt = 0
            while i>=0 and j<len(s) and s[i]==s[j]:
                cnt += 1
                i-=1 
                j += 1
            return cnt
        
        ans = 0
        for i in range(len(s)):
            ans += get_count(s, i, i)
            ans += get_count(s, i, i+ 1)
        return ans

class Solution2:
    def countSubstrings(self, s):
        if s is None:
            return 0
        dp = [[0] * len(s) for _ in range(len(s))]
        ans = 0
        
        for i in range(len(s)):
            dp[i][i] = 1
            ans += 1
            if i > 0 and s[i] == s[i-1]:
                dp[i-1][i] = 1
                ans += 1

        for k in range(3, len(s)+1):
            for j in range(k - 1, len(s)):
                if s[j] == s[j - (k-1)] and dp[j - (k-1) + 1][j-1] == 1:
                    ans += 1
                    dp[j-(k-1)][j] = 1

        return ans
