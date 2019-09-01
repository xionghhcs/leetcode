class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        c = nums[:]
        c.sort()
        i = 0
        j = len(nums) - 1
        while i < j and c[i] == nums[i]:
            i += 1
        while i < j and c[j] == nums[j]:
            j -= 1
        if i < j:
            return j - i + 1
        else:
            return 0
