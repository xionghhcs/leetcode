class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        mid = (1+ n) // 2
        r = guess(mid)
        while r != 0:
            if r == -1:
                mid = (mid + 1 + n) // 2
                r = guess(mid)
            else:
                mid = (1 + mid - 1) // 2
                r = guess(mid)
        return mid
