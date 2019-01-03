class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a_table = dict()
        b_table = dict()
        for w in A.split():
            if w in a_table:
                a_table[w] += 1
            else:
                a_table[w] = 1
        
        for w in B.split():
            if w in b_table:
                b_table[w] += 1
            else:
                b_table[w] = 1
        
        ans = []
        for k in a_table:
            if a_table[k] == 1:
                if k not in b_table:
                    ans.append(k)
        for k in b_table:
            if b_table[k] == 1 and k not in a_table:
                ans.append(k)
        return ans