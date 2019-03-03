class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, left, right):
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp

        def partition(nums, i, j):
            if i > j:
                return -1
            left = i + 1
            right = j
            mid_val = nums[i]
            while left < right:
                while left < right and nums[left] < mid_val:
                    left += 1
                while left < right and nums[right] >= mid_val:
                    right -= 1 
                swap(nums, left, right)    
            swap(nums, i, right)
        
        idx = partition(nums, 0, len(nums) - 1)
        partition(nums, 0, idx - 1)
        partition(nums, 0, idx + 1)
        return nums

