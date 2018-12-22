class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex == 0:
            return [1]
        rowIndex += 1
        ans = []
        for i in range(1, rowIndex + 1):
            row = [1] * i
            for i in range(1, i -1):
                row[i] = ans[i-1] + ans[i]
            ans=row
        return ans
