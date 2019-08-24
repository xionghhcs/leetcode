class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == target:
                cnt += 1
        return cnt > len(nums) // 2
    