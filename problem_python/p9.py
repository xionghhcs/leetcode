class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = 0
        b = x
        while b > 0:
            a = a * 10 + b % 10
            b = b // 10
        return a == x