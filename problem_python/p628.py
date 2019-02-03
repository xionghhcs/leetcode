class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = nums[0] * nums[1]
        p = nums[-2] * nums[-3]
        return  n * nums[-1] if n > p else p * nums[-1]
    