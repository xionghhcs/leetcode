class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cnt_table = dict()
        for i in A:
            try:
                cnt_table[i] += 1
                if cnt_table[i] == len(A) // 2:
                    return i
            except:
                cnt_table[i] = 1
        