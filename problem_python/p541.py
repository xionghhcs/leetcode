class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ''
        for i in range(0, len(s), k):
            tmp = i // k
            j = i + k -1
            if j >= len(s):
                j = len(s) - 1
            if tmp % 2 == 0: 
                while i <= j:
                    ans += s[j]
                    j -= 1
            else:
                while i <=j:
                    ans += s[i]
                    i += 1
        return ans