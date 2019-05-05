class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = dict()
        for c in s:
            table[c] = table.get(c, 0) + 1
        ans = 0
        for k in table:
            if table[k] > 1:
                while table[k] > 1:
                    ans += 2
                    table[k] = table[k] - 2
        for k in table:
            if table[k] == 1:
                ans += 1
                break
        return ans

