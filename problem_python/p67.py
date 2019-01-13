class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        ans = ''
        while i>=0 and j >=0:
            tmp = int(a[i]) + int(b[j]) + carry
            r = tmp % 2
            carry = tmp // 2
            ans = str(r) + ans
            i -= 1
            j -= 1
        
        while i >= 0:
            tmp = int(a[i]) + carry
            r = tmp % 2
            carry = tmp // 2
            ans = str(r) + ans
            i -= 1
        
        while j >= 0:
            tmp = int(b[j]) + carry
            r = tmp % 2
            carry = tmp // 2
            ans = str(r) + ans
            j -= 1
        
        return '1' + ans if carry == 1 else ans
        