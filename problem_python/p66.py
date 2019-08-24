class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [0] + digits
        idx = len(digits) - 1
        digits[idx] += 1
        while digits[idx] >= 10 and idx >0:
            digits[idx] = 0
            digits[idx - 1] += 1
            idx -= 1
        idx = 0
        while digits[idx] ==0 and idx < len(digits) - 1:
            idx += 1
        return digits[idx:]

        

class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            s = digits[i] + carry
            if i == len(digits) - 1:
                s += 1
            digits[i] = s % 10
            carry = s // 10
        if carry > 0:
            digits = [carry] + digits
        return digits
    