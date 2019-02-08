class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = dict()
        max_freq = 0
        max_index = 0
        ans = 0
        for idx, i in enumerate(nums):
            if i in table:
                table[i][0] += 1
                if max_freq < table[i][0]:
                    max_freq = table[i][0]
                    ans = idx - table[i][1] + 1
                elif max_freq == table[i][0]:
                    if ans > idx - table[i][1] + 1:
                        ans = idx - table[i][1] + 1
            else:
                table[i] = [1, idx]
        return ans

