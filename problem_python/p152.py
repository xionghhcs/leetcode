class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans, ma, mi = float('-inf'), 1, 1
        for i in range(0, len(nums)):
            if nums[i] < 0:
                ma, mi = mi, ma
            ma = max(ma * nums[i], nums[i])
            mi = min(mi * nums[i], nums[i])
            ans = max(ma, ans)
        return ans
    
        