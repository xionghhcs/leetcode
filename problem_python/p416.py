class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0:
            return False
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for i in range(target, n - 1, -1):
                dp[i] = dp[i] or dp[i-n]
        return dp[target]
