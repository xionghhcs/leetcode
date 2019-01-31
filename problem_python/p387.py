class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        d = collections.OrderedDict()
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        for k in d:
            if d[k] == 1:
                return s.find(k)
        return -1