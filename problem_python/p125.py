class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and (not s[i].isalpha() and not s[i].isdigit()):
                i += 1
            while i < j and (not s[j].isalpha() and not s[j].isdigit()):
                j -= 1
            print('{}:{}'.format(s[i], s[j]))
            print('{}:{}'.format(i,j))
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True