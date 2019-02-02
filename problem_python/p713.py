class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        product = 1
        ans = 0
        for right in range(0, len(nums)):
            product *= nums[right]
            while left <=right and product >=k:
                product = product // nums[left]
                left += 1
            ans += right - left + 1
        return ans
        