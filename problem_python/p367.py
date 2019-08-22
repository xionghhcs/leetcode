class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        j = num
        while i <= j:
            mid = (i + j) // 2
            if mid ** 2 == num:
              return True
            if mid ** 2 < num:
                i = mid + 1
            else:
                j = mid - 1
        return False
