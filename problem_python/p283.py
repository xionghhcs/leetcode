class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(a, i, j):
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
        
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i + 1
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if j != len(nums):
                    swap(nums, i, j)
        