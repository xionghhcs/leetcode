class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pre_bit = -1
        while n > 0:
            r = n % 2
            n = n // 2
            if pre_bit == -1:
                pre_bit = r
            else:
                if pre_bit == r:
                    return False
                else:
                    pre_bit = r
        return True