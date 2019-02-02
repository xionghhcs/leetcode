class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = 'aeiou'
        i, j = 0, len(s) - 1
        s = list(s)
        while i <j:
            while i < j:
                if s[i] not in v:
                    i += 1
                else:
                    break
            while i < j:
                if s[j] not in v:
                    j -= 1
                else:
                    break
            t = s[i]
            s[i] = s[j]
            s[j] = t
            i += 1
            j -= 1
        s = ''.join(s)
        return s