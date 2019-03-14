class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = {w:1 for w in wordDict}
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            for j in range(i-1, -1, -1):
                if dp[j]==1 and s[j:i] in words:
                    dp[i] = 1
                    break
        return True if dp[-1] == 1 else False

        