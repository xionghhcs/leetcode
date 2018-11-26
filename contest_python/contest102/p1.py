class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [v for v in A if v % 2 == 0] + [v for v in A if v % 2 ==1]