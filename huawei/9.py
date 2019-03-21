class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x_tmp = x
        ans = 0
        while x>0:
            ans = ans * 10 + x % 10
            x = x//10
        return ans == x_tmp
