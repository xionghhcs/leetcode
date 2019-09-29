class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse(nums, i, j):
            while(i<j):
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -=1
        reverse(nums, 0, len(nums) - k - 1)
        reverse(nums, len(nums) - k, len(nums)-1)
        reverse(nums, 0 , len(nums) - 1)
