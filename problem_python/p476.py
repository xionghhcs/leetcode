class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        def get_bit(num):
            ans = []
            while num > 0:
                rear = num % 2
                ans.append(rear)
                num = num // 2
            return ans
        ans = get_bit(num)
        print(ans)
        res = 0
        base = 1
        for b in ans:
            b = 1 if b==0 else 0
            res += b * base
            base *= 2
        
        return res