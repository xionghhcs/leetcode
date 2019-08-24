class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        idx = 0
        while idx < len(nums):
            if nums[idx] == 1:
                j = idx
                while j < len(nums) and nums[j]==1:
                    j += 1
                ans = max(ans, j - idx)
                idx = j
            else:
                idx += 1
        return ans
    