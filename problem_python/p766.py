class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            r = i
            c = 0
            while r + 1 < m and c + 1 < n:
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
                r += 1
                c += 1
        
        for j in range(n):
            r = 0
            c = j
            while r + 1 < m and c + 1 <n:
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
                r += 1
                c += 1

        return True