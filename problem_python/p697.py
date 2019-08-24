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

class Solution2:
    def findShortestSubArray(self, nums: List[int]) -> int:
        table = dict()
        max_degree = 1
        min_len = 1
        for idx, c in enumerate(nums):
            if c not in table:
                table[c] = [1, idx]
            else:
                table[c][0] += 1
                tmp_len = idx - table[c][1] + 1
                if table[c][0] > max_degree:
                    max_degree = table[c][0]
                    min_len = idx - table[c][1] + 1
                elif table[c][0] == max_degree and tmp_len < min_len:
                    min_len = tmp_len
        return min_len
    