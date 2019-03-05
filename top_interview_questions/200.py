class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        import copy
        flag = [['0'] * len(grid[0]) for i in range(len(grid))]

        def bfs(i, j):
            flag[i][j] = '1'
            if i -1 >= 0 and grid[i-1][j] == '1' and flag[i-1][j] == '0':
                bfs(i-1, j)
            if i+1 < len(grid) and grid[i+1][j] == '1' and flag[i+1][j] == '0':
                bfs(i+1, j)
            if j - 1 >=0 and grid[i][ j-1] == '1' and flag[i][j-1] == '0':
                bfs(i, j-1)
            if j + 1 < len(grid[0]) and grid[i][j + 1]=='1' and flag[i][j + 1] == '0':
                bfs(i, j + 1)
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and flag[i][j] == '0':
                    cnt += 1
                    bfs(i, j)
        return cnt


class Solution2:
    def numIslands(self, grid):
        pass

