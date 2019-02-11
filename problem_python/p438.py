class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p or len(p)> len(s):
            return []
        ans = []
        p = p.sort()
        for i in range(len(p), len(s)):
            c = s[i-len(p):i]
            c = c.sort()
            if c == p:
                ans.append(i - len(p))
        return ans
    
        