class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        import collections
        table = dict()

        ans = 0
        start = -1

        for c in s:
            table[c] = -1
        
        for i, c in enumerate(s):
            if table[c] > start:
                start = table[c]
            ans = max(ans, i - start)
            table[c] = i
        return ans
