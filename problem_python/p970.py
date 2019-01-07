class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        cnt_i = 0
        cnt_j = 0
        x_tmp = x
        y_tmp = y
        while x_tmp > 0:
            cnt_i += 1
            x_tmp = x_tmp // x
        while y_tmp > 0:
            cnt_j += 1
            y_tmp = y_tmp // y
        ans = []
        for i in range(cnt_i + 1):
            for j in range(cnt_j + 1):
                tmp = x ** i + y ** j
                if  tmp<=bound:
                    ans.append(tmp)
        return ans