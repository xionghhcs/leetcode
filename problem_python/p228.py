class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        idx = 0
        while idx < len(nums):
            j = idx + 1
            while j < len(nums) and nums[j-1] + 1 == nums[j]:
                j += 1
            if idx + 1 == j:
                ans.append(str(nums[idx]))
            else:
                ans.append('{}->{}'.format(nums[idx], nums[j - 1]))
            idx = j
        return ans


