
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0
        max_len = 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
            max_len = max(max_len, dp[i])
        return max_len
                    
class Solution2:
    def lengthOfLIS(self, nums):
        
        pass