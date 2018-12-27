class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_table = dict()
        t_table = dict()
        for c in s:
            if c in s_table:
                s_table[c] += 1
            else:
                s_table[c] = 1
        
        for c in t:
            if c in t_table:
                t_table[c] += 1
            else:
                t_table[c] = 1
        
        for k in t_table:
            if k not in s_table:
                return k
            else:
                if t_table[k] != s_table[k]:
                    return k