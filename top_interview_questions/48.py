class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix is None:
            return None
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        
        for i in range(n):
            p =  0
            q = n -1
            while p < q:
                tmp = matrix[i][p]
                matrix[i][p] = matrix[i][q]
                matrix[i][q] = tmp
                p += 1
                q -= 1
        