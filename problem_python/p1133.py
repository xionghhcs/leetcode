class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        if len(A) == 0:
            return -1
        table = dict()
        for c in A:
            table[c] = table.get(c, 0) + 1
        ans = None
        for k in table:
            if table[k] == 1:
                if ans == None:
                    ans = k
                else:
                    ans = max(ans, k)
        return ans if ans is not None else -1