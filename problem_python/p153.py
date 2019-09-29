class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        if nums[0] < nums[-1]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1, 0, -1):
            if nums[i] < nums[i-1]:
                return nums[i]

class Solution2:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return nums[i]
        return nums[0]