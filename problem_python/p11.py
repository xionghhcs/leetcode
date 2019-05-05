
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i = 0
        j = len(height) - 1
        while i<j:
            ans = max(ans, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans

class Solution2:
    def maxArea(self, height):
        ans = 0

        i = 0
        j = len(height) - 1
        while i < j:
            ans = max(ans, min(height[i], height[j]) * ( j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
        


        