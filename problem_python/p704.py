class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for idx, v in enumerate(nums):
            if v == target:
                return idx
        return -1


class Solution2:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while i<=j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                j = mid - 1
                continue
            if nums[mid] < target:
                i = mid += 1
        return -1