class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        import collections
        dp =[collections.defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i, v in enumerate(nums):
            for s, cnt in dp[i].items():
                dp[i+1][s + v] += cnt
                dp[i+1][s-v] += cnt
        return dp[len(nums)][S]
