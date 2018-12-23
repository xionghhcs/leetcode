class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def judge(n):
            hash_table = dict()
            n_origin = n
            while n > 0:
                rear = n % 10
                hash_table[rear] = 1
                n = n // 10
            if 0 in hash_table:
                return False
            for k in hash_table:
                if n_origin % k != 0:
                    return False
            return True
        ans = []
        for i in range(left, right + 1):
            if judge(i):
                ans.append(i)
        return ans
            