class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_ans(n):
            if n <=3:
                return True
            else:
                return get_ans(n-1) or get_ans(n-1) or get_ans(n-3)
        return get_ans(n)