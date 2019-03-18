class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        max_val = -1000000000000
        for v in nums:
            ans += v
            if ans > max_val:
                max_val = ans
            if ans < 0:
                ans = 0
        return max_val
    