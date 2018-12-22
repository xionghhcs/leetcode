class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        idx = 0
        while idx < len(nums):
            if nums[idx] >= target:
                return idx
            idx += 1
        return idx