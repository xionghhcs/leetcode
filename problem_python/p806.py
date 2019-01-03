class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        ans = 1
        cur_length = 0
        for c in S:
            if cur_length + widths[ord(c) - ord('a')] <=100:
                cur_length += widths[ord(c) - ord('a')]
            else:
                ans += 1
                cur_length = widths[ord(c) - ord('a')]
        return [ans, cur_length]