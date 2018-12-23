class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        base = 1
        for c in s[::-1]:
            idx = ord(c) - ord('A') + 1
            res = idx * base
            base = base * 26
        return res