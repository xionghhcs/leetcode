class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        hash_table = dict()
        hash_table[1] = 1
        hash_table[2] = 2
        def get_ans(n):
            if n in hash_table:
                return hash_table[n]
            tmp = get_ans(n -1) + get_ans(n -2)
            hash_table[n] = tmp 
            return hash_table[n]
        return get_ans(n)