class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        for i, w in enumerate(words):
            words[i] = w[::-1]
        return ' '.join(words)