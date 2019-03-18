class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        import collections
        table = collections.defaultdict(int)
        