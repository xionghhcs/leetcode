class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        table = dict()
        for v in nums:
            if v in table:
                return v
            else:
                table[v] = 1
        return -1

class Solution2:
    def findDuplicate(self, nums):
        nums = sorted(nums)
        for i in range(0, len(nums) -1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1

