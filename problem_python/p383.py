class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a_t = dict()
        b_t = dict()
        for c in ransomNote:
            if c in a_t:
                a_t[c] += 1
            else:
                a_t[c] = 1
        
        for c in magazine:
            if c in b_t:
                b_t[c] += 1
            else:
                b_t[c] = 1
        
        for k in a_t:
            if k in b_t:
                b_t[k] -= a_t[k]
                if b_t[k] < 0:
                    return False
            else:
                return False
        return True