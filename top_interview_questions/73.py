class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) ==  0:
            return None
        row_flag = [0] * len(matrix)
        col_flag = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_flag[i] = 1
                    col_flag[j] = 1

        for i in range(len(matrix)):
            if row_flag[i] == 1:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        
        for j in range(len(matrix[0])):
            if col_flag[j] == 1:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        return matrix


class Solution2:
    def setZeroes(self, matrix):
        first_row_is_zero = False
        first_col_is_zero = False
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row_is_zero = True
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_is_zero = True
                break
        
        for j in range(1, len(matrix[0])):
            for i in range(len(matrix)):
                if matrix[i][j]==0:
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0
                
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        
        if first_row_is_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_col_is_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0