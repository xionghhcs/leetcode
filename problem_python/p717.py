class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in range(len(bits) - 2, -1, -1):
            if bits[i]==1:
                cnt += 1
            else:
                break
        return cnt % 2 == 0

