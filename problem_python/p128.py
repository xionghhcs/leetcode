class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set()
        for n in nums:
            table.add(n)
        ans = 0
        for n in nums:
            if n-1 not in table:
                cnt = 0
                while n in table:
                    cnt += 1
                    n += 1
                ans = max(ans, cnt)
        return ans
