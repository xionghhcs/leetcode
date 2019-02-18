class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        for i in range(len(board)):
            table = dict()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in table:
                    return False
                else:
                    table[board[i][j]] = 1
        
        for i in range(len(board)):
            table = dict()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in table:
                    return False
                else:
                    table[board[j][i]] = 1
        
        for row in range(0,9, 3):
            for col in range(0,9,3):
                table = dict()
                for i in range(row, row+3):
                    for j in range(col, col + 3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in table:
                            return False
                        else:
                            table[board[i][j]] = 1
        return True
