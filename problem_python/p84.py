class Solution:
    def largestRectangleArea(self, hs: List[int]) -> int:
        ans = 0
        for i in range(len(hs)):
            if i + 1 < len(hs) and hs[i] <= hs[i+1]:
                continue
            minH = hs[i]
            for j in range(i,-1,-1):
                minH = min(minH, hs[j])
                ans = max(ans, (i - j + 1) * minH)
        return ans
