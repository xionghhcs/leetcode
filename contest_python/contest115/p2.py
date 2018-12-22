class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        for i in range(N):
            new_cells = [0]*8
            for j in range(1, len(cells) - 1):
                if cells[j-1] == cells[j+1]:
                    new_cells[j] = 1
                else:
                    new_cells[j] = 0
            cells = new_cells
        return cells
