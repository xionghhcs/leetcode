class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        mp = dict()
        for i in range(len(s)):
            if s[i] in mp:
                if mp[s[i]] != t[i]:
                    return False
            else:
                mp[s[i]] = t[i]
        mp = dict()
        for i in range(len(s)):
            if t[i] in mp:
                if mp[t[i]] != s[i]:
                    return False
            else:
                mp[t[i]] = s[i]
        return True

