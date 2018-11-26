class Solution:
    def minFlipsMonoIncr(self, S):
        """
        @author :sharpzhao
        :type S: str
        :rtype: int
        """
        cnt_0 = 0
        cnt_1 = 0
        i = 0
        res = 0
        while i < len(S) and S[i] == 0:
            i += 1
        while i < len(S):
            if S[i] == '0':
                cnt_0 += 1
            else:
                cnt_1 += 1

            if cnt_0 > cnt_1:
                res += cnt_1
                cnt_0 = 0
                cnt_1 = 0
                while i < len(S) and S[i] == 0:
                    i += 1
            i += 1
        return res + cnt_0


