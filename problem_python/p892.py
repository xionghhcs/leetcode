class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    ans += 1
        
        for i in range(n):
            
            ans += max(grid[i])

        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(grid[j][i])
            ans += max(tmp)
        return ans * 2
