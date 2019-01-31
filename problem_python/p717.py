class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        def get_ans(bits):
            if len(bits) == 1:
                pass