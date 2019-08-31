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

class Solution2:
    """
    记忆化搜索
    """
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def dfs(i, cnt, d):
            if i < len(nums) and (i, cnt) not in d:
                d[(i, cnt)] = dfs(i+1, cnt + nums[i],d) + dfs(i + 1, cnt - nums[i],d)
            return d.get((i, cnt), int(cnt == S))
        return dfs(0,0, {})
    