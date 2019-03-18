class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x >= 0 else -1
        if flag == -1:
            x = -x
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
        if res>=-pow(2, 31) and res <= pow(2,31) -1:
            return flag * res
        else:
            return 0
    