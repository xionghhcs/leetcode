class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        
        matrix = [[0] * c for _ in range(r)]
        idx = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                row = idx // c
                col = idx % c
                matrix[row][col] = nums[i][j]
                idx += 1
        return matrix