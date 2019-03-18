class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        if grid is None:
            return 0
        m, n = len(grid), len(grid[0])

        def visite_map(i,j):
            grid[i][j] = 0
            if i-1>=0 and grid[i-1][j]=='1':
                visite_map(i-1,j)
            if i+1<m and grid[i+1][j]=='1':
                visite_map(i+1,j)
            if j-1>=0 and grid[i][j-1]=='1':
                visite_map(i, j-1)
            if j+1 <n and grid[i][j+1]=='1':
                visite_map(i, j+1)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    visite_map(i, j)
        return ans
