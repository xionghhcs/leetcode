class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [[], nums]
        ans = []
        for k in self.subsets(nums[:-1]):
            for j in self.subsets([nums[-1]]):
                ans.append(k + j)
        return ans
