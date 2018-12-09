class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        def check(a):
            a.sort(reverse=True)
            hash_table = dict()

            for i in a:
                try:
                    hash_table[i] += 1
                except:
                    hash_table[i] = 1

            for i in a:
                if hash_table[i] == 0:
                    continue
                hash_table[i] -= 1

                if i % 2:
                    return False
                i = i // 2

                if i not in hash_table or hash_table[i] == 0:
                    return False

                hash_table[i] -= 1
            return True

        pos, neg = [], []
        for i in A:
            if i >=0:
                pos.append(i)
            else:
                neg.append(-i)
        return check(pos) and check(neg)




