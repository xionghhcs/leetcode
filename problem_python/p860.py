
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        table = [0] * 3
        for i in bills:
            r = i - 5
            while r > 0:
                flag = False
                while table[2] >0 and 20 <= r:
                    r -= 20
                    table[2] -= 1
                    flag = True
                while table[1] >0 and 10 <= r:
                    r -= 10
                    table[1] -= 1
                    flag = True
                while table[0] > 0 and 5 <= r:
                    r -= 5
                    table[0] -= 1
                    flag = True
                if flag is False:
                    break
            if i == 5:
                table[0] += 1
            if i == 10:
                table[1] += 1
            if i == 20:
                table[2] += 1
            if r>0:
                return False
        return True
            
