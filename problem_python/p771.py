class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0
        for c in S:
            if c in J:
                ans += 1
        return ans


class Solution2:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        hash_table = {c:1 for c in J}
        ans = 0
        for c in S:
            if c in hash_table:
                ans += 1
        return ans