class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ans = []
        for i in range(1, numRows + 1):
            row = [1] * i
            for i in range(1, i -1):
                row[i] = ans[-1][i-1] + ans[-1][i]
            ans.append(row)
        return ans
