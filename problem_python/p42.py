class Solution:
    def trap(self, hs: List[int]) -> int:
        if len(hs) <=2:
            return 0
        ans = 0
        left_max = [0] * len(hs)
        right_max = [0] * len(hs)
        left_max[0] = hs[0]
        right_max[-1] = hs[-1]
        for i in range(1, len(hs)):
            left_max[i] = max(left_max[i-1], hs[i])
        for j in range(len(hs)-1 - 1, -1,-1):
            right_max[j] = max(right_max[j+1], hs[j])
        for i in range(1, len(hs)-1):
            ans += min(left_max[i], right_max[i]) - hs[i]
        return ans
