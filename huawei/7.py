class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x >=0 else -1
        x = x * flag
        ans = 0
        while x > 0:
            ans = ans * 10 + x % 10
            x = x // 10
        ans = flag * ans
        if ans >= -pow(2, 31) and ans <= pow(2, 31) - 1:
            return ans
        return 0
