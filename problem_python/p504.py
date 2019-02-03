class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        flag = 1 if num > 0 else -1
        d = []
        while num > 0:
            r = num % 7:
            num = num // 7
            d.append(r)
        d = ''.join(d[::-1])
        if flag == -1:
            d = '-' + d
        return d
    

