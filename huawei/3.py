class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        import collections
        ans = 0
        for i in range(len(s)):
            table = dict()
            cnt = 0
            for j in range(i, len(s)):
                if s[j] not in table:
                    table[s[j]] = 1
                    cnt += 1
                    if cnt > ans:
                        ans = cnt
                else:
                    break
        return ans

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = left
        table = set()
        ans = 0
        while left < len(s) and right < len(s):
            if s[right] not in table:
                table.add(s[right])
                if len(table) > ans:
                    ans = len(table)
                right += 1
            else:
                while s[left] != s[right]:
                    table.remove(s[left])
                    left += 1
                table.remove(s[left])
                left += 1
                if len(table)> ans:
                    ans = len(table)
        return ans
