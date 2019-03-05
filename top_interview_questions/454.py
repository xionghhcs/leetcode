class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        a_b = []
        for a in A:
            for b in B:
                a_b.append(a + b)
        
        table = dict()
        for c in C:
            for d in D:
                table[c+d] = table[c+d] + 1 if c+d in table else 1
        
        ans = 0
        for v in a_b:
            ans += table.get(-v, 0)
        return ans
