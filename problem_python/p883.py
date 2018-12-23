class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        grid_len = len(grid)
        for i in range(grid_len):
            for j in range(grid_len):
                if grid[i][j] != 0:
                    ans += 1
        
        for i in range(grid_len):
            tmp = max(grid[i])
            ans += tmp
        
        for j in range(grid_len):
            max_val = 0
            for i in range(grid_len):
                max_val = max(max_val, grid[i][j])
            ans += max_val
        return ans