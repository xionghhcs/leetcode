class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums)(len(nums) + 1) / 2

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        out = -1
        for i in range(len(nums)):
            if nums[i] != i:
                idx = nums[i]
                while idx!= len(nums) and nums[idx] != idx:
                    tmp = nums[idx]
                    nums[idx] = idx
                    idx = tmp
                if idx == len(nums):
                    out = idx
        if out == -1:
            return len(nums)
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        